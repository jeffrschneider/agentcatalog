---
name: prepare-from-checked-data
description: Gathers only the fields a form asks for, prepares each filing and annual return from checked or reconciled figures with each figure traced, explains each change from the last filing, and checks that the year-end statements add up to the returns. Use it when running `ref/hr/close-the-payroll-year` and `ref/hr/file-a-required-report`.
license: CC-BY-4.0
metadata:
  agent: filing-coordinator
  agent-version: "1"
---

# Prepare from checked data

## What it does

Gathers only the fields a form asks for, prepares each filing and annual
return from checked or reconciled figures with each figure traced,
explains each change from the last filing, and checks that the year-end
statements add up to the returns.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Statements Against the Returns**
  - `ref/hr/close-the-payroll-year`, activity 11 -
    [Close the Payroll Year](../../../../processes/human-resources/close-the-payroll-year.md)
- **Compare With the Last Filing**
  - `ref/hr/file-a-required-report`, activity 10 -
    [File a Required Report](../../../../processes/human-resources/file-a-required-report.md)
- **Gather the Data the Filing Needs**
  - `ref/hr/file-a-required-report`, activity 3 -
    [File a Required Report](../../../../processes/human-resources/file-a-required-report.md)
- **Prepare the Annual Returns**
  - `ref/hr/close-the-payroll-year`, activity 9 -
    [Close the Payroll Year](../../../../processes/human-resources/close-the-payroll-year.md)
- **Prepare the Filing**
  - `ref/hr/file-a-required-report`, activity 9 -
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
