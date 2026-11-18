# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the side letter register | write | Every signed letter, each clause as an obligation with its owner, its trigger and its due date, and every election made; this agent keeps it. |
| the document store | write | Side letter drafts at their versions, beside counsel's text. |
| the investor portal | write | After the final close, each investor with an MFN right is sent the terms it may elect, and its elections come back here. |
| the fund accounting system | read | The calls, fees, offsets and expenses it checks against the letters, booked by the capital-account-keeper agent. |
| the portfolio reporting system | read | The fees portfolio companies paid the firm, which the offsets are worked from. |
| the notification channel | write | An obligation coming due reaches its owner ahead of the date. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
