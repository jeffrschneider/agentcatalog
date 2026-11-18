# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the deal pipeline | write | Each memo version sits on the deal's record, and a pass or a decline is recorded there with its reason for the next deal team to read. |
| the request log | read | Which diligence requests are still open and what each answer said. |
| the data room | read | The material each finding rests on. |
| the financial model | read | The issued model at its version, so the memo carries no number the model does not. |
| the committee portal | write | The signed memo at its version, with the model and the mandate result, sent before the reading deadline. |
| the signature system | trigger | The memo routed to the deal lead partner for the signature this agent never gives. |
| the decision record | read | The committee's questions, its decision, its conditions and the reason for a decline. |
| the portfolio reporting system | read | What happened to a failed holding, which its memo is read against. |
| the lessons library | write | The lessons of a write-off, filed where the next memo's author will read them. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
