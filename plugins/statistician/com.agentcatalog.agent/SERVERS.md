# The systems this abstract agent needs

Thirteen systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the study design | read | The question, the method and the sample, at the versions they were set at. |
| the response record | read | Every response as it was given, and every response the study removed. |
| the customer and revenue record | read | The accounts, what they bought, what they renewed, and when they left. |
| analytics platforms | read |  |
| ad platforms | read | What each channel served and what came back. |
| licensed market data | read | Within the subscriptions the organization actually holds. |
| the calculation record | write | Every figure lands with the data behind it, the method used, the exclusions applied and the range around it. |
| the restricted analysis area | read | Only the group data a named person has released for one group fairness check, such as the protected characteristics employees chose to record, read for that check alone and closed to this agent when the check ends. |
| the control list | read | How often each control runs, how many times it ran in the period and what rests on it, which a control test's sample size is set from. |
| the test record | write | Each sample size with the method behind it, set before any item is drawn, and what the results of the test support. |
| the review record | read | Each reviewed support case's scores by part of the rubric, topic, channel and team, which a case review's results and the reviewers' agreement are worked out from. |
| the support system | read | How many cases closed in the period by team and channel, which a case review's sample size is set from. |
| the survey tool | read | The answers to each after-case survey with their counts, which the scores are worked out from. |

There is deliberately no write into the response record. This agent says
which responses it left out and under which rule, and the study-manager
agent keeps the responses as they were given. There is deliberately no
standing grant on the HR system or on any record of protected
characteristics either. This agent reads that data only in the
restricted analysis area, for the one check it was released for.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
