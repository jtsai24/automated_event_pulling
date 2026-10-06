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

1. Read `SOURCES.md` and check every active event source with priority 80 or higher, from highest to lowest priority. Sources below 80 are documented for reference but are not part of the routine weekly pull.
2. Read `CONFERENCE_SOURCES.md` and check conference sources using a 6–12 month horizon.
3. Verify event and conference details using official organizer or registration pages when possible.
4. Compare discoveries with the event database.
5. Deduplicate by event title, date, and organizer.
6. Add clear new events and conferences, and update existing records only when material details changed.
7. Preserve missing information as `TBD`; never guess.
8. Exclude events whose eligibility is limited to current students or another group the intended audience cannot join. If an ineligible event already exists in the database, preserve the record for audit history, begin its notes with `Excluded from reports`, and remove it from current and future public reports.
9. Generate one combined report containing events from the next four complete Monday–Sunday weeks and conferences from the next two months, in Seattle time.
10. Write the report using: `reports/YYYY-MM-DD - Career AI Events for [date range].md`.
11. Divide the report into two top-level sections: `Events` first and `Conferences` second. Do not generate a separate conference report.
12. Update `README.md` so the newest combined report link appears at the top.

Seattle AI Week is a required conference check. Verify the umbrella program and its individual events through WTIA and official host pages. Add verified individual events to the database without duplicating listings found through normal event sources.

## Source-completeness requirements

A calendar landing page is a discovery index, not sufficient evidence that all of its events were checked.

For every active source with priority 80 or higher:

1. Enumerate every visible upcoming event card whose date could fall within the report window. Open each individual event page; do not rely only on the calendar landing page.
2. If a landing page omits dates, shows `TBA`, fails to render, uses an embedded calendar, or cannot be fully enumerated, use alternate public discovery routes before marking the source incomplete:
   - Search the organizer name plus the report date range.
   - Search exact visible event titles.
   - Search the organizer's Meetup group, Luma calendar, official website, and public event indexes.
   - Use targeted `site:` searches for the organizer's known domains.
3. Treat a date found on a public alternate listing as verified only after opening the individual event or registration page when possible. Preserve unresolved fields as `TBD`.
4. A source access problem does not permit silently omitting its visible event titles. Record each unresolved title as a review item.
5. For sources marked incomplete, report:
   - which discovery routes were attempted;
   - visible titles that remain unresolved;
   - how many dated events were successfully verified.
6. Before publishing, run a coverage audit for every priority-90-or-higher source and every source marked incomplete. Search again by organizer name and by each unresolved title. Compare the results with the Notion database and the draft report.
7. Do not label a run fully successful when any priority source remains incompletely checked. Label it **completed with source gaps** and list the affected sources and unresolved titles in the run summary.

### Required cross-checks for known multi-platform sources

- **AI Builders and Learners:** Check the Luma calendar first and open every event card. On Luma calendar timelines, the date and time may appear in a separate heading above the card while `To Be Announced` inside the card refers to the venue, streaming link, or location—not the event date. Never interpret that label as an unknown date when a timeline date/time is visible. If text extraction omits or detaches the timeline heading, inspect the rendered calendar visually or open the individual event page. Use Meetup or an exact-title search only when the rendered Luma event still lacks required details.
- **Union.ai / Building AI Together:** Check the official Union event page, the Building AI Together Meetup groups, and exact-title web searches. Embedded or partially rendered Union calendars are not sufficient.
- **Seattle AI Week:** Check the WTIA page, the official Luma calendar, and individual host pages.

## Required public event fields

- Date
- Time
- Event name
- Organizer
- Location or online status
- Registration URL
- Short, factual note when useful

## Report format

Begin with an `## Events` section containing one subsection and Markdown table per week:

```markdown
## Events

### Week of September 21–27

| Date | Time | Event | Organizer | Location |
|---|---|---|---|---|
| Sep 24 | 5:00–8:00 PM | [Example event](https://example.com) | Example organizer | Seattle |
```

Then add a `## Conferences` section covering the next two months. Represent each conference once, even when it spans multiple days. Use its full date range and do not repeat it in daily event rows.

```markdown
## Conferences

| Dates | Conference | Focus | Location | Registration |
|---|---|---|---|---|
| Oct 26–30 | [Seattle AI Week](https://example.com) | AI industry and community | Seattle | Open |
```

End every report with its generation date and a reminder that event details can change. Do not include personal attendance decisions in the public report.

For conferences within the two-month report window, include the full multi-day date range, conference name, focus, location, registration status or deadline, price when published, and official URL. Preserve unpublished details as `TBD`.
