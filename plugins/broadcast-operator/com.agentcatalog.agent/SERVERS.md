# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the broadcast platform | write | The session, its access settings, its polls and its loaded material are set up here. |
| the live session | trigger | Starting it, ending it, putting a presenter on air, opening a poll, and recording. |
| the session recording store | write | The recording lands at a version with the date it was made. |
| the attendance and engagement record | write | Who joined, when they joined and left, what they answered and what they asked. |
| the registration record | read | Who is expected. |
| the asset store | read | The slides, the video and the graphics at the versions that were signed. |
| the event plan and its schedule | read |  |
| the speaker record | read | Who presents and what each of them owes. |
| the presenter back channel | write | What is said to the presenters while the session is running. |

There is deliberately no sending grant. This agent invites nobody,
because the email-producer agent sends the invitation, the reminder and
the follow-up to the list the run defines.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
