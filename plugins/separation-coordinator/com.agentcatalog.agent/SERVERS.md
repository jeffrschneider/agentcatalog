# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the HR system | write | The departure, the last day and the leaving record, with the reason for leaving held where only HR can see it. |
| the employee relations case system | write | The record behind a dismissal, the conversation as both people who held it confirmed it, and the letters, in the restricted case. |
| the asset register | write | Each device, card, key and document checked in, or recorded as missing. |
| the document store | write | The letters, the notices, the final documents and the separation terms at their versions. |
| the signature system | trigger | Sends a letter, a notice or the final documents to the named person who signs them, with no right to sign. |
| the payroll system | read | The final pay date and what the leaver is owed anyway, which stays outside any trade. |
| the workforce planning system | read | The roles affected, the pool and the written criteria in a layoff. |
| the notification channel | write | Each team hears its items and the last day, and a moved last day reaches payroll, benefits and IT the same day. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
