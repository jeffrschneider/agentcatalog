---
name: answer-for-a-published-report
description: Answers the questions the readers of a published report raise, beside the person who holds the relationship with them, and logs each one against the version it asks about, and records each decision a reader takes with its owner and its date for the next report. Use it when running `ref/fin/report-the-monthly-results` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: reporting-manager
  agent-version: "1"
---

# Answer for a published report

## What it does

Answers the questions the readers of a published report raise, beside
the person who holds the relationship with them, and logs each one
against the version it asks about, and records each decision a reader
takes with its owner and its date for the next report. Then records what
the period's report taught: what was late, what was corrected, what was
asked, and what the next report changes.

## Where it happens

The agent does this in seven activities across four reference processes.
Each one names the activity as that process words it.

- **Answer the Investors' Questions**
  - `ref/pc/issue-the-quarterly-report-and-statements`, activity 16 -
    [Issue the Quarterly Report and Statements](../../../../processes/private-capital/issue-the-quarterly-report-and-statements.md)
- **Answer the Leaders' Questions**
  - `ref/fin/report-the-monthly-results`, activity 14 -
    [Report the Monthly Results](../../../../processes/finance/report-the-monthly-results.md)
  - `ref/hr/report-on-the-workforce`, activity 15 -
    [Report on the Workforce](../../../../processes/human-resources/report-on-the-workforce.md)
- **Answer the Readers' Questions**
  - `ref/sup/report-what-customers-say`, activity 13 -
    [Report What Customers Say](../../../../processes/customer-support/report-what-customers-say.md)
- **Record Each Decision**
  - `ref/sup/report-what-customers-say`, activity 15 -
    [Report What Customers Say](../../../../processes/customer-support/report-what-customers-say.md)
- **Record What the Month Taught**
  - `ref/fin/report-the-monthly-results`, activity 16 -
    [Report the Monthly Results](../../../../processes/finance/report-the-monthly-results.md)
- **Record What the Period Taught**
  - `ref/hr/report-on-the-workforce`, activity 17 -
    [Report on the Workforce](../../../../processes/human-resources/report-on-the-workforce.md)
  - `ref/sup/report-what-customers-say`, activity 16 -
    [Report What Customers Say](../../../../processes/customer-support/report-what-customers-say.md)
- **Record What the Quarter Taught**
  - `ref/pc/issue-the-quarterly-report-and-statements`, activity 17 -
    [Issue the Quarterly Report and Statements](../../../../processes/private-capital/issue-the-quarterly-report-and-statements.md)

## What to record

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
