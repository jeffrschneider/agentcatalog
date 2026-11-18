# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the answer library | read | Every answer is read from it at a version, and none is written from memory. |
| the evidence store | read | The reports, certificates and policies the answers point at, each at the version the answer names. |
| the CRM | read | The opportunity or investor record the form is attached to and the confidentiality agreement that covers it. |
| the requester's portal | write | The form filed the way the requester asked. |
| the document store | write | The response as sent, its date and its receipt. |
| the answer library | write | Each signed new answer to an investor's questionnaire is added at a version, with its owner, its source and the date it must be read again. |
| the data room | read | The frozen track record and the fund documents the investor's answers rest on, each at its version. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
