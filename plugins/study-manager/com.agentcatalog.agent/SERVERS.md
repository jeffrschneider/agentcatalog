# The systems this abstract agent needs

Ten systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the study record | write | Each study lands at a version with its question, its method, who is sampled and how the sample is drawn. |
| the questions and the material shown | write | Held at a version before anybody sees them, and a change made after the study is in the field lands as a new version. |
| the survey and interview system | trigger | A study opens on its date and closes when the sample is complete. |
| the response record | write | Every response lands as it was given, with its date. |
| the earlier studies in the series | read | At the versions they ran under, so a question that changed between two runs is visible. |
| the contact database | read |  |
| the consent record | read |  |
| the customer and revenue record | read | The accounts, what they bought, what they renewed, when they left, and the deals a win-loss study reads back over. |
| analytics platforms | read |  |
| the meeting calendar | write | Cap: which interviews and sessions it may set without asking, set by the adopting organization. |

There is deliberately no grant to send. This agent says who has to be
sampled, the consent-manager agent says which of those contacts may be
reached at all, and the audience-operator agent sends the invitation.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
