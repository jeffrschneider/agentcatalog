# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | read | The account, what it already owns, and the deal the ask belongs to. |
| the quoting system | read | The configuration, the price and the term as the deal stands. |
| the deal desk queue | write | The request, its level, its promised time and its state. |
| the approval record | write | The decision, the reason, the signer and the deal version it was decided against. |
| the contract record | read | The paper the deal sits on. |
| the standard terms store | read | The terms in force each item is tested against. |
| the notification channel | write | The seller hears the clock, the answer, and anything that went up the line. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
