# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the HR help channel | write | Each question and its answer, the acknowledgment of a records request, and the note telling an employee who has their question. |
| the HR system | read | Only the location, the type of employment and the benefit plan that decide which answer applies, and nothing from the health, investigation or background check records. |
| the policy library | read | The policy text an answer cites, at the version in force for the employee's location. |
| the answer library | read | The approved answers, each beside the policy version it rests on. |
| the routing list | read | The named person for each sensitive subject. |
| the notification channel | write | A personal or sensitive question reaches its named person within the hours the company sets, and a question that suggests someone is in danger reaches one at once. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
