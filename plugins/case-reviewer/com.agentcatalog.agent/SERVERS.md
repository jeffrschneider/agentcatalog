# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the support system | read | The cases closed in each period by team, channel and topic, with the history and the replies of each case drawn. |
| the phone system | read | The call recordings of the cases drawn, kept under `<your jurisdiction's rule on recording calls>`. |
| the knowledge base | read | The approved content each reply in a drawn case cited. |
| the policy library | read | `<your quality rubric>` at the version in force, and `<your reply rules>` and `<your identity policy>` at their versions, read to find a reply sent without the approval it needed or a skipped identity check. |
| the survey tool | read | The low survey scores that point to the cases picked for a reason. |
| the review record | write | Each sample with its population and its draw, each score with its moment and the rubric version, each uncertain mark, each specialist's results and reviewed cases in the record only the specialist and their team lead can open, and each split and each agreed reading, with no right to show a specialist's results to anyone else. |
| the notification channel | write | A case that cannot wait sent to the quality lead the same day, each desk fault sent to its owner, each specialist's results sent to that specialist and their team lead, a questioned score sent for a second reading, and each reviewer sent their own scores. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
