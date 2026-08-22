# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the system that delivers the work | read | The start and stop stamps. |
| the CRM | read | The run, its queue and its owner. |
| the inbox and the form store | read | When the work first arrived. |
| the reporting store | write | The measurements, the queries behind them, and the period as published. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
