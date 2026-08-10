#!/usr/bin/env python3
"""Generate the ISO-8601 calendar-week-number .ics file.

Regenerating just recomputes the rolling window relative to the current
date, so re-running this script periodically (see
.github/workflows/update-calendar.yml) keeps future weeks available to
subscribers without ever changing the subscribe URL.
"""

from datetime import date, datetime, timedelta, timezone

YEARS_BACK = 2
YEARS_FORWARD = 5
CALENDAR_DOMAIN = "isoweeks.mattbiegler.github.io"
OUTPUT_PATH = "docs/isoweeks.ics"


def iso_mondays(start, end):
    """Yield the Monday date of every ISO week overlapping [start, end)."""
    monday = start - timedelta(days=start.weekday())
    while monday < end:
        yield monday
        monday += timedelta(days=7)


def build_event(monday, dtstamp):
    iso_year, iso_week, _ = monday.isocalendar()
    week_end = monday + timedelta(days=7)
    uid = f"isoweek-{iso_year}-W{iso_week:02d}@{CALENDAR_DOMAIN}"
    return "\r\n".join(
        [
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTAMP:{dtstamp}",
            f"DTSTART;VALUE=DATE:{monday:%Y%m%d}",
            f"DTEND;VALUE=DATE:{week_end:%Y%m%d}",
            f"SUMMARY:Week {iso_week}",
            "TRANSP:TRANSPARENT",
            "END:VEVENT",
        ]
    )


def build_calendar(today=None):
    today = today or date.today()
    start = date(today.year - YEARS_BACK, 1, 1)
    end = date(today.year + YEARS_FORWARD + 1, 1, 1)
    dtstamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    events = [build_event(monday, dtstamp) for monday in iso_mondays(start, end)]

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//mattbiegler//ISO-8601 Calendar Week Numbers//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:ISO-8601 Week Numbers",
        "X-WR-CALDESC:All-day event for each ISO-8601 calendar week (Monday start).",
        "REFRESH-INTERVAL;VALUE=DURATION:P1D",
        "X-PUBLISHED-TTL:P1D",
        *events,
        "END:VCALENDAR",
    ]
    return "\r\n".join(lines) + "\r\n"


def main():
    calendar_text = build_calendar()
    with open(OUTPUT_PATH, "w", newline="") as f:
        f.write(calendar_text)


if __name__ == "__main__":
    main()
