# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the data dictionary | write | Every definition lands at a version, dated, with the person who signed it, and the version it replaces stays readable at its own number. |
| the CRM | write | Required fields, allowed values, and the corrections to records already wrong. |
| the reporting layer | read | What counts off the object, so a change is read against the reports before it is signed. |
| the integrations | read | Which systems the object is copied into. |
| the consent record | read | What may be held, field by field, and for how long. |
| the import tooling | read | What an import writes, when the trail leads there. |
| the standards store | read | The measure definitions in force, so a record definition does not contradict one. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
