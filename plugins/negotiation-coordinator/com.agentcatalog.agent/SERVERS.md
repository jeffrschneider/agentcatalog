# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | write | The offer as sent, the buyer's reply, and the notes from the calls since. |
| the quoting system | write | The offer rebuilt from what was agreed, with every changed line traced to the ask that changed it. |
| the contract system | read | The paper the agreed terms are read against. |
| the approval system | read | Which concession is signed, by whom, and on what date. |
| the pricing model | read | What each ask costs and what it does to margin, within a discount cap the adopting process sets. |
| the shared workspace with the buyer | write | The list both sides confirm, and the refusals in writing. |
| the fund model | read | What an investor's ask costs in fees and carried interest, read at the size it would reach if every investor with a most favored nation right elected it. |
| the deal pipeline | write | Each bid in a sale, logged with its price, how it will be paid for, its conditions and its date, and the comparison of the final bids. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
