# The systems this abstract agent needs

Eleven systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the creator record | write | Every creator, their audience figures, their history and the terms they hold. |
| the deal record | write | What was agreed with each creator, at the version it was agreed. |
| the contact log | write | Every exchange with a creator lands here on the day it happened. |
| the outreach channel | write | Cap: how many creators it may approach without asking, set by the adopting organization. |
| audience measurement sources | read | The figures behind a creator's reach, and the checks on whether that reach is real. |
| the published work record | read | What each creator posted and what the checking agents found in it. |
| the audience definitions | read | The audience the campaign is trying to reach. |
| the claims register | read |  |
| brand guidelines | read |  |
| the disclosure rule record | read | What a paid partnership has to say in each market the work will run in. |
| the asset store | read | The material a creator is given, at the versions that were signed. |

There is deliberately no payment grant. This agent records the fee that
was agreed and the date it falls due, and a person releases the money.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
