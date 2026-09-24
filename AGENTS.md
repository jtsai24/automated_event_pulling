# Event Report Instructions

## Purpose

Discover relevant career, AI, software, and technical networking events and publish a clear weekly report.

## System boundaries

- `SOURCES.md` defines the public sources and their scan priority.
- The current event database is the Notion **Upcoming Career Events** database: https://app.notion.com/p/3b48d66b99dd80ec9c99fd6b3309ffa3
- Notion is a replaceable storage implementation. A future database may be used if it provides the same event fields and supports deduplication and updates.
- `reports/` contains public generated reports.
- Never publish private notes, personal contacts, or information that cannot be verified publicly.

## Weekly workflow

1. Read `SOURCES.md` and check sources from highest to lowest priority.
2. Verify event details using official organizer or registration pages when possible.
3. Compare discoveries with the event database.
4. Deduplicate by event title, date, and organizer.
5. Add clear new events and update existing events only when material details changed.
6. Preserve missing information as `TBD`; never guess.
7. Generate a four-week report in Seattle time.
8. Write the report using the existing naming format: `reports/YYYY-MM-DD - Career AI Events for [date range].md`.
9. Update the **Latest report** link at the top of `README.md` to point directly to the newly generated report.

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
