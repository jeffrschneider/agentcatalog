# The systems this abstract agent needs

Twelve systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| analytics platforms | read |  |
| ad platforms | read |  |
| the CRM | read |  |
| the plans and commitments for the period | read | What each run said it would do. |
| the fund's books | read | The approved marks, the performance figures and each investor's capital account, when the report goes to a fund's investors. |
| the portfolio reporting system | read | Each company's quarter as the portfolio review read it, for the letter to the fund's investors. |
| the notification channel | write | The investors hear before the date passes when a late report will arrive. |
| the report store | write | Each period's report lands at a version. |
| the general ledger | read | The month's results as the close signed them off, which every figure in the monthly results report ties to. |
| the budget record | read | The budget and the latest approved forecast at their versions, and what each budget owner has committed, spent and has left. |
| the financial planning system | read | Each line compared with the plan and each difference above the threshold, as the planning-analyst agent marked it. |
| the reporting tool | write | The monthly results report at a version, delivered to each leader on its date. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
