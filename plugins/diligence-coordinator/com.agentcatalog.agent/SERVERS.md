# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the request log | write | Every request and every answer, dated, and an answer given only in a meeting is written in before it counts. |
| the document room | write | Material received under confidentiality, readable only by the people the access agreement names. |
| the partner record | write | The candidate's file and the diligence result land here. |
| company registry sources | read | Registration, ownership and filings. |
| the screening service | read | Sanctions, ownership and conduct. |
| the contract system | read | What our own agreements already commit us to. |
| the deal pipeline | write | The opportunity's record, where the rated findings and the report to the deal lead land. |
| the financial model | read | The issued model at its version, which the memo's findings and risks are tied to. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
