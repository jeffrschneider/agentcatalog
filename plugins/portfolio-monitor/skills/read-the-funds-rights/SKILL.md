---
name: read-the-funds-rights
description: "Reads the executed agreements for what each company owes the fund and what the fund may do: information rights, loan reporting terms, consent rights, director rights, preferences and the reserve left. Use it when running `ref/pc/collect-the-portfolio-company-reports` and 3 other reference processes."
license: CC-BY-4.0
metadata:
  agent: portfolio-monitor
  agent-version: "1"
---

# Read the funds rights

## What it does

Reads the executed agreements for what each company owes the fund and
what the fund may do: information rights, loan reporting terms, consent
rights, director rights, preferences and the reserve left.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Check the Fund's Consent Rights**
  - `ref/pc/prepare-and-hold-a-board-meeting`, activity 7 -
    [Prepare and Hold a Board Meeting](../../../../processes/private-capital/prepare-and-hold-a-board-meeting.md)
- **List the Fund's Rights and Duties**
  - `ref/pc/hand-over-to-the-portfolio-team`, activity 5 -
    [Hand Over to the Portfolio Team](../../../../processes/private-capital/hand-over-to-the-portfolio-team.md)
- **Read What Each Company Owes**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 2 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Read the Fund's Rights and Limits**
  - `ref/pc/work-a-company-in-trouble`, activity 5 -
    [Work a Company in Trouble](../../../../processes/private-capital/work-a-company-in-trouble.md)

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
