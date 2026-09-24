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
8. Generate one combined report containing all conferences and events occurring during the next four complete Monday–Sunday weeks, in Seattle time.
9. Write the report using: `reports/YYYY-MM-DD - Career AI Events for [date range].md`.
10. Divide the report into two top-level sections: `Conferences` first and `Events` second. Do not generate a separate conference report.
11. Update `README.md` so the newest combined report link appears at the top.

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

Begin with a `## Conferences` section. Represent each conference once, even when it spans multiple days. Use its full date range and do not repeat it in daily event rows.

```markdown
## Conferences

| Dates | Conference | Focus | Location | Registration |
|---|---|---|---|---|
| Oct 26–30 | [Seattle AI Week](https://example.com) | AI industry and community | Seattle | Open |
```

Then add an `## Events` section with one subsection and Markdown table per week:

```markdown
## Events

### Week of September 21–27

| Date | Time | Event | Organizer | Location |
|---|---|---|---|---|
| Sep 24 | 5:00–8:00 PM | [Example event](https://example.com) | Example organizer | Seattle |
```

End every report with its generation date and a reminder that event details can change. Do not include personal attendance decisions in the public report.

For conferences within the four-week report window, include the full multi-day date range, conference name, focus, location, registration status or deadline, price when published, and official URL. Preserve unpublished details as `TBD`.
