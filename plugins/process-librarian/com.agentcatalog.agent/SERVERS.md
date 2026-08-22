# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the document store | write | The process at a version, at a fixed address, with every document it replaces marked as replaced. |
| the process register | write | Which version is current, and which processes people are expected to follow. |
| the wiki and the existing descriptions | read | The pages, decks, checklists and mail threads that already describe the work, each carrying its date. |
| the CRM | read | The accounts of the work read against what the record shows. |
| the system trail | read | What the systems recorded for the recent runs, so a step nobody records is written as a step with no trail. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
