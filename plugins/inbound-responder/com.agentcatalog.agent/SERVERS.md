# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the inbox and the form store | read | The inquiry arrives there. |
| the CRM | write | The reply, the times offered and the notes go on the record. |
| the sending system | write | The reply goes out on the channel the inquiry came in on. |
| the calendar | write | A time to talk is proposed and held. |
| the consent record and the do-not-contact list | read | To check the reply may be sent at all. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
