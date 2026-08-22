---
name: get-the-meeting-in-the-diary
description: Works out who comes from each side and what each is there for, offers times in the person's own time zone, and gets an invitation accepted with the joining details in it. Use it when running `ref/sls/book-the-meeting` and `ref/sls/work-a-referral`.
license: CC-BY-4.0
metadata:
  agent: meeting-scheduler
  agent-version: "1"
---

# Get the meeting in the diary

## What it does

Works out who comes from each side and what each is there for, offers
times in the person's own time zone, and gets an invitation accepted
with the joining details in it. The diary has to hold the meeting, not a
note about it.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Book the Conversation**
  - `ref/sls/work-a-referral`, activity 12 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)
- **Confirm the Meeting**
  - `ref/sls/book-the-meeting`, activity 6 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Decide Who Should Attend**
  - `ref/sls/book-the-meeting`, activity 3 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Offer Times**
  - `ref/sls/book-the-meeting`, activity 5 -
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
