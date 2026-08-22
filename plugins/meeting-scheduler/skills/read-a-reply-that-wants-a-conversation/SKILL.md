---
name: read-a-reply-that-wants-a-conversation
description: Takes in a reply that wants to talk, with the thread and the touch that caused it, and reads what the person actually asked for and how soon they want it. Use it when running `ref/sls/book-the-meeting`, `ref/sls/run-an-outbound-sequence` and `ref/sls/work-a-referral`.
license: CC-BY-4.0
metadata:
  agent: meeting-scheduler
  agent-version: "1"
---

# Read a reply that wants a conversation

## What it does

Takes in a reply that wants to talk, with the thread and the touch that
caused it, and reads what the person actually asked for and how soon
they want it. An introduction that lands is taken in the same way.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Hand over the Positive Replies**
  - `ref/sls/run-an-outbound-sequence`, activity 15 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)
- **Read What They Asked For**
  - `ref/sls/book-the-meeting`, activity 2 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Take in the Reply**
  - `ref/sls/book-the-meeting`, activity 1 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Take the Handover**
  - `ref/sls/work-a-referral`, activity 11 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)

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
