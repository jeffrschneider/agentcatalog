# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the scheduling system | write | Each draft schedule and rota at its version, the schedule published once approved, each approved swap and each move a team lead decided, and the hours the team has in each interval, with no right to approve a schedule or a swap. |
| the HR system | read | The leave approved under `<your leave policy>` and each leave of absence, read as dates with no reason attached, with no right to approve, refuse or change anyone's leave. |
| the policy library | read | `<your working time policy>`, `<your service level policy>` and `<your support hours>`, each at its version. |
| the timekeeping system | write | The planned hours of each published schedule and each swap, and the hours of cover called in, for pay. |
| the support system | read | The requests by channel and interval behind the people needed, the day's queues, and the queue held after hours. |
| the phone system | read | The people working the phone channel and the calls arriving by interval. |
| the chat tool | read | The people working the chat channel and the chats arriving by interval. |
| the notification channel | write | Each person sent their own shifts and on-call hours, both people told of a swap, each person moved told, the person on call and the one behind them asked to confirm, each shortfall sent to the team lead, and each forecast sent to the support operations lead and the team leads. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
