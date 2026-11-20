# The systems this abstract agent needs

Ten systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the certification record | write | The result, the standard version, the assessors, the evidence and the expiry date. |
| the learning system | write | Who sat what, and who is due to sit again. |
| the enablement library | read | The material people were taught from, so the sitting tests what was covered. |
| the CRM | write | On a practice recor, the systems check is done on a practice record and never on a live customer. |
| the quoting system | write | On a practice recor, the same, for the quote the person builds unaided. |
| the partner portal | write | Certificates issued with a date and an expiry, and the certified list visible to both sides. |
| analytics | read | What the people who passed went on to do. |
| the support system | write | On a practice case in the practice area only, so a support specialist's sitting never touches a live customer's case. |
| the knowledge base | read | The articles a support specialist may use during a sitting, set out beforehand. |
| the HR system | read | Who manages and who mentors the person sitting, so no assessor scores their own people. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
