# The systems this abstract agent needs

Eleven systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the support system | write | Each suspected outage with its grouped cases, each case joined to an incident or sent back to its queue, the customer side of each incident, the approved wording sent to each open linked case, and each follow-up, with no right to send words a named person has not approved. |
| the status page | write | Exactly the approved version of each update, correction, resolved update and summary, posted with the time it went up and the time of the next, and the planned maintenance read from it, with no right to post a version no named person approved. |
| the incident record | read | Each incident engineering has open, its severity, the facts the incident lead confirmed and engineering's review. |
| the issue tracker | read | The known bugs and the releases of the last `<hours>` a symptom may match. |
| the CRM | read | The accounts behind the grouped cases, their plans and their owners. |
| the coverage record | read | The public posts about a symptom, read and recorded and never answered. |
| the statement record at `ref/mkt/crisis-communication` | read | Marketing's statement each update is set beside. |
| the policy library | read | `<your incident policy>` with the cadence and the approver for each severity, `<your threshold>` and `<your reply rules>` at their versions. |
| the paging system | write | The engineer on call paged under `<your on-call rota>` with the evidence, and the next person on the rota when nobody answers. |
| the outbound mail system | write | Exactly the approved summary sent to the contacts on every affected account. |
| the notification channel | write | The head of support told the same minute as each page, each account owner sent the list of their affected accounts, the approved wording passed to the support specialists, and each account missing from engineering's list named to the incident lead. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
