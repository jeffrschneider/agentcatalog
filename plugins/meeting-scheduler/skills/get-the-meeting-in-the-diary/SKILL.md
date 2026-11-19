---
name: get-the-meeting-in-the-diary
description: Works out who comes from each side and what each is there for, offers times in the person's own time zone, and gets an invitation accepted with the joining details in it. Use it when running `ref/hr/plan-the-hire` and 6 other reference processes.
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

The agent does this in thirteen activities across seven reference
processes. Each one names the activity as that process words it.

- **Arrange the Reference Calls**
  - `ref/pc/work-an-investor-prospect`, activity 14 -
    [Work an Investor Prospect](../../../../processes/private-capital/work-an-investor-prospect.md)
- **Ask for the Candidate's Times**
  - `ref/hr/run-the-interviews`, activity 2 -
    [Run the Interviews](../../../../processes/human-resources/run-the-interviews.md)
- **Book Each Interview**
  - `ref/hr/run-the-interviews`, activity 5 -
    [Run the Interviews](../../../../processes/human-resources/run-the-interviews.md)
- **Book the Conversation**
  - `ref/sls/work-a-referral`, activity 12 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)
- **Book the Debrief**
  - `ref/hr/run-the-interviews`, activity 13 -
    [Run the Interviews](../../../../processes/human-resources/run-the-interviews.md)
- **Book the First Meeting**
  - `ref/pc/reach-out-to-a-company`, activity 12 -
    [Reach Out to a Company](../../../../processes/private-capital/reach-out-to-a-company.md)
  - `ref/pc/work-an-investor-prospect`, activity 8 -
    [Work an Investor Prospect](../../../../processes/private-capital/work-an-investor-prospect.md)
- **Book the Intake Meeting**
  - `ref/hr/plan-the-hire`, activity 2 -
    [Plan the Hire](../../../../processes/human-resources/plan-the-hire.md)
- **Book the Specification Meeting**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 2 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)
- **Confirm the Meeting**
  - `ref/sls/book-the-meeting`, activity 6 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Confirm the Start**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 17 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)
- **Decide Who Should Attend**
  - `ref/sls/book-the-meeting`, activity 3 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Hold the Panel's Dates**
  - `ref/hr/plan-the-hire`, activity 13 -
    [Plan the Hire](../../../../processes/human-resources/plan-the-hire.md)
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
