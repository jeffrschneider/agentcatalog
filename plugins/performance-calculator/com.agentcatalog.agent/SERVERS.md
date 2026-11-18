# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the fund accounting system | read | Every deal's dated cash flows, the fees and carried interest charged, and the approved marks as posted. |
| the portfolio reporting system | read | Each company's earnings and debt, which a buyout gain is split by. |
| the valuation files | read | The approved marks at the record date, with the method behind each one. |
| the document store | write | The method, the frozen set and the workpapers, kept for the retention period the rules set. |
| the report store | write | The quarter's fund figures at a version, for the letter and the statements. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
