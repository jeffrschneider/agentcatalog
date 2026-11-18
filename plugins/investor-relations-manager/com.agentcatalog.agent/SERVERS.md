# The systems this abstract agent needs

Twelve systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the customer relationship management system, or CRM | write | Every contact, interest, decline and promise is written here the same day. |
| the data room | write | Opened to an investor or a candidate only under its signed confidentiality agreement, and closed when its run ends. |
| the document store | write | The deck, the case studies and the memorandum at their versions, and every version that was sent. |
| the design tools | write | The deck and the case studies are laid out here from the frozen figures. |
| the investor portal | write | Co-investment offers, consent requests and the decisions investors must be told. |
| the investor's own portal | write | A questionnaire response goes in through the route and format the investor asks for. |
| the allocation record | write | Who was offered, what each asked for, what each got, and why. |
| the signature system | trigger | Confidentiality agreements sent for a person to sign; this agent never signs. |
| the decision record | read | The committee decision an offer rests on, and the advisory committee decision investors must be told. |
| the side letter register | read | Co-investment rights and the notice terms a consent decision has to meet. |
| the fund accounting system | read | Figures a questionnaire or a follow-up asks for, as the books hold them. |
| the notification channel | write |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
