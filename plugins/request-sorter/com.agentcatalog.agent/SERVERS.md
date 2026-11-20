# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the support system | write | Each request as it arrived, its match or its mark as unmatched, the case it opened or joined, its urgency and topic with the rule behind each, its service level and its clock, its marks for a person or an identity check, its queue, each case held overnight and each case joined to a suspected outage, with no right to send a reply to a customer or to change a routing rule. |
| the chat tool | read | Each chat as it arrived. |
| the phone system | read | Each call's notes, and any recording kept under `<your jurisdiction's rule on recording a call>`. |
| the CRM | read | The details on file each sender is matched against, with no right to change a field. |
| the policy library | read | `<your routing rules>`, `<your service level policy>`, `<your reply rules>`, `<your identity policy>`, `<your list of what cannot wait>` and `<your after-hours rules>` at the versions each request is read and sorted under. |
| the scheduling system | read | The after-hours rota for the period, with the person on call and the next person on it. |
| a copy of `<your support system>` away from live | write | Past requests sorted under a proposed routing change, with no right to change the live system. |
| the notification channel | write | Each request that cannot wait sent to its owner, each page to the person on call and the next person on the rota, and each surge on one symptom sent to the outage-coordinator agent. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
