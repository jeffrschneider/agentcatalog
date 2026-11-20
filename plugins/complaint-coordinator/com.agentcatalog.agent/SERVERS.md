# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the complaints register | write | Each complaint logged once with its class, the date it arrived and its deadline, the outcome of each point, the dates, any money decided, the route further and whether the customer took it, with no right to decide whether a complaint is formal or to decide a point. |
| the policy library | read | `<your complaints policy>` and the approved acknowledgment, each at its version. |
| the support system | write | The complaint taken in from its case, the acknowledgment sent in the approved words, and the cases, replies and promises behind it read, with no right to send the answer. |
| the phone system | read | The call records behind the complaint. |
| the CRM | read | The account the complaint concerns and the customer's agreement. |
| the billing system | read | The bills and payments a complaint concerns, with no right to change one. |
| the knowledge base | read | The approved content each reply behind the complaint cited. |
| the notification channel | write | Anything legal sent to `<your legal team>` the same day, the complaints lead told of a doubt or of an answer about to miss its deadline, each refund or credit sent to the process that decides it, and each cause sent to whoever owns it. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
