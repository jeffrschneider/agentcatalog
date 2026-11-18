---
name: set-the-reserves-in-the-fund-model
description: Proposes each company's reserve from the deal lead's ask, models the fund at each reserve level, checks the reserves against uncalled capital, recycling and the fund's terms, and writes the reserves the partners agree into the fund model at a new version. Use it when running `ref/pc/run-the-portfolio-review`.
license: CC-BY-4.0
metadata:
  agent: fund-modeler
  agent-version: "1"
---

# Set the reserves in the fund model

## What it does

Proposes each company's reserve from the deal lead's ask, models the
fund at each reserve level, checks the reserves against uncalled
capital, recycling and the fund's terms, and writes the reserves the
partners agree into the fund model at a new version.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Check the Fund Can Carry the Reserves**
  - `ref/pc/run-the-portfolio-review`, activity 7 -
    [Run the Portfolio Review](../../../../processes/private-capital/run-the-portfolio-review.md)
- **Model the Fund with the Reserves**
  - `ref/pc/run-the-portfolio-review`, activity 6 -
    [Run the Portfolio Review](../../../../processes/private-capital/run-the-portfolio-review.md)
- **Propose Each Company's Reserve**
  - `ref/pc/run-the-portfolio-review`, activity 5 -
    [Run the Portfolio Review](../../../../processes/private-capital/run-the-portfolio-review.md)
- **Set the Reserves**
  - `ref/pc/run-the-portfolio-review`, activity 11 -
    [Run the Portfolio Review](../../../../processes/private-capital/run-the-portfolio-review.md)
- **Update the Fund Model**
  - `ref/pc/run-the-portfolio-review`, activity 16 -
    [Run the Portfolio Review](../../../../processes/private-capital/run-the-portfolio-review.md)

## What to record

For a strategy run: the successor clause and the share of the last fund
invested or reserved against its threshold, as the chief compliance
officer read it; the last fund's plan set beside what it did, with the
reason for each gap; every version of the model tried, with what changed
and why each was set aside; the construction as deal count, deal size,
ownership or control and pacing; the reserve share and the last fund's
reserve use it was set from; the target size and the hard cap; the fee
and its step-down, the carry, the hurdle, the catch-up and the offsets,
each priced; the net return in the base, low and high cases with the
deal outcomes each case assumes; the options put to the partners; and
the model frozen at the strategy's version. For a mandate check: the
deal's share of commitments alone and combined, the capital left after
fees, reserves, excused investors' shares and the pipeline, naming the
deals counted, and what the deal does to diversification, reserves and
the expected return, against the fund model at its version. For a
portfolio review: each proposed reserve with the deal lead's ask, the
fund modeled at each reserve level, the capacity check against uncalled
capital, recycling, the limit per company and the investment period, and
the model version that replaced last quarter's. An auditor can rebuild
any reserve or any capital-left figure from the model version and the
inputs it names.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
