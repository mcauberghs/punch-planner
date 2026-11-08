# Punch Planner

**Version 1.4.5 (2026-11-08)** · Author: Mickael Cauberghs

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
- Check vs ADP: type ADP's daily total, see ✓ or ✗ per day
- Lunch alarms: gentle chime with snooze 5/10/15/20 min (new best time shown), urgent red alarm at 55 min, stop for the day
- (i) buttons show details only when needed
- Works offline; data saved on the phone; share/save/restore a backup file, daily backup reminder

## Install on Android (Samsung Galaxy S10e)

1. Open the GitHub Pages link in **Chrome** on the phone.
2. Tap **⋮** → **Install app** (or **Add to Home screen** → **Install**).
3. Open Punch Planner from the home screen.

## Updates

After a commit, GitHub Pages needs 1–2 minutes to publish. Then open the app
with internet: it finds the new version and reloads itself once.

## Files

| File                    | Purpose                                  |
|-------------------------|------------------------------------------|
| `index.html`            | The app (HTML, CSS and JavaScript)       |
| `manifest.webmanifest`  | App name, icons, standalone mode         |
| `sw.js`                 | Service worker: offline copy of the app  |
| `icon-*.png`            | App icons                                |
| `tools/make_logo.py`    | Draws the app icons (Python + Pillow)    |

## Change log

| Version | Date       | Author             | Change |
|---------|------------|--------------------|--------|
| 1.0.0   | 2026-11-07 | Mickael Cauberghs  | First version: planner, totals, 40-hour warning, history, editor, Excel copy |
| 1.1.0   | 2026-11-07 | Mickael Cauberghs  | Standalone Android app on GitHub Pages: offline, phone storage, backup save/restore, laser time-card logo |
| 1.2.0   | 2026-11-07 | Mickael Cauberghs  | Share backup button (email, Google Drive) to move my real times to the laptop |
| 1.3.0   | 2026-11-07 | Mickael Cauberghs  | Check vs ADP (reconciliation), lunch alarms (gentle + snooze, urgent red, stop for today), (i) info buttons, daily backup reminder, remove one punch, bigger logo |
| 1.3.1   | 2026-11-07 | Mickael Cauberghs  | End-of-day box red (too early) / green (8 hours done), with (i) explanation |
| 1.4.0   | 2026-11-08 | Mickael Cauberghs  | Type times on the number keypad with AM/PM buttons (no clock picker); cleaner day editor |
| 1.4.1   | 2026-11-08 | Mickael Cauberghs  | Fix: Today's punches aligned, one per line |
| 1.4.2   | 2026-11-08 | Mickael Cauberghs  | Clearer Delete day (also in Add or edit any day), confirmation in place, Undo |
| 1.4.3   | 2026-11-08 | Mickael Cauberghs  | Delete question opens in the middle of the screen, with focus |
| 1.4.4   | 2026-11-08 | Mickael Cauberghs  | Faster updates: always checks GitHub for the newest version, reloads itself |
| 1.4.5   | 2026-11-08 | Mickael Cauberghs  | Check vs ADP table fits on the phone; "Matches ADP" label |
