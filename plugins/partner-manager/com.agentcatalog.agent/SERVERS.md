# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the partner record | write | Each partner's contacts, tier, dates and standing land here. |
| the agreement record | read | What each side owes, at the version that was signed. |
| the partner portal | write | Cap: which material each tier may be given, set by the adopting organization. |
| the asset store | read |  |
| the training record | write | Who from the partner was trained, on what, and when they finished. |
| the CRM | read | The deals a partner registered and what became of them. |
| the notification channel | write | A partner hears a change to the terms or to their tier on the day it is decided. |

There is deliberately no grant over the agreement itself. This agent
records what was signed and tracks what each side owes under it, and the
people who sign contracts change the terms.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
