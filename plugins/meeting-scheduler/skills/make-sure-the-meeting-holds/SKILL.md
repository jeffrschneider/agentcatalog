---
name: make-sure-the-meeting-holds
description: Briefs everybody who attends, so nobody asks again what the person already answered, and reminds both sides before it. Use it when running `ref/pc/fill-a-key-role-at-a-portfolio-company` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: meeting-scheduler
  agent-version: "1"
---

# Make sure the meeting holds

## What it does

Briefs everybody who attends, so nobody asks again what the person
already answered, and reminds both sides before it. Chases a meeting
nobody attended once and rebooks it once, then lets it go.

## Where it happens

The agent does this in six activities across four reference processes.
Each one names the activity as that process words it.

- **Brief the Attendees**
  - `ref/sls/book-the-meeting`, activity 7 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Brief the Partner**
  - `ref/pc/reach-out-to-a-company`, activity 13 -
    [Reach Out to a Company](../../../../processes/private-capital/reach-out-to-a-company.md)
- **Handle a No-Show**
  - `ref/sls/book-the-meeting`, activity 10 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Hold the Follow-Up Meetings**
  - `ref/pc/work-an-investor-prospect`, activity 13 -
    [Work an Investor Prospect](../../../../processes/private-capital/work-an-investor-prospect.md)
- **Remind Before the Meeting**
  - `ref/sls/book-the-meeting`, activity 8 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Run the Interviews**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 11 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)

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
