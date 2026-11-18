# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the deal pipeline | write | Each teaser or pitch, its screen note, the partner's decision, and any opportunity opened with its named owner. |
| the customer relationship management system, or CRM | write | Past meetings, bids, passes and owners matched before anything is read, and the outcome written back. |
| the pitch inbox and the website form | read | The deck as it arrived, with its sender and its channel. |
| the data room | read | The information memorandum and the seller's data, read only by the people the confidentiality agreement allows. |
| the restricted list | write | A seller or a company with listed securities is entered the day the confidentiality agreement is signed, for the chief compliance officer to hold. |
| the email system | write | The written withdrawal to the bank, sent before its deadline. |
| the notification channel | write | The timetable and the promised answer date raised to the partner while there is time to act. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
