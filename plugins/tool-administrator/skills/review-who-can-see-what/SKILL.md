---
name: review-who-can-see-what
description: Opens the access review for a period with its systems, its access owners and its dates, lists every account with its role, its permissions and its last use, and every report, export and link that carries data out, and matches each account to a current employee, an approved service or nobody. Use it when running `ref/hr/review-access-to-employee-data`.
license: CC-BY-4.0
metadata:
  agent: tool-administrator
  agent-version: "1"
---

# Review who can see what

## What it does

Opens the access review for a period with its systems, its access owners
and its dates, lists every account with its role, its permissions and
its last use, and every report, export and link that carries data out,
and matches each account to a current employee, an approved service or
nobody. It flags access wider than the job needs and roles that clash,
sends each owner the accesses they answer for, and on the close date
removes the access nobody approved.

## Where it happens

The agent does this in seven activities across one reference process.
Each one names the activity as that process words it.

- **Check Each Role Against the Job**
  - `ref/hr/review-access-to-employee-data`, activity 8 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)
- **List Every Account and Its Role**
  - `ref/hr/review-access-to-employee-data`, activity 2 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)
- **List the Exports and Links**
  - `ref/hr/review-access-to-employee-data`, activity 3 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)
- **Match Each Account to a Person**
  - `ref/hr/review-access-to-employee-data`, activity 4 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)
- **Open the Review for the Period**
  - `ref/hr/review-access-to-employee-data`, activity 1 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)
- **Remove the Access Nobody Approved**
  - `ref/hr/review-access-to-employee-data`, activity 11 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)
- **Send Each Owner Their Accounts**
  - `ref/hr/review-access-to-employee-data`, activity 9 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)

## What to record

The entry as it was taken on: the owner, the licence, the term and the
process the tool runs. Every account open today with its role and its
named approver, and every closure with its date and how long the account
stood after the leaving record. The configuration at a version, each
change carrying its date, the request behind it, what the trial away
from live showed, and the way back that was kept. Each licence count
setting licences paid for against licences used, naming every licence
unused past the limit. Every refused request, with the reason and the
process it belongs to. The review recorded with its decision, its date,
the evidence it was made on and the date the next one falls. In a
retirement: who was told and when, the export with everything the tool
held that it could not take, every link stopped with what it was
carrying, the read-only date, the closed accounts, the notice given and
the final invoice.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
