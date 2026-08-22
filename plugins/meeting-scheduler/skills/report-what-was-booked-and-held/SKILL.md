---
name: report-what-was-booked-and-held
description: Reports what was booked, what held and what was missed, and reads back which replies turned into meetings that actually happened. Use it when running `ref/sls/book-the-meeting`.
license: CC-BY-4.0
metadata:
  agent: meeting-scheduler
  agent-version: "1"
---

# Report what was booked and held

## What it does

Reports what was booked, what held and what was missed, and reads back
which replies turned into meetings that actually happened.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Record What Was Learned**
  - `ref/sls/book-the-meeting`, activity 16 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Report the Bookings**
  - `ref/sls/book-the-meeting`, activity 15 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)

## What to record

Per booking: the reply and the touch that caused it, what the person
asked for and how soon, who was coming from each side and what each was
for, the times offered and the time zone they were offered in, the
accepted invitation with its joining details, the brief as every
attendee read it, and the reminder with whether both sides acknowledged.
Per held meeting: the write-up against the account inside the stated
hours, the recording where one was agreed and the notice that was read
out, the decision to go forward or stop, and the next step with a date
on it. Per missed meeting: the chase, the rebooking, and the point at
which it was let go.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
