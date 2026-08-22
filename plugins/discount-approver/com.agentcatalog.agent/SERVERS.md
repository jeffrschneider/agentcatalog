# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the quoting system | read | The lines the ask covers, at the quote version it is asked against. |
| the CRM | read | The deal, the customer, and what they already have. |
| the rate card store | read | Every line re-priced at a named card version, never against a previous quote. |
| the cost model | read | The floor the discounted deal is set against. |
| the approval record | write | The decision, the reason, the signer, the band and the quote version. |
| the discount log | write | What was asked, what was given, and how long the answer took. |
| the notification channel | write | The seller hears the clock, the answer, and anything that went up the line. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
