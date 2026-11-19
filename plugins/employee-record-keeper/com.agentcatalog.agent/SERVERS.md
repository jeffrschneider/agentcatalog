# The systems this abstract agent needs

Eleven systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the HR system | write | Each employee record, every change with its effective date and its evidence, the old value kept with its dates, and the retention schedule paused on any record a hold keeps. |
| the restricted records store | write | Files each right to work document where only the named people can see it, and reads only the store's access list and its log of openings. |
| the payroll system | write | The pay, the tax details, the bank account and each change, passed before the cut-off of the period it falls in. |
| the benefits system | write | The eligibility date, the enrollment window and each life event. |
| the access system | write | A new manager, team, location or job, so access follows the job. |
| the time and attendance system | read | Only the records and fields an audit request covers. |
| the applicant tracking system | read | The signed offer each new record is created from. |
| the records request log | write | Each request, the identity check, the decision with the person who made it, what was sent and when. |
| the document store | write | The evidence each change rests on and each answer prepared for a records request. |
| the secure delivery route | write | Sends an approved answer to the contact the confirmed identity names. |
| the notification channel | write | The employee hears what changed, at the old contact as well for a change of contact details, and an access nobody named reaches the privacy lead the day it is found. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
