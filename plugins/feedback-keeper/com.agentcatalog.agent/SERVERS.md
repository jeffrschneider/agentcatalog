# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the issue tracker | write | Each feature request logged for `<your product team>` or joined with the customer's words added, each account counted with what it pays, each answer to the product team's questions, each release taken in, each need a release missed, and each decision on a request, with no right to set a request's priority or mark it planned or released. |
| the support system | write | Each case marked with the request's reference, and each reply telling a customer how requests are handled, with the cases of the period read for the topics. |
| the CRM | read | Each account's plan and its owner. |
| the billing system | read | What each account asking pays. |
| the survey tool | read | The survey comments placed under the topics. |
| the complaints register | read | The period's complaints placed under the topics. |
| the policy library | read | `<your feature request policy>` at its version, with the approved wording on how requests are handled. |
| the report library | write | The topic list at its version and the evidence under each finding, for the report the reporting-manager agent owns. |
| the notification channel | write | Each question from the product team put to the support specialist who holds the case. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
