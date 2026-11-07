# Punch Planner

**Version 1.1.0 (2026-11-07)** · Author: Mickael Cauberghs

A small Android app (installable web app) that tells me the best time to punch
in and out on the ADP timecard, so I work a real 8:00 per day, take a real
30-minute lunch, and the quarter-hour rounding never works against me.

## Rounding rule (ADP, 7-minute rule)

| Minutes after a quarter hour | Rounds to          | Example        |
|------------------------------|--------------------|----------------|
| 0–7                          | back (earlier)     | 8:37 → 8:30    |
| 8–14                         | forward (later)    | 8:38 → 8:45    |

## Features

- One big button for the 4 daily punches (in, lunch out, lunch in, out)
- Best punch window for each step, with a countdown
- End-of-day time for **real 8:00** and **8.00 card hours**
- Daily and weekly totals: real time vs. card time
- Warning above 40 card hours per week
- History with search by day, week, month or custom dates
- Edit a day, add notes, copy a period for Excel
- Works offline; data saved on the phone; backup file save/restore

## Install on Android (Samsung Galaxy S10e)

1. Open the GitHub Pages link in **Chrome** on the phone.
2. Tap **⋮** → **Install app** (or **Add to Home screen** → **Install**).
3. Open Punch Planner from the home screen.

## Files

| File                    | Purpose                                  |
|-------------------------|------------------------------------------|
| `index.html`            | The app (HTML, CSS and JavaScript)       |
| `manifest.webmanifest`  | App name, icons, standalone mode         |
| `sw.js`                 | Service worker: offline copy of the app  |
| `icon-*.png`            | App icons                                |

## Change log

| Version | Date       | Author             | Change |
|---------|------------|--------------------|--------|
| 1.0.0   | 2026-11-07 | Mickael Cauberghs  | First version: planner, totals, 40-hour warning, history, editor, Excel copy |
| 1.1.0   | 2026-11-07 | Mickael Cauberghs  | Standalone Android app on GitHub Pages: offline, phone storage, backup save/restore, laser time-card logo |
