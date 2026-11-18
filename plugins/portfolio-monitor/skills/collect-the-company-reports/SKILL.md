---
name: collect-the-company-reports
description: Sets up and runs each company's reporting on one template. Use it when running `ref/pc/collect-the-portfolio-company-reports`, `ref/pc/hand-over-to-the-portfolio-team` and `ref/pc/prepare-and-hold-a-board-meeting`.
license: CC-BY-4.0
metadata:
  agent: portfolio-monitor
  agent-version: "1"
---

# Collect the company reports

## What it does

Sets up and runs each company's reporting on one template. It agrees the
template, sends it with its due date, takes in packages and board packs
as they were sent, chases a late one once and then with the deal lead,
checks each is complete, and records what arrived late or wrong.

## Where it happens

The agent does this in eleven activities across three reference
processes. Each one names the activity as that process words it.

- **Agree the Reporting Template**
  - `ref/pc/hand-over-to-the-portfolio-team`, activity 10 -
    [Hand Over to the Portfolio Team](../../../../processes/private-capital/hand-over-to-the-portfolio-team.md)
- **Chase a Late Report**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 5 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Check the Package Is Complete**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 6 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Collect the Board Pack**
  - `ref/pc/prepare-and-hold-a-board-meeting`, activity 2 -
    [Prepare and Hold a Board Meeting](../../../../processes/private-capital/prepare-and-hold-a-board-meeting.md)
- **Confirm the First Report Arrived**
  - `ref/pc/hand-over-to-the-portfolio-team`, activity 13 -
    [Hand Over to the Portfolio Team](../../../../processes/private-capital/hand-over-to-the-portfolio-team.md)
- **Open the Reporting Period**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 1 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Record What Arrived Late or Wrong**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 17 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Send the Template and the Due Date**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 3 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Set Up the First Month's Reporting**
  - `ref/pc/hand-over-to-the-portfolio-team`, activity 11 -
    [Hand Over to the Portfolio Team](../../../../processes/private-capital/hand-over-to-the-portfolio-team.md)
- **Take in What Each Company Sends**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 4 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Take in the Meeting and the Agenda**
  - `ref/pc/prepare-and-hold-a-board-meeting`, activity 1 -
    [Prepare and Hold a Board Meeting](../../../../processes/private-capital/prepare-and-hold-a-board-meeting.md)

## What to record

Each reporting period leaves the companies that owed reports and the
date each package was due, every package as the company sent it with its
date and its sender, the reminder and the escalation for every late one,
and the completeness check naming each gap with its explanation. Each
company gets a one-page summary with every figure traced to the template
line it came from and every untied figure marked untied, with the deal
lead's confirmation or written correction beside it. Every warning is
recorded with the numbers behind it, the date the breach or the
shortfall would land, and the hour it was raised beside the hour it was
found. The handover to the valuation names every company that did not
report. A handover run leaves the fund's rights and duties read from the
executed agreements, the template as agreed with the company, and the
date the first report arrived. Each board meeting leaves the date the
pack arrived, the numbers against the budget, the prior period and the
covenants, the decisions the board was asked for with each consent the
fund owes and its due date, and every difference between the minutes and
the record sent to the company secretary. A company in trouble leaves
the confirmed facts or the reporting error named, a runway built week by
week with the covenant headroom at each test date, a weekly reading
until it is cleared, and the date and the reason it came off the list.
The portfolio review leaves each company's condition and its place on
the scale, with the reason for any change of level.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
