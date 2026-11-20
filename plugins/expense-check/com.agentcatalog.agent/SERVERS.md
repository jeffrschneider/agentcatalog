# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the expense tool | write | Each line's result against the policy, any part treated as pay, and each question to the employee, with no right to approve, refuse or pay a line. |
| the HR system | read | The manager named to approve each employee's claims and each holder's transactions. |
| the card register | read | Each card's merchant rules, which each transaction is read against. |
| the notification channel | write | The employee is asked for a missing receipt or reason, and a manager who has not decided is reminded. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
