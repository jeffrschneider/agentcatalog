---
name: file-by-the-deadline
description: Files each signed filing and return through the authority's route by its deadline, keeps the receipt, the filed copy and the data at a version, answers the authority's follow-ups from the kept data, and files any correction with its own receipt. Use it when running `ref/hr/close-the-payroll-year` and `ref/hr/file-a-required-report`.
license: CC-BY-4.0
metadata:
  agent: filing-coordinator
  agent-version: "1"
---

# File by the deadline

## What it does

Files each signed filing and return through the authority's route by its
deadline, keeps the receipt, the filed copy and the data at a version,
answers the authority's follow-ups from the kept data, and files any
correction with its own receipt.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Answer the Authority's Follow-Ups**
  - `ref/hr/file-a-required-report`, activity 15 -
    [File a Required Report](../../../../processes/human-resources/file-a-required-report.md)
- **File a Corrected Return**
  - `ref/hr/close-the-payroll-year`, activity 16 -
    [Close the Payroll Year](../../../../processes/human-resources/close-the-payroll-year.md)
- **File by the Deadline**
  - `ref/hr/file-a-required-report`, activity 13 -
    [File a Required Report](../../../../processes/human-resources/file-a-required-report.md)
- **File the Returns**
  - `ref/hr/close-the-payroll-year`, activity 13 -
    [Close the Payroll Year](../../../../processes/human-resources/close-the-payroll-year.md)
- **Keep the Receipt**
  - `ref/hr/file-a-required-report`, activity 14 -
    [File a Required Report](../../../../processes/human-resources/file-a-required-report.md)

## What to record

Each filing leaves the authority, the location, the period, the form,
the deadline and the named signer, counsel's answer on whether the form
or the rule changed, the fields gathered at their date and nothing more,
the filing at a version with each figure traced to its data, each change
from the last filing explained, the review and the signature with who
gave them, the date it was filed, and the receipt, the filed copy and
the data kept for `<your jurisdiction's retention period>`. It also
leaves each follow-up and correction, and the next date on the calendar
with its lead time. The payroll year end leaves every return and
deadline for each place with the timetable counted back from it, each
annual return prepared from the reconciled figures, the check of the
statements against the returns person by person and in total, each
return filed with its receipt, and any corrected return with its own
receipt beside the first. An audit leaves the authority, the scope, the
period and every date, each request numbered with its due date and its
owner, each response as signed and sent with what went, when, to whom
and at which version, every record shown and question asked during an
inspection, each finding with what it rests on, its owner and its date,
and the closing letter with the hold lifted. Nothing in the record shows
this agent signing a filing or deciding the company's position on a
finding.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
