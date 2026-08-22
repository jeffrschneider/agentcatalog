# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the enablement library | write | Each piece lands at a numbered version, and the version reps hold is the one recorded here. |
| the claims register | read | At its version. |
| brand guidelines | read |  |
| the asset store | read |  |
| the competitive record | read | What has been established about each competitor, at its version. |
| the CRM | read | What deals were won and lost, and what they were lost to. |
| the usage record for the material | read | Which pieces reps opened and in which deals. |
| the notification channel | write | Reps hear which version is current and from when. |

There is deliberately no write into the CRM. This agent reads what deals
were won and lost to work out what the material has to answer, and it
changes nothing there.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
