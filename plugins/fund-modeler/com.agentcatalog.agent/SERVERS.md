# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the fund model | write | The construction, the reserves, the economics and the returns live here at versions, and this agent is the only thing that writes them. |
| the fund accounting system | read | Commitments, uncalled capital, fees charged, and what the last fund called, invested and returned. |
| the portfolio reporting system | read | What the last fund's companies actually did, and the condition of each company the fund holds now. |
| the deal pipeline | read | The deals ahead in the pipeline that draw on the same capital as the one being checked. |
| the customer relationship management system, or CRM | read | The commitment sizes existing and target investors have stated, which the fund size is read against. |
| the partnership decision record | read | The mandate, the size and the reserves as the partners decided them, which the model is set to. |
| the document store | write | The strategy and the model frozen side by side at one version. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
