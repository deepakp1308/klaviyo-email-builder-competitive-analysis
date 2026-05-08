"""Parse cached VOC JSONL files and extract email-builder-relevant messages with MRR.

Output:
  voc_emailbuilder.json  — list of {channel, ts, ts_human, user, mrr, plan, prs, text, permalink, fullstory}

Filtering:
  - Keep only messages mentioning email builder concepts.
  - Keep only messages within last 18 months.
"""
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path("/Users/dprabhakara/cursor")
SOURCES = {
    "C051Y4H98VB": ("#hvc_feedback", ROOT / "voc_raw_C051Y4H98VB.jsonl"),
    "C095FJ3SQF4": ("#mc-hvc-escalations", ROOT / "voc_raw_C095FJ3SQF4.jsonl"),
}
OUT = Path("/Users/dprabhakara/cursor/klaviyo-email-builder-competitive-analysis/voc_emailbuilder.json")

# 18 months ago from today (May 8, 2026 → Nov 8, 2024)
EIGHTEEN_MONTHS_AGO = datetime(2024, 11, 8, tzinfo=timezone.utc).timestamp()

# Email builder relevant keywords — must match strong builder/editor signals
BUILDER_KEYWORDS = re.compile(
    r"\b("
    r"email\s*builder|new\s*builder|new\s*editor|email\s*editor|new\s*email|"
    r"template\s*editor|template\s*builder|campaign\s*builder|"
    r"new\s*campaign\s*builder|nbe|drag(?:\s|-)?and(?:\s|-)?drop|drag\s*-?\s*drop|"
    r"content\s*studio|creative\s*assistant|intuit\s*assist|write\s*with\s*ai|"
    r"text\s*block|image\s*block|button\s*block|product\s*block|content\s*block|code\s*block|"
    r"saved\s*template|template\s*library|saved\s*content|brand\s*kit|brand\s*style|"
    r"merge\s*tag|conditional\s*content|dynamic\s*content|"
    r"image\s*editor|crop|resize|upload\s*image|file\s*manager|content\s*studio|"
    r"design\s*element|design\s*the\s*email|email\s*design|edit\s*layout|"
    r"font\s+color|font\s+size|change\s+font|line\s+spacing|spacing\s+issue|"
    r"alignment|column|footer|header\s+block|"
    r"editor|builder|template|"
    r"preview\s*pane|test\s*email|inbox\s*preview|mobile\s*view|mobile\s*preview|dark\s*mode|"
    r"hyperlink|link\s+button|insert\s+link|html\s+code"
    r")\b",
    re.IGNORECASE,
)

# Strong off-topic exclusions — if feedback is solely about these, drop
EXCLUDE_TOPICS = re.compile(
    r"\b("
    r"price|pricing|charge\s+me|invoice|invoicing|refund|billing|"
    r"deliverabilit|bounce\s+rate|spam\s+folder|dkim|dmarc|domain\s+auth|"
    r"customer\s+support|live\s+chat|phone\s+support|chatbot\s+support|"
    r"sms\s+credit|sms\s+marketing|"
    r"audience\s+management|contact\s+import|integration"
    r")\b",
    re.IGNORECASE,
)


def is_builder_relevant(text: str) -> bool:
    """Return True if message is more about builder than off-topic noise."""
    if not text:
        return False
    builder_hits = len(BUILDER_KEYWORDS.findall(text))
    off_topic_hits = len(EXCLUDE_TOPICS.findall(text))
    # require more builder signal than off-topic
    return builder_hits >= 1 and builder_hits >= off_topic_hits

# MRR / plan extraction
MRR_RE = re.compile(r"\*?MRR:?\*?\s*\$?(\d{1,5}(?:[.,]\d{1,2})?)", re.IGNORECASE)
PLAN_RE = re.compile(r"\*?(Free|Essentials|Standard|Premium|Plus|Lite|Foundations)\s+plan\*?", re.IGNORECASE)
USER_ID_RE = re.compile(r"\*?User\s*ID:?\*?\s*(\d+)", re.IGNORECASE)
PRS_RE = re.compile(r"\*?PRS:?\*?\s*(\d+)", re.IGNORECASE)
REASON_RE = re.compile(r"\*?Reason:?\*?\s*([^\n*]+)", re.IGNORECASE)
FEEDBACK_RE = re.compile(r"\*?Feedback:?\*?\s*([\s\S]+?)(?=\n\n|\n\*|\Z)", re.IGNORECASE)
FULLSTORY_RE = re.compile(r"https://app\.fullstory\.com/[^\s|>]+")
TS_RE = re.compile(r"Message TS:\s*([\d.]+)")
TIME_RE = re.compile(r"=== Message from .*? at (\S+ \S+ \S+) ===")

# Split a "messages" field into individual messages
SPLITTER = re.compile(r"=== Message from (.*?) at (.*?) ===")


def split_messages(blob: str):
    """Yield (header, body) for each message in a channel page blob."""
    parts = SPLITTER.split(blob)
    # parts: [prefix, sender1, time1, body1, sender2, time2, body2, ...]
    if len(parts) < 4:
        return
    for i in range(1, len(parts), 3):
        sender = parts[i].strip()
        time_str = parts[i + 1].strip()
        body = parts[i + 2].strip() if i + 2 < len(parts) else ""
        yield sender, time_str, body


def parse_time(ts_str: str):
    """Parse '2026-05-05 15:59:30 PDT' → unix ts."""
    try:
        # Strip TZ name; assume PT offsets (PDT=-7h, PST=-8h)
        m = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s*([A-Z]{2,4})?", ts_str)
        if not m:
            return None
        dt_str, tz = m.group(1), m.group(2) or "UTC"
        dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        offsets = {"PDT": -7, "PST": -8, "EDT": -4, "EST": -5, "UTC": 0}
        tz_offset = offsets.get(tz, 0)
        dt = dt.replace(tzinfo=timezone(timedelta(hours=tz_offset)))
        return dt.timestamp()
    except Exception:
        return None


NOISE_MARKERS = re.compile(
    r"^(received\*?\s*:postal_horn:|badge\*?|top!?|non|none|na|n/a|"
    r"buen|bom|bueno|good|great|perfect|nice|excellent|love|"
    r"\*?reactions?:?\*?|reactions?\s+from)\s*$",
    re.IGNORECASE,
)


def extract_record(channel_id: str, channel_name: str, sender: str, time_str: str, body: str):
    # Run builder relevance against feedback content (post-extraction) for accuracy
    feedback_text = ""
    m = FEEDBACK_RE.search(body)
    if m:
        feedback_text = m.group(1).strip()
    # Drop noise: too short, escalation tracking pings, sentiment-only messages
    if len(feedback_text.strip()) < 25:
        return None
    if NOISE_MARKERS.match(feedback_text.strip()):
        return None
    full_for_match = (feedback_text + "\n" + body)
    if not is_builder_relevant(full_for_match):
        return None
    ts = parse_time(time_str)
    if ts is None or ts < EIGHTEEN_MONTHS_AGO:
        return None
    mrr = None
    m = MRR_RE.search(body)
    if m:
        try:
            mrr = float(m.group(1).replace(",", ""))
        except Exception:
            mrr = None
    plan = None
    m = PLAN_RE.search(body)
    if m:
        plan = m.group(1).title()
    user_id = None
    m = USER_ID_RE.search(body)
    if m:
        user_id = m.group(1)
    prs = None
    m = PRS_RE.search(body)
    if m:
        try:
            prs = int(m.group(1))
        except Exception:
            prs = None
    reason = None
    m = REASON_RE.search(body)
    if m:
        raw = m.group(1).strip()
        # strip CSS pollution / mso tags
        if "<style" in raw or "mso-" in raw or "td {" in raw:
            reason = None
        else:
            reason = raw[:120]
    feedback = None
    m = FEEDBACK_RE.search(body)
    if m:
        feedback = m.group(1).strip()
    msg_ts = None
    m = TS_RE.search(body)
    if m:
        msg_ts = m.group(1)
    fs = FULLSTORY_RE.search(body)
    fullstory = fs.group(0) if fs else None

    permalink = None
    if msg_ts:
        ts_dot = msg_ts
        ts_no_dot = ts_dot.replace(".", "")
        permalink = f"https://intuit.enterprise.slack.com/archives/{channel_id}/p{ts_no_dot}"

    return {
        "channel_id": channel_id,
        "channel": channel_name,
        "ts": ts,
        "ts_human": datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d"),
        "sender": sender,
        "user_id": user_id,
        "mrr": mrr,
        "plan": plan,
        "prs": prs,
        "reason": reason,
        "feedback": feedback,
        "msg_ts": msg_ts,
        "permalink": permalink,
        "fullstory": fullstory,
    }


def main():
    records = []
    for channel_id, (name, path) in SOURCES.items():
        if not path.exists():
            print(f"MISSING {path}", file=sys.stderr)
            continue
        with path.open() as f:
            for line in f:
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                blob = obj.get("messages", "")
                for sender, time_str, body in split_messages(blob):
                    rec = extract_record(channel_id, name, sender, time_str, body)
                    if rec:
                        records.append(rec)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w") as f:
        json.dump(records, f, indent=2, default=str)

    # Quick stats
    print(f"Total records: {len(records)}")
    if records:
        with_mrr = [r for r in records if r["mrr"] is not None]
        hvc = [r for r in records if r["mrr"] is not None and r["mrr"] >= 299]
        print(f"  with MRR: {len(with_mrr)}")
        print(f"  HVC ($299+ MRR): {len(hvc)}")
        if hvc:
            total_hvc_mrr = sum(r["mrr"] for r in hvc)
            print(f"  Total HVC MRR: ${total_hvc_mrr:,.0f}/mo")
        by_channel = {}
        for r in records:
            by_channel[r["channel"]] = by_channel.get(r["channel"], 0) + 1
        print("  By channel:", by_channel)
        dates = [r["ts_human"] for r in records]
        print(f"  Date range: {min(dates)} → {max(dates)}")


if __name__ == "__main__":
    main()
