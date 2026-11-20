# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the delegation register | write | Each draft with every change marked, each version with its effective date, and the old versions with the dates they applied, with no right to approve a version or an item. |
| the board records | read | The decision behind each change and the people the board names. |
| the HR system | read | Each role, the person who holds it, and the last day of an approver who is leaving or the dates one is away. |
| the ERP | read | The approval limits and routes each system reads from the delegation. |
| the approval records of each process | read | Each approval asked for and given since the version in force was published, with who gave it. |
| the policy library | read | Each finance policy's text with the amounts, limits and approvers it names. |
| the notification channel | write | Each request for approval is answered with the approvers it needs, an approval that does not count reaches the controller, and each change reaches the owner of the process that carries it out. |
| the refund register | read | Each refund or goodwill credit proposed, who asked for, proposed or recommended it, and who decided it. |
| the support system | read | Who on the case asked for, proposed or recommended a refund or a credit, so none of them decides it. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
