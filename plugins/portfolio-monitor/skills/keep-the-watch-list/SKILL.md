---
name: keep-the-watch-list
description: Raises a warning the day it is found, ranks every company on the watch list scale, hands a company that needs it to its own process, watches a company in trouble every week until it comes off the list, and records what warned first and how early. Use it when running `ref/pc/collect-the-portfolio-company-reports` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: portfolio-monitor
  agent-version: "1"
---

# Keep the watch list

## What it does

Raises a warning the day it is found, ranks every company on the watch
list scale, hands a company that needs it to its own process, watches a
company in trouble every week until it comes off the list, and records
what warned first and how early.

## Where it happens

The agent does this in nine activities across four reference processes.
Each one names the activity as that process words it.

- **Hand On the Watch List and Reserves**
  - `ref/pc/run-the-portfolio-review`, activity 17 -
    [Run the Portfolio Review](../../../../processes/private-capital/run-the-portfolio-review.md)
- **Raise a Warning the Same Day**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 13 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Raise the Warning**
  - `ref/pc/work-a-company-in-trouble`, activity 1 -
    [Work a Company in Trouble](../../../../processes/private-capital/work-a-company-in-trouble.md)
- **Rank the Companies by Risk**
  - `ref/pc/run-the-portfolio-review`, activity 3 -
    [Run the Portfolio Review](../../../../processes/private-capital/run-the-portfolio-review.md)
- **Record What Was Learned**
  - `ref/pc/work-a-company-in-trouble`, activity 18 -
    [Work a Company in Trouble](../../../../processes/private-capital/work-a-company-in-trouble.md)
- **Start the Work a Company Needs**
  - `ref/pc/run-the-portfolio-review`, activity 14 -
    [Run the Portfolio Review](../../../../processes/private-capital/run-the-portfolio-review.md)
- **Take the Company off the Watch List**
  - `ref/pc/work-a-company-in-trouble`, activity 17 -
    [Work a Company in Trouble](../../../../processes/private-capital/work-a-company-in-trouble.md)
- **Update the Plan and the Watch List**
  - `ref/pc/prepare-and-hold-a-board-meeting`, activity 16 -
    [Prepare and Hold a Board Meeting](../../../../processes/private-capital/prepare-and-hold-a-board-meeting.md)
- **Watch the Company Every Week**
  - `ref/pc/work-a-company-in-trouble`, activity 16 -
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
