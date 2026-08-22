# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the press and analyst contact record | write | Who covers the subject, and what each of them has published. |
| the contact log | write | Every exchange lands here on the day it happened. |
| the approved press material | read | At the versions the signers approved. |
| the claims register | read |  |
| the outbound mail system | write | Cap: which contacts it may send to without asking, set by the adopting organization. |
| the briefing calendar | write | Briefings are booked and their attendees held here. |
| the coverage record | read |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
