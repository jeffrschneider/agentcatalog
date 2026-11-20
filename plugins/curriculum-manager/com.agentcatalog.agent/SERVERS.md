# The systems this abstract agent needs

Twelve systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the learning system | write | The plan, the courses, and who completed what. |
| the enablement library | write | The material at a version, at one address people can reach. |
| the calendar | write | Sessions, trainers and rooms in diaries on both sides. |
| the lab environment | trigger | Each person builds the thing themselves, once, with a cap on hours per person. |
| the certification record | read | What somebody already holds, so teaching starts from what they can be excused. |
| the price book and the competitor set | read | So what is taught is what is currently in force. |
| the course library | write | Each course in the company's learning program, each required course and the orientation material, published at a version at one address people can reach. |
| the workforce plan | read | The skills the approved plan says the company will need in the year and does not yet have. |
| the policy library | read | Every policy now in force at its version, which the orientation material and each required course are read against. |
| the knowledge base | read | The approved content a support specialist is taught from, at its version. |
| the support system | read | The cases on a feature so far, and the queues, routing, service levels and saved replies a new support specialist is taught. |
| the release calendar | read | What each release changes and the date it reaches customers, so the support specialists are briefed before it does. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
