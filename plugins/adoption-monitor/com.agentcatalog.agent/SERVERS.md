# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the process register | read | The process at the version being measured, with the steps it calls gates. |
| the logging system | read | The fields, timestamps and log lines that already carry the behavior. |
| the reporting tool | write | The report, naming the process and the version it measures. |
| the systems being watched | write | The fields and events that make a departure visible, built only after the change is signed, each with a way to turn it off without a deployment. |
| the alert path | trigger | A departure past its threshold reaches the person the thresholds name. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
