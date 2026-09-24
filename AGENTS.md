# Event Report Instructions

## Purpose

Discover relevant career, AI, software, and technical networking events and publish a clear weekly report.

## System boundaries

- `SOURCES.md` defines the public sources and their scan priority.
- `CONFERENCE_SOURCES.md` defines major-conference sources and known conferences requiring verification.
- The current event database is the Notion **Upcoming Career Events** database: https://app.notion.com/p/3b48d66b99dd80ec9c99fd6b3309ffa3
- Notion is a replaceable storage implementation. A future database may be used if it provides the same event fields and supports deduplication and updates.
- `reports/` contains public generated reports.
- Never publish private notes, personal contacts, or information that cannot be verified publicly.

## Weekly workflow

1. Read `SOURCES.md` and check sources from highest to lowest priority.
2. Read `CONFERENCE_SOURCES.md` and check conference sources using a 6–12 month horizon.
3. Verify event and conference details using official organizer or registration pages when possible.
4. Compare discoveries with the event database.
5. Deduplicate by event title, date, and organizer.
6. Add clear new events and conferences, and update existing records only when material details changed.
7. Preserve missing information as `TBD`; never guess.
8. Generate a four-week event report in Seattle time.
9. Write the event report using: `reports/YYYY-MM-DD - Career AI Events for [date range].md`.
10. Generate a separate conference report covering verified conferences in the next 6–12 months.
11. Write it using: `reports/YYYY-MM-DD - Conference Watch.md`.
12. Update `README.md` so the newest event report and Conference Watch links appear at the top.

Seattle AI Week is a required conference check. Verify the umbrella program and its individual events through WTIA and official host pages. Add verified individual events to the database without duplicating listings found through normal event sources.

## Required public event fields

- Date
- Time
- Event name
- Organizer
- Location or online status
- Registration URL
- Short, factual note when useful

## Report format

Use one section per week and one Markdown table per section:

```markdown
## Week of September 21–27

| Date | Time | Event | Organizer | Location |
|---|---|---|---|---|
| Sep 24 | 5:00–8:00 PM | [Example event](https://example.com) | Example organizer | Seattle |
```

End every report with its generation date and a reminder that event details can change. Do not include personal attendance decisions in the public report.

The Conference Watch should include conference name, dates, location, focus, registration status or deadline, price when published, and official URL. Preserve unpublished details as `TBD`.
