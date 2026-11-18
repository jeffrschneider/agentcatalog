---
name: measure-a-deal-against-the-fund
description: Shows a proposed deal's share of commitments alone and combined, the capital left after fees, reserves, excused investors and the pipeline, and what the deal does to the fund's diversification, reserves and expected return. Use it when running `ref/pc/check-the-deal-against-the-fund-mandate`.
license: CC-BY-4.0
metadata:
  agent: fund-modeler
  agent-version: "1"
---

# Measure a deal against the fund

## What it does

Shows a proposed deal's share of commitments alone and combined, the
capital left after fees, reserves, excused investors and the pipeline,
and what the deal does to the fund's diversification, reserves and
expected return.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check the Capital Left**
  - `ref/pc/check-the-deal-against-the-fund-mandate`, activity 8 -
    [Check the Deal Against the Fund Mandate](../../../../processes/private-capital/check-the-deal-against-the-fund-mandate.md)
- **Model the Deal's Effect on the Fund**
  - `ref/pc/check-the-deal-against-the-fund-mandate`, activity 9 -
    [Check the Deal Against the Fund Mandate](../../../../processes/private-capital/check-the-deal-against-the-fund-mandate.md)
- **Test the Concentration Limits**
  - `ref/pc/check-the-deal-against-the-fund-mandate`, activity 4 -
    [Check the Deal Against the Fund Mandate](../../../../processes/private-capital/check-the-deal-against-the-fund-mandate.md)

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
