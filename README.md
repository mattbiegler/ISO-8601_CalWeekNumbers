# ISO-8601 Calendar Week Numbers

A subscribable calendar that adds one all-day event per week, labeled "Week N", using the ISO-8601 definition of a calendar week: weeks start on Monday, and week 1 of a year is the week containing that year's first Thursday (equivalently, the first week with at least 4 days in the new year).

Each event spans the full Monday-Sunday week, has no reminders, and is marked as free/transparent so it never shows you as busy.

## Subscribe

**webcal (recommended — updates automatically):**

```
webcal://mattbiegler.github.io/ISO-8601_CalWeekNumbers/isoweeks.ics
```

**https (same file, use if your app doesn't support webcal://):**

```
https://mattbiegler.github.io/ISO-8601_CalWeekNumbers/isoweeks.ics
```

The URL never changes, even as new weeks are added, so you only need to subscribe once.

### iOS / macOS (Apple Calendar)

- Tap or click the `webcal://` link above and confirm the subscription, **or**
- iOS: Settings → Calendar → Accounts → Add Account → Other → Add Subscribed Calendar, and paste the `https://` link.
- macOS: Calendar app → File → New Calendar Subscription, and paste the `https://` link.

### Google Calendar (Android + web)

Google Calendar only supports adding subscriptions from the web UI, but it then syncs to the Android/iOS apps automatically:

- On calendar.google.com → "Other calendars" (+) → "From URL" → paste the `https://` link.

### Outlook

- Outlook.com / new Outlook: Add calendar → Subscribe from web → paste the `https://` link.
- Outlook desktop (classic): Calendar view → Add Calendar → From Internet → paste the `https://` link.

## How it stays current

`generate_ics.py` generates events for a rolling window (2 years back through 5 years forward) relative to whenever it's run. A scheduled GitHub Action (`.github/workflows/update-calendar.yml`) re-runs it on the 1st of every month and commits the regenerated file, so the calendar keeps extending into the future without anyone needing to edit anything — and without the subscribe URL ever changing.

## Regenerating manually

```
python generate_ics.py
```

This overwrites `docs/isoweeks.ics`, which is what GitHub Pages serves.
