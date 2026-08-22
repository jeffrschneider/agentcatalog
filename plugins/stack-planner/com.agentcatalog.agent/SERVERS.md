# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the stack record | write | Every entry lands with the process it serves, its owner, its cost, its term and its renewal date. |
| the requirements record | write | The requirements and the criteria at the version they were fixed at, dated before any candidate was seen. |
| the scoring record | read | The verdicts the scoring agent returned, read rather than edited. |
| the decision record | write | Who chose, on what date, for what reasons, and anyone who disagreed. |
| the process register | read | Whether a process exists that would run inside the tool at all. |
| a trial environment | read | The finalists doing the team's real work over the same period, measured once. |
| the budget record | read | What the stack already costs, so a new entry is read against it. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
