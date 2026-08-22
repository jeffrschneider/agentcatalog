# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the session proposal store | write | Every proposal lands with the verdict it was given and the criterion behind it. |
| the agenda and its schedule | write | The running order lands at a version each time it changes. |
| the speaker record | write | What each speaker owes, what has arrived and what they have been told. |
| the asset store | write | Speaker material lands at versions as it arrives. |
| the speaker communication channel | write |  |
| the event's deadline list | read |  |
| the venue and room schedule | read |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
