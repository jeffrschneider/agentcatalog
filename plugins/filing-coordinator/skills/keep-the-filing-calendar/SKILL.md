---
name: keep-the-filing-calendar
description: Opens each filing, each tax return and the payroll year end from the calendar with the form, the deadline and the signer, asks counsel whether the form or the rule has changed, and records what each filing, return or notice taught with the next date and its lead time. Use it when running `ref/fin/file-an-indirect-tax-return` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: filing-coordinator
  agent-version: "1"
---

# Keep the filing calendar

## What it does

Opens each filing, each tax return and the payroll year end from the
calendar with the form, the deadline and the signer, asks counsel
whether the form or the rule has changed, and records what each filing,
return or notice taught with the next date and its lead time.

## Where it happens

The agent does this in seven activities across five reference processes.
Each one names the activity as that process words it.

- **Confirm What the Filing Asks For**
  - `ref/hr/file-a-required-report`, activity 2 -
    [File a Required Report](../../../../processes/human-resources/file-a-required-report.md)
- **Open the Filing From the Calendar**
  - `ref/hr/file-a-required-report`, activity 1 -
    [File a Required Report](../../../../processes/human-resources/file-a-required-report.md)
- **Open the Return From the Calendar**
  - `ref/fin/file-an-indirect-tax-return`, activity 1 -
    [File an Indirect Tax Return](../../../../processes/finance/file-an-indirect-tax-return.md)
  - `ref/fin/file-the-income-tax-return`, activity 1 -
    [File the Income Tax Return](../../../../processes/finance/file-the-income-tax-return.md)
- **Open the Year-End Close**
  - `ref/hr/close-the-payroll-year`, activity 1 -
    [Close the Payroll Year](../../../../processes/human-resources/close-the-payroll-year.md)
- **Record What the Filing Taught**
  - `ref/hr/file-a-required-report`, activity 16 -
    [File a Required Report](../../../../processes/human-resources/file-a-required-report.md)
- **Record What the Notice Taught**
  - `ref/fin/respond-to-a-tax-notice`, activity 16 -
    [Respond to a Tax Notice](../../../../processes/finance/respond-to-a-tax-notice.md)
- **Record What the Return Taught**
  - `ref/fin/file-an-indirect-tax-return`, activity 20 -
    [File an Indirect Tax Return](../../../../processes/finance/file-an-indirect-tax-return.md)
  - `ref/fin/file-the-income-tax-return`, activity 18 -
    [File the Income Tax Return](../../../../processes/finance/file-the-income-tax-return.md)

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
