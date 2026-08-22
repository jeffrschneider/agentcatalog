# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the strategy record | write | The reason the run started and the thesis it ended with live here, at versions. |
| company data sources | read | What each candidate sells, to whom, and at what size. |
| the CRM | read | Where a candidate already touches our customers. |
| the contract system | read | A customer contract can forbid working with a candidate, and that has to be found before contact. |
| the confidentiality register | write | What was signed with whom, and on what date. |
| the partner record | write |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
