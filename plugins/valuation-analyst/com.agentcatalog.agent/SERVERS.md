# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the valuation files | write | One file per holding at the version the committee approved, and this agent keeps them. |
| the portfolio reporting system | read | The confirmed reports and summaries, and the companies that did not report. |
| the cap table record | read | The fund's shares by class and the rights each class carries. |
| market data sources | read | Rounds, offers, sales and the multiples of comparable listed companies, each with its date. |
| the fund accounting system | read | Last quarter's approved marks and the fund's cost in each company. |
| the audit request portal | write | The support for each mark the auditor tests, answered in the auditor's own log. |
| the notification channel | write | The committee pack and the clock reach the people who review and approve the marks. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
