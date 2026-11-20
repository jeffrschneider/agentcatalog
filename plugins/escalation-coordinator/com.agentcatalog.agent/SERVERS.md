# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the support system | write | Each escalation summary, the tier and the specialist chosen, each outcome handed back, each security or safety report kept out of the shared queues and opened only to the named people who must see it with every opening logged, and each later report joined, with no right to send a reply to a customer. |
| the issue tracker | write | Each bug filed with the steps, the masked evidence, the accounts affected and the severity proposed, each case and account joined to a bug already filed, each status answer recorded, and each fix taken in, with no right to confirm a bug, set its severity or close it. |
| the CRM | read | The account's entitlement, which sets the tier, and the customers and cases linked to a bug. |
| the policy library | read | `<your escalation tiers>`, `<your bug severity rules>`, `<your data handling policy>` and `<your security policy>` at their versions. |
| the security reporting channel | write | Each report sent to `<your security team>` or the named safety owner in the reporter's own words, with the case and the evidence. |
| the restricted record | write | Who knew what and when about each security or safety report, each answer from the security team, and each reply as sent with who approved it, kept as `<your jurisdiction's rule on keeping security records>` requires. |
| the paging channel | write | The person on call paged outside working hours, and the next named person under `<your security policy>` when nobody confirms within the hour. |
| the notification channel | write | The first specialist told what solved the case, the privacy lead and `<your legal team>` told the same hour of a possible exposure of personal data, the owner of a public place asked to take a report out of public view, and the head of support told when nobody confirms a report in time. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
