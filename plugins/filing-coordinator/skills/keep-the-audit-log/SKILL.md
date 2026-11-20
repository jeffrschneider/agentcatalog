---
name: keep-the-audit-log
description: Logs an audit or a tax authority's notice with its authority, scope and dates, confirms who is asking or that the notice is genuine against the authority's published details, logs each request with its due date and owner, sends each signed or approved response and logs what went, logs each follow-up, finding and proposed adjustment with its owner and date, and closes the audit or the notice on the record with its receipt once counsel lifts any hold. Use it when running `ref/fin/respond-to-a-tax-audit`, `ref/fin/respond-to-a-tax-notice` and `ref/hr/respond-to-an-employment-audit`.
license: CC-BY-4.0
metadata:
  agent: filing-coordinator
  agent-version: "1"
---

# Keep the audit log

## What it does

Logs an audit or a tax authority's notice with its authority, scope and
dates, confirms who is asking or that the notice is genuine against the
authority's published details, logs each request with its due date and
owner, sends each signed or approved response and logs what went, logs
each follow-up, finding and proposed adjustment with its owner and date,
and closes the audit or the notice on the record with its receipt once
counsel lifts any hold.

## Where it happens

The agent does this in eleven activities across three reference
processes. Each one names the activity as that process words it.

- **Answer the Follow-Ups**
  - `ref/hr/respond-to-an-employment-audit`, activity 14 -
    [Respond to an Employment Audit](../../../../processes/human-resources/respond-to-an-employment-audit.md)
- **Close the Audit on the Record**
  - `ref/fin/respond-to-a-tax-audit`, activity 20 -
    [Respond to a Tax Audit](../../../../processes/finance/respond-to-a-tax-audit.md)
  - `ref/hr/respond-to-an-employment-audit`, activity 18 -
    [Respond to an Employment Audit](../../../../processes/human-resources/respond-to-an-employment-audit.md)
- **Close the Notice With Its Receipt**
  - `ref/fin/respond-to-a-tax-notice`, activity 15 -
    [Respond to a Tax Notice](../../../../processes/finance/respond-to-a-tax-notice.md)
- **Confirm Who Is Asking and on What Authority**
  - `ref/fin/respond-to-a-tax-audit`, activity 2 -
    [Respond to a Tax Audit](../../../../processes/finance/respond-to-a-tax-audit.md)
  - `ref/hr/respond-to-an-employment-audit`, activity 2 -
    [Respond to an Employment Audit](../../../../processes/human-resources/respond-to-an-employment-audit.md)
- **Confirm the Notice Is Genuine**
  - `ref/fin/respond-to-a-tax-notice`, activity 2 -
    [Respond to a Tax Notice](../../../../processes/finance/respond-to-a-tax-notice.md)
- **Log Each Finding**
  - `ref/hr/respond-to-an-employment-audit`, activity 15 -
    [Respond to an Employment Audit](../../../../processes/human-resources/respond-to-an-employment-audit.md)
- **Log Each Proposed Adjustment**
  - `ref/fin/respond-to-a-tax-audit`, activity 14 -
    [Respond to a Tax Audit](../../../../processes/finance/respond-to-a-tax-audit.md)
- **Log Each Request**
  - `ref/fin/respond-to-a-tax-audit`, activity 5 -
    [Respond to a Tax Audit](../../../../processes/finance/respond-to-a-tax-audit.md)
  - `ref/hr/respond-to-an-employment-audit`, activity 5 -
    [Respond to an Employment Audit](../../../../processes/human-resources/respond-to-an-employment-audit.md)
- **Log the Audit**
  - `ref/fin/respond-to-a-tax-audit`, activity 1 -
    [Respond to a Tax Audit](../../../../processes/finance/respond-to-a-tax-audit.md)
  - `ref/hr/respond-to-an-employment-audit`, activity 1 -
    [Respond to an Employment Audit](../../../../processes/human-resources/respond-to-an-employment-audit.md)
- **Log the Notice**
  - `ref/fin/respond-to-a-tax-notice`, activity 1 -
    [Respond to a Tax Notice](../../../../processes/finance/respond-to-a-tax-notice.md)
- **Send the Response and Log It**
  - `ref/fin/respond-to-a-tax-audit`, activity 13 -
    [Respond to a Tax Audit](../../../../processes/finance/respond-to-a-tax-audit.md)
  - `ref/fin/respond-to-a-tax-notice`, activity 10 -
    [Respond to a Tax Notice](../../../../processes/finance/respond-to-a-tax-notice.md)
  - `ref/hr/respond-to-an-employment-audit`, activity 13 -
    [Respond to an Employment Audit](../../../../processes/human-resources/respond-to-an-employment-audit.md)

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
