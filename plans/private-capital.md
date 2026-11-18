# Private Capital

A second pass at the catalog's department for the work of venture capital, growth equity and buyout firms, with Jeff's answers to the first pass's open questions applied. It still has 8 value streams, 40 processes and 30 agents (18 new, 12 reused), and 7 more existing agents are cited as they stand. Step tables come later.

## 1. Decisions

Jeff answered the first pass's five open questions. He decided 1, 2 and 5, and he left 3 and 4 to us, so the first pass's recommendations stand as the decisions for those two.

1. **Scope.** The department covers equity investing by venture, growth and buyout firms. Private credit comes later as its own value streams, because lending and loan servicing are different work.
2. **Which firms.** The department models only firms that invest a fund raised from outside investors.
3. **Venture and buyout.** The two share one department and one set of processes. A process carries a one-line Venture or Buyout note where the work differs, and a process that belongs to one strategy says so in that line.
4. **The fund administrator.** The agents are written as doing the fund's accounting work: capital accounts, capital calls, distributions, fees and tax documents. An outside fund administrator is treated as an outside party that may hold any of those roles for the firm or check the firm's work in them.
5. **Reused agents.** The four existing agents that were worded for marketing, sales or partners (`decision-coordinator`, `questionnaire-responder`, `reporting-manager` and `portal-keeper`) are widened in place to cover this department's uses, and no copies are made. The widened text is pushed to the catalog branch `widen-reused-agents-for-private-capital` and is not merged yet.

## 2. Department name

**Recommended: Private Capital.** The industry uses this name for firms that raise money from investors and put it into private companies, and it covers venture, growth and buyout without naming any one of them.

- **Private Markets.** This term is common, but it also takes in real estate, infrastructure and private credit, and investors often use it for the asset class they buy.
- **Equity Investment.** This one is plain and easy to read, but it leaves out credit funds and can be read as buying public stocks.

I set aside "Principal Investing" because it means investing a firm's own balance sheet. That fits a bank's desk better than a fund investing for its limited partners (LPs).

Proposed ids, following the catalog's pattern: folders `streams/private-capital/` and `processes/private-capital/`, and ids `vs/pc/<slug>` and `ref/pc/<slug>`.

## 3. Value streams

| # | Stream | Goal (the outcome it produces) | Main human roles |
|---|---|---|---|
| 1 | Strategy-to-Fund | A fund with a written strategy, its legal documents in force, and signed investor commitments at final close. | managing partner, partners, CFO, chief compliance officer, investor relations lead, fund counsel, placement agent, prospective LPs |
| 2 | Lead-to-Opportunity | Every company that reaches the firm (pitched, referred, sent by a banker or found in a sector search) gets a recorded screening decision, and each one worth pursuing becomes an opportunity with a named owner. | partners, principals, associates, analysts, founders and management teams, investment bankers, referrers |
| 3 | Opportunity-to-Recommendation | An investment memo that recommends investing on stated terms, with every claim resting on a diligence finding, or a recorded pass with its reason. | deal lead partner, principal, associate, outside advisers (accounting, legal, commercial), founders and management, customers and industry experts |
| 4 | Recommendation-to-Close | An investment that the committee approved, documented, signed, funded and recorded on the fund's books, or a decided no. | investment committee, deal lead partner, CFO, chief compliance officer, outside counsel, company founders and board, co-investors, lenders |
| 5 | Close-to-Value | A portfolio company working to a value creation plan that the firm and management agreed, with the firm's help delivered against it. | operating partner, deal lead partner as board director, platform and talent team, portfolio company CEO and management, portfolio company board |
| 6 | Quarter-to-Mark | A fair value for every holding each quarter, approved by the valuation committee, with each company's condition reviewed and its reserves set. | valuation committee, CFO, controller, partners, portfolio company CFOs, auditor |
| 7 | Hold-to-Exit | A holding turned into cash or shares the fund can distribute, or written off, with the proceeds settled and the result recorded. | deal lead partner, managing partner, investment committee, portfolio company CEO and board, sell-side bankers, counsel, buyers |
| 8 | Commitment-to-Statement | Every investor holds an accurate, on-time account of what it committed, paid in and received back, and of what its share is worth. | CFO, controller, fund administrator, investor relations lead, chief compliance officer, LPs, LP advisory committee, auditor, tax adviser |

Some decisions stay with people in every process: the committee's vote, the valuation committee's approval of the marks, every signature, every release of money, and a director's vote on a portfolio board.

**Later.** Private credit will be added as its own value streams, and continuation vehicles and other secondaries that a firm leads are also left for a later pass.

## 4. Processes (40)

A slug marked * is an existing catalog agent. Every other slug is a new agent from section 5. The last column notes only the work that differs between venture and buyout, and a blank means both run the process the same way. Growth equity takes the venture note when it buys a minority stake and the buyout note when it buys control.

### Strategy-to-Fund

| Process | What it does | Agents | Venture and buyout |
|---|---|---|---|
| Set the Fund Strategy | The partners agree what the fund will invest in, how large it will be, how the money splits between new deals and reserves, and what terms it will offer investors. | fund-modeler, researcher*, decision-coordinator* | Venture: a large share of the fund is held back for each company's later rounds. Buyout: the fund plans fewer and larger deals, each with borrowed money, and a smaller reserve for add-on acquisitions. |
| Form the Fund | The fund's entities are set up, its partnership agreement, offering memorandum and subscription documents are drafted, and the administrator, auditor and bank are chosen. | supplier-check*, close-plan-keeper*, signature-manager* | |
| Prepare the Fundraising Materials | The track record is calculated and checked, and the deck, the offering memorandum and the investor data room are built from it within the advertising rules. | performance-calculator, investor-relations-manager, disclosure-check*, portal-keeper* | Buyout: the track record splits each gain into earnings growth, a higher exit multiple and debt paid down. |
| Work an Investor Prospect | A prospective investor is found, approached, met and followed up until it says what it will commit or declines. | investor-relations-manager, prospect-researcher*, relationship-mapper*, meeting-scheduler* | |
| Answer a Due Diligence Questionnaire | An investor's questionnaire is answered from the firm's library of approved answers, and every new answer is signed by the person who owns it. | questionnaire-responder*, investor-relations-manager | |
| Negotiate the Fund Terms and Side Letters | Each investor's comments on the partnership agreement and its side letter requests are logged, priced, answered and agreed. | negotiation-coordinator*, redline-reviewer*, side-letter-keeper | |
| Hold a Fund Close | Each subscription is checked and each investor screened, the close is signed, later investors are trued up with earlier ones, and after the final close each investor makes its side letter elections. | subscription-reviewer, supplier-check*, capital-account-keeper, signature-manager*, side-letter-keeper | |

### Lead-to-Opportunity

| Process | What it does | Agents | Venture and buyout |
|---|---|---|---|
| Map a Sector | The firm writes down its thesis for a sector, lists the companies that fit it, and watches them for signs they are ready to talk. | company-scout, researcher* | Venture: the signs are a new product, a key hire or a coming round. Buyout: the signs are an owner ready to sell, another investor near the end of its hold, or a parent company selling a division. |
| Reach Out to a Company | A company found on a sector map is approached through the warmest path the firm has and brought to a first meeting. | company-scout, relationship-mapper*, meeting-scheduler* | |
| Screen an Inbound Pitch | A pitch from a founder or a referrer is matched to what the firm already knows, tested against the mandate, decided by a partner, and answered inside the promised time. | deal-screener, inbound-responder* | |
| Respond to a Sale Process | A company offered through a banker-run sale is screened, the confidentiality agreement is signed, the information memorandum is read, and an indication of interest goes in by the deadline or the firm withdraws. | deal-screener, returns-modeler, signature-manager* | Buyout: this is the usual way a deal starts, and the indication of interest states the price and how it will be paid for. Venture: this is rare, and it is seen mostly in late rounds that a banker runs. |

### Opportunity-to-Recommendation

| Process | What it does | Agents | Venture and buyout |
|---|---|---|---|
| Run Commercial and Product Diligence | The market, customers, competitors and product are tested against evidence from customer calls, expert calls and the product itself. | diligence-coordinator*, researcher* | Venture: with little history to test, the product, the founders and the early customers carry most of the weight. Buyout: an outside adviser often writes a commercial report that the lenders also read. |
| Run Financial Diligence | The company's numbers are rebuilt from its own records, covering revenue quality, margins, cash and the adjustments management proposes. | financial-analyst, diligence-coordinator* | Venture: the work is lighter and centers on cash burn, runway and unit economics. Buyout: outside accountants test the earnings that the price and the debt rest on, and set the working capital and net debt that the price is adjusted by. |
| Run Legal and Compliance Diligence | The capitalization, material contracts, ownership of the technology, litigation, and the background of the company and its leaders are checked. | cap-table-keeper, supplier-check*, diligence-coordinator* | Venture: the founders' assignment of the technology to the company and the cap table get the closest look. Buyout: the work adds competition filings for the change of control, and often insurance against breaches of the seller's promises. |
| Build the Investment Model | Entry price, ownership, dilution or debt, and exit scenarios are modeled so the return at each outcome is known before terms are offered. | returns-modeler, financial-analyst, cap-table-keeper | Venture: the model follows ownership through later rounds, the reserve the company will need, and the exit size that would return the fund. Buyout: the model carries the debt, the cash flow that pays it down, the covenants and the exit multiple. |
| Check the Deal Against the Fund Mandate | The investment is tested against the fund's limits and exclusions, the investors excused from it, the capital left to invest, and conflicts with other funds and portfolio companies. | mandate-check, fund-modeler | |
| Write the Investment Memo | The case is written with its thesis, findings, risks, model and proposed terms, and each claim is tied to the evidence under it. | memo-writer, diligence-coordinator*, returns-modeler | |

### Recommendation-to-Close

| Process | What it does | Agents | Venture and buyout |
|---|---|---|---|
| Decide at Investment Committee | The committee reads the memo, questions the deal team and votes, and the decision is recorded with its conditions and any dissent. | decision-coordinator*, memo-writer, mandate-check | |
| Issue a Term Sheet | The approved terms are written onto a term sheet, negotiated with the company and signed, with any exclusivity period recorded. | deal-structurer*, returns-modeler | Venture: the term sheet sets a priced round of preferred shares, with the liquidation preference, board seats and pro rata rights. Buyout: it is a letter of intent with the price, how it is financed, what management rolls over, and an exclusivity period. |
| Offer a Co-Investment | The share of a deal the fund will not take alone is offered to investors and partner firms under the allocation policy, and each allocation is recorded with its reason. | investor-relations-manager, mandate-check | Venture: the lead firm syndicates the round, sharing it with other firms and the company's existing investors. Buyout: the share the fund will not take goes mostly to the fund's own investors. |
| Negotiate the Definitive Agreements | The investment or purchase agreement is negotiated clause by clause against the signed term sheet. | deal-structurer*, redline-reviewer*, returns-modeler | Venture: the round's documents are usually close to a standard form. Buyout: the debt financing is negotiated with the lenders at the same time, and management's equity and rollover are settled. |
| Run the Closing | Every closing condition is met, the documents are signed, the money is wired to verified instructions, and the fund's new position is recorded. | close-plan-keeper*, signature-manager*, wire-check, cap-table-keeper | Venture: several investors often close together, sometimes in tranches tied to milestones. Buyout: the lenders fund at the same closing, the company's old debt is paid off, and every payment follows one funds flow. |

### Close-to-Value

A follow-on round (venture) or an add-on acquisition (buyout) starts in this stream and then runs through the diligence and committee processes like a new deal.

| Process | What it does | Agents | Venture and buyout |
|---|---|---|---|
| Hand Over to the Portfolio Team | Everything the deal team learned and promised passes to the people who will work with the company, and its reporting is set up from the first month. | handover-coordinator*, value-creation-planner, portfolio-monitor | Venture: the deal lead usually stays on as the company's board member, so the handover is mostly the reporting set-up. |
| Write the Value Creation Plan | The firm and management agree the few changes that will raise the company's value, each with an owner, a measure and a date, and progress is tracked against them. | value-creation-planner, financial-analyst, commitment-keeper* | Venture: the founders own the plan, and the firm offers help without control. Buyout: the firm has control, the plan opens with the first hundred days, and add-on acquisitions are often part of it. |
| Prepare and Hold a Board Meeting | The firm's director reads the board pack against the plan before the meeting, and the decisions, consents and actions the board agrees are recorded and followed up. | portfolio-monitor, value-creation-planner, commitment-keeper* | Venture: the firm holds one seat beside other investors and the founders. Buyout: the firm appoints most of the board. |
| Fill a Key Role at a Portfolio Company | The role is specified with the CEO, candidates are found through the firm's network and an outside search, and the chosen candidate's references are checked. | relationship-mapper*, researcher*, meeting-scheduler* | Venture: the founders make the hire, and the firm helps find candidates. Buyout: the firm can make the appointment itself, and the hire's equity comes from the management incentive plan. |
| Work a Company in Trouble | A company that is missing its plan, short of cash or breaching a covenant gets its options laid out, and the partners decide on a bridge, a restructuring, a sale or no further money. | portfolio-monitor, returns-modeler, decision-coordinator* | Venture: the choice is usually a bridge or an inside round among the existing investors. Buyout: the lenders are at the table, and the options include new equity to cure a covenant breach, new loan terms, or handing the company to the lenders. |

### Quarter-to-Mark

| Process | What it does | Agents | Venture and buyout |
|---|---|---|---|
| Collect the Portfolio Company Reports | Each company's financials and measures arrive on one template and are read against plan and the prior period, and any covenant or cash warning is raised. | portfolio-monitor, financial-analyst | Venture: the firm gets what its information rights allow, often each quarter. Buyout: the firm gets monthly management accounts and the covenant certificates the lenders also receive. |
| Value the Portfolio | Each holding gets a proposed fair value under the valuation policy with its method and inputs written down, and the valuation committee approves the marks. | valuation-analyst, cap-table-keeper, portfolio-monitor | Venture: the latest round's price is the usual starting point, adjusted for what has changed since. Buyout: the value starts from earnings times the multiples of comparable public companies and recent sales, less the debt. |
| Run the Portfolio Review | The partners go through every company's condition, update the watch list, and set the reserves held back for each company's later rounds. | portfolio-monitor, fund-modeler, decision-coordinator* | Venture: the main decision is each company's reserve and whether the fund takes its pro rata in the next round. Buyout: the closest look goes to each company's room under its covenants and the add-on acquisitions it is pursuing. |

### Hold-to-Exit

| Process | What it does | Agents | Venture and buyout |
|---|---|---|---|
| Plan the Exit | The route, timing and likely buyers for a holding are worked out with management and the board, and the committee approves the start. | exit-planner, returns-modeler, researcher*, decision-coordinator* | Venture: the firm seldom controls the timing, so the plan works through the board, and selling the fund's shares to another investor is one route. Buyout: the firm sets the timing, and a refinancing that pays the fund a dividend is one route before a sale. |
| Run a Sale Process | An adviser is chosen, the company is marketed, buyers' diligence is answered, the sale agreement is negotiated and signed, and the proceeds are settled against the cap table. | exit-planner, supplier-check*, negotiation-coordinator*, signature-manager*, cap-table-keeper | Venture: the company and its board run the sale, and the fund is one of many sellers, paid in the order its preferences set. Buyout: the firm runs the sale, often with a diligence report it commissions for buyers, and the proceeds repay the debt first. |
| Sell Down a Public Position | After a listing, the fund's shares are sold or distributed to investors in kind as the lock-up, the trading windows and the fund's plan allow. | exit-planner, cap-table-keeper, mandate-check | |
| Write Off a Failed Investment | A holding with nothing left is closed out, marked to zero and documented for tax, and its lessons are recorded against the original memo. | valuation-analyst, cap-table-keeper, memo-writer | |

### Commitment-to-Statement

| Process | What it does | Agents | Venture and buyout |
|---|---|---|---|
| Issue a Capital Call | Each investor's share of the money needed is calculated with excused investors and side letter terms applied, the notices go out, and every receipt is matched. | capital-account-keeper, side-letter-keeper, wire-check, portal-keeper* | |
| Make a Distribution | Proceeds run through the fund's waterfall, each investor's share and the carried interest are calculated, and the money is paid to verified accounts. | capital-account-keeper, wire-check, portal-keeper* | |
| Allocate Fees and Expenses | The management fee, fee offsets and every expense are charged to the fund, the firm or a portfolio company as the partnership agreement and side letters require. | capital-account-keeper, side-letter-keeper | Buyout: transaction and monitoring fees charged to portfolio companies are offset against the management fee, and the costs of deals that did not close are allocated. Venture: portfolio companies are rarely charged fees. |
| Issue the Quarterly Report and Statements | Each investor receives the quarter's letter, the fund's performance, the portfolio's marks and its own capital account statement, checked against its side letter reporting terms. | reporting-manager*, performance-calculator, capital-account-keeper, side-letter-keeper, portal-keeper* | |
| Seek an Advisory Committee Consent | A conflict or a departure from the partnership agreement goes to the LP advisory committee with the facts, and its decision is recorded. | decision-coordinator*, mandate-check, investor-relations-manager | |
| Close the Year-End Audit and Tax Documents | The auditor tests the year's valuations, capital accounts and fees, the audited statements are issued, and each investor receives its tax documents. | capital-account-keeper, valuation-analyst, portal-keeper* | |

## 5. Agents (30)

| Agent | Purpose | Home stream | Reuse |
|---|---|---|---|
| Fund modeler (`fund-modeler`) | Models the fund as a whole: its size, how many investments of what size, how much is held in reserve, the fees and carry, and the returns the strategy needs. | Strategy-to-Fund | new |
| Investor relations manager (`investor-relations-manager`) | Runs the firm's relationship with each investor, from a name on the target list through a signed commitment to the requests, consents and co-investment offers that follow. | Strategy-to-Fund | new |
| Side letter keeper (`side-letter-keeper`) | Holds every side letter as a list of obligations, runs the side letter elections after the final close, and checks each call, fee and report against what was promised. | Strategy-to-Fund | new |
| Subscription reviewer (`subscription-reviewer`) | Checks that each investor's subscription documents are complete and that the investor is eligible to be admitted before the close is signed. | Strategy-to-Fund | new |
| Company scout (`company-scout`) | Finds the companies that fit a written sector thesis, says why each one fits, and watches them for signs they are ready to talk. | Lead-to-Opportunity | new |
| Deal screener (`deal-screener`) | Reads each inbound pitch or banker's teaser, matches it to what the firm already holds, tests it against the mandate and the theses, and writes a screen note for a partner to decide from. | Lead-to-Opportunity | new |
| Financial analyst (`financial-analyst`) | Rebuilds a company's numbers from its own records and reports revenue quality, margins, cash and proposed adjustments, with each figure traced to its source. | Opportunity-to-Recommendation | new |
| Returns modeler (`returns-modeler`) | Models one investment from entry to exit, covering price, ownership, dilution or debt and exit scenarios, and states the return at each outcome with its assumptions. | Opportunity-to-Recommendation | new |
| Mandate check (`mandate-check`) | Tests a proposed investment, trade or allocation against the fund's limits and exclusions, excused investors, the restricted list, and conflicts with other funds and portfolio companies. | Opportunity-to-Recommendation | new |
| Memo writer (`memo-writer`) | Writes the investment memo and its later versions, ties every claim to the finding under it, and states the risks and the open questions. | Opportunity-to-Recommendation | new |
| Cap table keeper (`cap-table-keeper`) | Reads and models a company's capitalization, then holds the fund's position in it: share classes, preferences, rights, and what each exit price pays the fund. | Recommendation-to-Close | new |
| Value creation planner (`value-creation-planner`) | Drafts the value creation plan with management, puts an owner, a measure and a date on each change, and keeps the plan current. | Close-to-Value | new |
| Portfolio monitor (`portfolio-monitor`) | Collects each company's reports on one template, reads them against plan, the prior period and the covenants, and keeps the watch list. | Quarter-to-Mark | new |
| Valuation analyst (`valuation-analyst`) | Proposes each holding's fair value every quarter under the valuation policy, with the method, inputs and comparables written down for the committee and the auditor. | Quarter-to-Mark | new |
| Exit planner (`exit-planner`) | Works out the route, timing and buyers for an exit, prepares the company for it, and runs the sale or sell-down through to settlement. | Hold-to-Exit | new |
| Performance calculator (`performance-calculator`) | Computes deal and fund performance (IRR, multiples, distributions against paid-in capital), gross and net, from the cash flows and marks under a written method. | Commitment-to-Statement | new |
| Capital account keeper (`capital-account-keeper`) | Holds every investor's capital account, works out each investor's share of every call, distribution, fee, expense and carried interest allocation by the fund's waterfall, and prepares each investor's year-end tax documents. An outside fund administrator may hold this role for the firm or check the firm's work in it. | Commitment-to-Statement | new |
| Wire check (`wire-check`) | Confirms every outgoing payment against independently verified instructions and matches every incoming receipt to what was called, and releases no money itself. An outside fund administrator may hold this role for the firm or check the firm's work in it. | Commitment-to-Statement | new |
| Questionnaire responder | Answers investor due diligence questionnaires from the firm's library of approved answers. | Strategy-to-Fund | reuses `questionnaire-responder`, widened in place (decision 5) |
| Negotiation coordinator | Logs each investor's or buyer's asks, prices them, and records what was given, traded or refused. | Strategy-to-Fund | reuses `negotiation-coordinator` |
| Researcher | Finds and sources the outside evidence: sector research, customer and expert calls, candidate references and buyer lists. | Opportunity-to-Recommendation | reuses `researcher` |
| Diligence coordinator | Turns the investment thesis into what must be proved, keeps the request log, and rates every finding with an owner. | Opportunity-to-Recommendation | reuses `diligence-coordinator` |
| Supplier check | Screens investors, target companies and their leaders against registries and sanctions lists, and scores service providers and sell-side advisers against written criteria. | Opportunity-to-Recommendation | reuses `supplier-check` |
| Decision coordinator | Runs committee and partnership decisions from the open question to the recorded answer, and decides nothing itself. | Recommendation-to-Close | reuses `decision-coordinator`, widened in place (decision 5) |
| Deal structurer | Turns the approved deal into a term sheet and reads every redline of the definitive agreements back against it. | Recommendation-to-Close | reuses `deal-structurer` (its purpose already names an investment and a term sheet) |
| Redline reviewer | Reads markups of the fund documents and the deal documents clause by clause against the standard or agreed text. | Recommendation-to-Close | reuses `redline-reviewer` |
| Signature manager | Gets confidentiality agreements, subscription documents, closing documents and sale agreements executed and filed. | Recommendation-to-Close | reuses `signature-manager` |
| Close plan keeper | Holds the closing checklist, with one owner and one date on every condition still owed. | Recommendation-to-Close | reuses `close-plan-keeper` |
| Reporting manager | Owns the quarterly investor report for its period and sets the results beside what was committed. | Commitment-to-Statement | reuses `reporting-manager`, widened in place (decision 5) |
| Portal keeper | Holds what each investor can reach in the investor portal and data room, and publishes notices and statements at a version. | Commitment-to-Statement | reuses `portal-keeper`, widened in place (decision 5) |

The processes also cite seven existing agents in the roles they already hold: `disclosure-check` (fundraising material against the advertising rules), `prospect-researcher` (the investor target list), `relationship-mapper` (warm paths to investors, companies and candidates), `meeting-scheduler`, `inbound-responder` (answering a pitch inside the promised time), `handover-coordinator` (deal team to portfolio team) and `commitment-keeper` (the value creation plan and board actions).
