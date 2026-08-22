# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the invoices and statements for the period | read |  |
| the media plan and the orders placed against it | read | What was ordered, at the version it was ordered at. |
| the agreed rates, fees and discounts | read | At their versions. |
| ad platforms | read | What actually ran, at the figures the platform reports. |
| analytics platforms | read |  |
| the accounting record for the period | read | What has been billed and what has already been paid. |
| the reconciliation record | write | Every line lands with its verdict, the amount at stake, and the answer it got. |

There is deliberately no payment grant. This agent says which lines do
not match and what each one is worth, and the people who hold the money
settle them and pay.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
