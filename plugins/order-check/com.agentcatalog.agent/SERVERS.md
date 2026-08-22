# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the contract repository | read | Every booking field names the clause it was read from. |
| the price book | read | Each line priced at a named version, or naming the approval that let it differ. |
| the product catalog | read | Every sold line matched to something that exists. |
| delivery capacity records | read | Whether the date the customer expects can be met. |
| the order system | write | The booking, at the version an approver signed and no other. |
| the CRM | write | The opportunity closed at the booked amount. |
| the billing system | write | The billing schedule, the payment terms and the purchase order reference. |
| the forecast | write | Corrected to what was actually booked rather than to what was forecast. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
