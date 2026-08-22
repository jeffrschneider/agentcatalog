# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | read | The stage, the amount and the close date as they stand, with every change and who made it. |
| the call record | read | The customer's own words, quoted rather than summarized. |
| the activity record | read | Who was met, how recently, and by whom. |
| the contract system | read | The steps a signature still has to pass. |
| the inspection record | write | The findings at a version, dated. |
| the clause record | write | What was decided last time the same change came up. |
| the loss record | write | The reason code, the buyer's words, the winner and the follow-up date. |
| the partner deal register | read | What a partner claimed, when, and the evidence they brought for it. |
| the notification channel | write | The people who worked a deal hear the outcome from us first. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
