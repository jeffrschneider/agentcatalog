# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the requirements and scoring criteria for the selection | read | At the version they were fixed at, before any candidate was seen. |
| the candidate material | read | The proposals, the answers, the demonstrations and the reference calls, as they were submitted. |
| a trial environment | read | A candidate system as it behaves under test, where the process arranges one. |
| the security and privacy standards the organization has adopted | read | At their versions. |
| the supplier record | read | What the department already buys and runs, so an overlap with something already held is scored rather than missed. |
| the scoring record | write | Every verdict lands with the requirement it cites and the evidence behind it. |
| the screening service | read | Sanctions, money laundering and adverse records for investors and their owners, target companies and their leaders, and the firm's own people and providers. |
| company registry sources | read | A company's registration, good standing and owners. |
| court and regulator records | read | Suits, threats, regulator letters and settlements. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
