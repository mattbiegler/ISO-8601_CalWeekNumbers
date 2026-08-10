# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## General Requirements

1. Be professional, expect professional results.
2. Discuss design and get confirmation before doing actual development.
3. Consider development based on best practices. Clean, reusable, simple, easily readable, etc.

## Project Requirements

1. Calendar import for showing week numbers according to ISO-8601 standard. Monday start, requiring 4 days to be new week.
2. I want people to be able to import calendar into iOS, macOS, Android or any other common device calendar.
3. Ideally would like to have it automatically update calendars if people are subscribed to it and changes were made.
4. I want the events on the calendar to be set for all-day for the entire week. 
5. Name of event should be Week # with # replaced with the actual week number.
6. The event should not have any reminders and should always be open on calendars so it doesn't show people as busy for the whole week.
7. Consider this project as being able to create that calendar, but have the ability to add to it or change if wantiong and the link that people subscribe to doesn't change, but would like the subscribe link to be hosted on github, if possible.
8. Update README.md with relevant information on how people using the calendar should connect it/subscribe to it. Include any relevant info.

## Architecture

- `generate_ics.py` — stdlib-only Python script. Computes a rolling window (2 years back through 5 years forward of the current date) and emits one `VEVENT` per ISO-8601 week via `date.isocalendar()`, which already implements the Monday-start / first-Thursday week-1 rule. Writes `docs/isoweeks.ics`.
- `docs/isoweeks.ics` — generated output, served by GitHub Pages (Pages source: `main` branch, `/docs` folder). This is the file subscribers' calendar apps fetch; do not hand-edit it.
- `.github/workflows/update-calendar.yml` — monthly cron (`workflow_dispatch` also available) that re-runs the generator and commits the result if it changed. This is what keeps the rolling window current without ever changing the subscribe URL.

Each generated event's `UID` is derived from its ISO year/week (not generation time), so regeneration updates events in place rather than creating duplicates.

## Commands

- Regenerate the calendar: `python generate_ics.py`
- No lint/test suite exists yet; there is a single script with no external dependencies.
