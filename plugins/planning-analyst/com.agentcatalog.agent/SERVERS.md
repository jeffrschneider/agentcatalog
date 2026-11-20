# The systems this abstract agent needs

Ten systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the financial planning system | write | The drafts, the combined budget, the options, each reforecast, each case and each covenant projection at their versions, with no right to approve a budget, a reforecast or a case. |
| the general ledger | read | Each closed month's results, the trial balance and the entries behind each difference. |
| the budget record | read | The issued budget and the latest approved forecast at their versions, and what each owner has committed and spent. |
| the workforce plan | read | Each team's headcount, start dates and labor cost at the version approved. |
| the published revenue forecast | read | The forecast view and the number sales leadership committed, each at its version. |
| the decision record | read | The trade-offs the executive team settled and each approved investment case the plan carries. |
| the treasury system | read | The published cash forecast the covenant projections start from. |
| the facility record | read | Each covenant's definitions and test dates, for the projection. |
| the document store | write | Each case on the template, and what each budget, reforecast and case rests on. |
| the notification channel | write | The instructions reach each department head, a draft with a gap goes back to its owner, and each owner is asked about the changes already known. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
