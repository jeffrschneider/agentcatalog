# The systems this abstract agent needs

Thirteen systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the identity system | write | Accounts and licences ordered before day one, at the job's list rather than a copy of somebody else's. |
| the learning system | write | The plan at a version, and who has completed what. |
| the enablement library | write | One address holds the material a joiner is taught from, so the roll-out and the curriculum never differ. |
| the territory record | read | The patch and the ramped number, at the version the territory process signed. |
| the call recording system | read | The calls the joiner listens to, with the date of each one. |
| the calendar | write | Sessions, the sitting and the first customer conversation in diaries on both sides. |
| the CRM | read | The accounts the joiner has been given, so teaching is against the real patch. |
| analytics | read | Where the joiner stands against the ramp plan. |
| the applicant tracking system | read | The signed acceptance a new hire's preparation starts from, with the job, the manager, the location, the pay, the start date and any condition still open. |
| the HR system | write | The welcome and the forms sent to the new hire's own sign-in, and each completed form filed to the employee record, with no right to fill in a field on the new hire's behalf. It reads each new hire's job, manager, location, language, start date and probation period, and nothing from their forms, to set an orientation group and draft the plan for the first months. |
| the IT service desk | write | The accounts on the job's access list, with the approver of any account beyond it, and the laptop, the phone, the badge, the desk or the home delivery the job needs, each ordered with the date it must arrive. |
| the survey tool | write | The private questions to each new hire about how the start went, read by the HR business partner, and the feedback on each orientation session, read only for the group as a whole. |
| the notification channel | write | The new hire told where to go on the first day, when, and who will meet them, and the manager told when a check-in is booked again. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
