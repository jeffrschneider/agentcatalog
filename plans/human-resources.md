# Human Resources

A first pass at the catalog's department for a company's own human resources (HR) function, at an employer of a few hundred people or more. It follows the employee's whole time with the company, from the plan that creates a role to the day the person leaves, and it covers HR's own operations. It has 8 value streams, 44 processes and 44 agents (21 new, 23 reused). Activity tables come later.

## 1. Decisions

I made these calls so the work could start. Jeff can override any of them, and the documents that follow are written to them.

1. **Scope.** The department models a company's own HR function at an employer of a few hundred people or more, for the employee's whole time with the company and for HR's own operations. It does not model a staffing agency, a recruitment firm or an outside HR provider that serves other companies, though any of those may hold a role for the company in a roster.
2. **Payroll belongs here.** HR runs payroll, from the changes that feed it to the payments, the withholding and the year-end statements. Finance checks it: a named finance person checks each pay register against the ledger and the last period before a named approver releases the payments, and finance reconciles the payroll accounts each month. An outside payroll provider may hold the payroll administrator's role for the company or run the calculation that the company checks, and the roster says which.
3. **Jurisdiction-neutral.** Laws differ by country and by state, so no document states one country's law as the rule. Where a local rule decides a step, such as final pay, notice periods, leave, when a background check may run, what a job posting must say or how long a record is kept, the document leaves a blank such as `<your jurisdiction's rule on final pay>`, and the adopting company's counsel fills it in. A company that employs people in several places fills each blank once for each place.
4. **People decide about people.** Hiring and rejection decisions, offers, pay changes, promotions, discipline, terminations, the findings of an investigation, accommodations and leave approvals are each made by a named person. By the same rule, so are performance ratings, the end of a probation period and who is selected in a layoff. The phases that hold these decisions carry `automation: never`. Agents gather, draft, check, schedule, record and remind.
5. **Least personal data.** Agents never weigh a protected characteristic in anything they do about a person, and each step sees the least personal data it needs. The application screener reads applications with the name, photo, age and other details the step does not need withheld. Health records (from leave and accommodations), investigation records and background check results are held apart and open only to the named people who must see them, and the agents that hold them pass on only the outcome, such as the dates of an approved leave.
6. **Group fairness checks.** One use of protected characteristics stays in, and it is my call for Jeff to confirm. The checks that look for unfair outcomes across groups, which are pay against like work in the pay review, the selection for a layoff, and the group figures in the required filings and the workforce report, are run by the statistician agent on data a named person releases for that check alone. The agent reports results for groups above a minimum size and never a result about one person, and named people decide what to do. If Jeff prefers that people run these checks with no agent, the processes keep the same shape with a person in that role.
7. **Reused agents.** Twenty-three existing agents take work here. Eight of them need their purpose or Not line widened in place (`onboarding-manager`, `curriculum-manager`, `commitment-keeper`, `wire-check`, `handover-coordinator`, `disclosure-check`, `analytics` and `questionnaire-responder`), following the Private Capital decision to widen in place and make no copies. The other fifteen fit as they stand.
8. **Stream names.** Following Jeff's new rule, each stream's title is a friendly descriptor in a buyer's words, its slug is the kebab form of that title, and its document has no friendly name line.
9. **Left for later.** Each of these is left for a later pass, for the reason given.
   - Unions and collective bargaining: bargaining and running a collective agreement differ by country, sector and agreement, and they deserve a value stream of their own.
   - Immigration and visas: sponsorship and work permits are specific to each country and usually run with outside counsel, so onboarding checks only the right to work.
   - Executive pay and equity plans: a committee of the board decides them on its own cycle, with public disclosure and plan administration that finance and legal share.
   - Moves between countries: they depend on the immigration and cross-border tax work left out above.
   - Health and safety at work: operations or facilities usually own it, with incident processes of their own.
   - Contractors and temporary workers: procurement usually buys them, and whether a worker counts as an employee is a legal question that each jurisdiction answers differently.
   - Employment claims and lawsuits: counsel leads them, and HR's part, the records and the case history, runs through Answer a Records Request and the employee relations case record.

## 2. Department name

**Recommended: Human Resources.** It is the name most buyers use for the function and for the person who leads it, it reads plainly beside Sales, Marketing and Private Capital, and it covers payroll and compliance as well as the programs for people.

- **People.** Many companies now call the function People or People Operations, and the name reads warmly, but on its own in a catalog list it does not say what the department does.
- **Talent.** This name is popular for recruiting and development, but buyers read it as leaving out payroll, benefits, employee relations and compliance.

I set aside "Human Capital Management" because it names a category of software more than a department.

Proposed ids, following the catalog's pattern: folders `streams/human-resources/` and `processes/human-resources/`, and ids `vs/hr/<slug>` and `ref/hr/<slug>`.

## 3. Value streams

| # | Stream | Slug | Outcome it produces | Main human roles |
|---|---|---|---|---|
| 1 | Workforce planning | `workforce-planning` | An approved plan for the year with each team's headcount and labor cost, an organization structure everyone can read, and every new or replacement position approved before anyone is recruited into it. | chief executive, executive team, head of HR, finance lead, department heads, HR business partners, compensation lead |
| 2 | Hiring | `hiring` | Each approved position filled by a candidate who accepted a written offer and was chosen by the hiring manager on scored evidence, with every other applicant given an answer. | hiring manager, recruiter, interview panel, compensation lead, offer approvers, candidates, referees, background check provider |
| 3 | Onboarding | `onboarding` | Each new hire starts on the agreed day with the paperwork and the right to work confirmed, access and equipment working, the policies acknowledged, and a plan for the first months that ends in a recorded outcome. | new hire, hiring manager, HR operations, IT, payroll, facilities, a buddy |
| 4 | Pay and benefits | `pay-and-benefits` | Every employee is paid the right amount on the right day with the withholding filed, paid within a range the company can explain, enrolled in the benefits they chose, and supported through any leave. | payroll manager, finance controller, payroll approver, compensation lead, benefits lead, leave approvers, managers, employees, benefits broker and carriers |
| 5 | Performance and development | `performance-and-development` | Every employee is reviewed fairly on the company's cycle with a recorded rating, objectives and a development plan, promotions are decided on evidence, required training is complete, and each key role has its possible successors named. | managers, employees, calibration and promotion panels, HR business partners, learning lead, head of HR |
| 6 | Employee relations | `employee-relations` | Every concern an employee raises reaches a written answer from a named person inside the promised time, every investigation ends in findings an investigator signed, and every disciplinary outcome is consistent with the policy and with past cases. | employee relations lead, HR business partners, named investigators, managers, employees who raise concerns and the people named in them, counsel, the people who decide discipline and accommodations |
| 7 | Leaving the company | `leaving-the-company` | Every departure rests on a resignation or a recorded decision, and each leaver receives final pay and documents on time, returns company property, loses access on the last day and hands over the work, while the company learns why people leave. | departing employee, manager, HR business partner, head of HR, counsel, payroll, IT, executive sponsor for a layoff, employee representatives where consultation is required |
| 8 | HR operations | `hr-operations` | An accurate record for every employee, employees' questions answered, policies current and acknowledged, every required filing made and every audit answered on time, and access to personal data kept to the people who need it. | HR operations lead, HR system administrator, privacy lead, counsel, finance, auditors and inspectors, employees and former employees |

Some decisions stay with people in every process: every hiring or rejection decision, offer, pay change, promotion, rating, disciplinary outcome, dismissal, layoff selection, investigation finding, accommodation and leave approval, and every signature and release of money.

**Later.** Unions and collective bargaining, immigration and visas, executive pay and equity plans, moves between countries, health and safety, contractors and temporary workers, and employment claims are left for a later pass, for the reasons in decision 9.

## 4. Processes (44)

A slug marked * is an existing catalog agent. Every other slug is a new agent from section 5. Where a process holds a decision about a person, its description names who decides, and the phase that holds that decision carries `automation: never`. An employee's own targets are called objectives in these documents, so the word goals belongs only to each process's goals section.

### Workforce planning

| Process | What it does | Agents |
|---|---|---|
| Plan the Workforce | Each year the leaders set every team's headcount, roles and labor cost from the business plan, the hiring and leaving the company actually had, and the skills it will need, and the executive team and finance approve the plan. | workforce-planner, analytics*, decision-coordinator* |
| Open a Position | A manager's request for a new or replacement position is checked against the plan and the budget, the job is placed at a level with its pay range, and the named approvers sign before anyone is recruited. | workforce-planner, compensation-analyst |
| Change the Organization Structure | A reorganization is drawn up as options with their cost and reporting lines, the effect on each role is listed, named leaders decide what happens to each person, and the change is announced and recorded on one date. | workforce-planner, decision-coordinator*, comms-manager*, employee-record-keeper |
| Report on the Workforce | Each period the leaders receive headcount, hires, leavers, time to fill and labor cost against the plan, with the reasons people gave for leaving, and any figure about a group is shown only above a minimum group size. | reporting-manager*, analytics*, workforce-planner |

### Hiring

| Process | What it does | Agents |
|---|---|---|
| Plan the Hire | The hiring manager and the recruiter agree the must-haves, a structured interview plan with scored questions, the panel, the sources and the dates before anyone is approached. | recruiting-coordinator, meeting-scheduler* |
| Post a Job | The posting is written from the approved job, checked for wording that would put off qualified people and for the statements `<your jurisdiction's rules>` require, such as a pay range, and published where the plan says. | copywriter*, disclosure-check*, recruiting-coordinator |
| Find Candidates | People who match the must-haves are found through employee referrals, past applicants who agreed to be kept on file and the sources the company may use, and the recruiter approaches each one. | candidate-sourcer, relationship-mapper* |
| Screen Applications | Each application is read against the written must-haves only, with the details the step does not need withheld, the recruiter decides who goes forward, and every applicant hears back. | application-screener, recruiting-coordinator |
| Run the Interviews | The panel is briefed, each interview is scheduled and scored on its own against the plan, and the hiring manager decides at a debrief from the scores and the evidence. | recruiting-coordinator, meeting-scheduler* |
| Check a Candidate's Background | With the candidate's written consent, and only at the point `<your jurisdiction's rules>` allow, references are taken and the checks the role requires are run, the results are seen only by the named people, and a person decides on any finding after the candidate has had the chance to respond. | background-check, researcher* |
| Make an Offer | The offer is built within the approved range and checked against the pay of people in the same job, the named approvers sign it, it is sent and negotiated within set limits, and the signed acceptance passes the hire to onboarding. | offer-builder, compensation-analyst, negotiation-coordinator*, signature-manager* |

### Onboarding

| Process | What it does | Agents |
|---|---|---|
| Prepare for a New Hire | Between the signed offer and the first day, the employee record is created, the forms and the proof of the right to work are collected under `<your jurisdiction's rules>`, payroll and benefits are set up, and access and equipment are ordered and tested. | onboarding-manager*, employee-record-keeper, tool-administrator* |
| Run New Hire Orientation | Each group of new starters is taken through the company, its policies and the first required training, and each person's acknowledgment of the policies is recorded. | onboarding-manager*, curriculum-manager*, policy-keeper, training-coordinator |
| Run a New Hire's First Months | The manager and the new hire agree a plan for the first months, the check-ins happen on their dates, and where the contract sets a probation period the manager confirms, extends or ends it before the date it closes. | onboarding-manager*, commitment-keeper*, employee-record-keeper |

### Pay and benefits

| Process | What it does | Agents |
|---|---|---|
| Run Payroll | Each pay period the changes are gathered, pay is calculated from gross to net under `<your jurisdiction's tax and deduction rules>`, finance checks the register against the last period, a named person approves it, and the payments and the withholding go out on time. | payroll-administrator, wire-check*, employee-record-keeper |
| Close the Payroll Year | The year's payroll is reconciled to the ledger and the tax filings, any correction is made before the deadline, and each employee receives the year-end pay and tax statement `<your jurisdiction>` requires. | payroll-administrator, filing-coordinator |
| Change an Employee's Pay | A pay change outside the pay review, such as for a promotion, a move or a market adjustment, is checked against the range, the budget and the pay of people in the same job, approved by named people, and paid from its effective date. | compensation-analyst, payroll-administrator, employee-record-keeper |
| Run the Pay Review | The ranges are refreshed from market data, the budget and the guidelines are set, managers propose changes within them, pay is compared across groups doing like work before anything is approved, named people approve, and each employee receives a letter. | compensation-analyst, researcher*, statistician*, decision-coordinator* |
| Run Benefits Open Enrollment | The plans are renewed with the carriers through the broker, named people decide any change to the plans, employees are told what changed and make their elections, and the elections reach the carriers and payroll by the deadline. | benefits-administrator, supplier-check*, decision-coordinator* |
| Enroll an Employee in Benefits | A new hire, or an employee with a life event such as a birth or a marriage, is told what they may elect and by when, eligibility is checked, and the elections reach the carriers and payroll inside the window. | benefits-administrator, payroll-administrator |
| Manage a Leave of Absence | A leave request is checked against the policy and `<your jurisdiction's leave rules>`, any health information is seen only by the named people, a named person approves the leave, pay and benefits during the leave are set, and the return is planned. | leave-coordinator, benefits-administrator, payroll-administrator |

### Performance and development

| Process | What it does | Agents |
|---|---|---|
| Run the Performance Review | Each cycle employees, peers and managers write down evidence of the work, the managers' ratings are calibrated by a panel of leaders, each employee hears the result in a conversation, and the next period's objectives and development plan are recorded. | performance-review-coordinator, decision-coordinator*, career-planner |
| Decide Promotions | Each nomination is written against the expectations of the next level with its evidence, a panel decides, and each promotion carries its pay change and its announcement. | performance-review-coordinator, compensation-analyst, decision-coordinator* |
| Run a Performance Improvement Plan | A gap in performance is written down with its evidence, a plan with dates and the support the company will give is agreed, progress is checked on each date, and a named person decides the outcome. | commitment-keeper*, employee-case-keeper, performance-review-coordinator |
| Plan Succession for Key Roles | Leaders review each key role, name the people who could step into it and how ready each one is, and turn the gaps into development actions or hiring plans. | career-planner, workforce-planner, decision-coordinator* |
| Plan the Learning Program | The year's learning needs are gathered from the development plans, the reviews and the skills the workforce plan calls for, the program is chosen within its budget, and each course is built or bought. | curriculum-manager*, career-planner, training-coordinator |
| Run Required Training | Training that the law or the company requires is assigned by role and location, completion is tracked and chased, and the record shows who completed what and when. | training-coordinator, curriculum-manager* |
| Move an Employee to a New Role | An employee applies for or is offered an internal role, the hiring manager chooses on the same criteria used for outside candidates, and the move happens on a set date with the pay, the record and the work handed over. | career-planner, recruiting-coordinator, compensation-analyst, handover-coordinator* |

### Employee relations

| Process | What it does | Agents |
|---|---|---|
| Resolve an Employee Concern | A concern raised in any channel, named or anonymous, is logged and acknowledged, a named person chooses whether it is answered with guidance, heard as a grievance or investigated, and the employee receives a written answer inside the promised time. | employee-case-keeper, policy-keeper |
| Investigate a Workplace Complaint | A named investigator writes the allegations as questions, interviews the witnesses and gathers the evidence, then writes and signs the findings, and a named person decides what follows. | investigation-coordinator, employee-case-keeper |
| Issue a Disciplinary Action | A conduct matter is set against the policy and the outcomes of similar past cases, the employee is heard, a named person decides, and the outcome is delivered in writing with the route to appeal. | employee-case-keeper, policy-keeper |
| Handle an Accommodation Request | A request for a change to a job or a workplace is logged, the employee and the manager talk through what would work, only the information needed is collected and kept restricted, a named person decides, and the change is put in place and reviewed. | accommodation-coordinator, leave-coordinator |
| Run the Employee Survey | The survey is designed to compare with the last one, run so that no answer can be traced to a person, reported only for groups above a minimum size, and turned into actions with owners and dates. | study-manager*, statistician*, commitment-keeper* |

### Leaving the company

| Process | What it does | Agents |
|---|---|---|
| Offboard a Leaver | Any departure, whether a resignation, a retirement, a dismissal or a layoff, is carried from the confirmed last day to the closed record: the work is handed over, property is returned, access ends on the last day, final pay is worked out under `<your jurisdiction's rule on final pay>`, benefits end or continue, and the leaver is offered an exit interview. | separation-coordinator, handover-coordinator*, tool-administrator*, payroll-administrator, benefits-administrator |
| Dismiss an Employee | A proposed dismissal for performance or conduct is checked against the record, the policy and `<your jurisdiction's rules on dismissal>` with counsel, named people decide, the conversation is held, and the leaving process starts. | separation-coordinator, employee-case-keeper |
| Run a Layoff | The business reason and the roles affected are written down, the selection criteria are fixed before any names are applied, the selection is checked for unfair outcomes across groups, notice and consultation follow `<your jurisdiction's rules on collective dismissal>`, leaders decide, and each person affected is told in person with the support on offer. | separation-coordinator, workforce-planner, statistician*, comms-manager* |
| Negotiate a Separation Agreement | Separation terms are drafted within the policy, the employee gets the time and the advice `<your jurisdiction's rules>` require, every change is read against the standard text, and the agreement is signed before any payment under it. | separation-coordinator, negotiation-coordinator*, redline-reviewer*, signature-manager* |

### HR operations

| Process | What it does | Agents |
|---|---|---|
| Answer an Employee's Question | An employee's question about pay, benefits, leave or policy is answered from the approved policy library at its version for the employee's location, inside the promised time, and anything personal or sensitive goes to a named person. | employee-question-responder, policy-keeper |
| Change an Employee Record | A change to an employee's record, such as a new address, a new manager or a new bank account, is checked for authority and evidence, applied on its effective date, and passed to payroll, benefits and access. | employee-record-keeper, wire-check* |
| Publish an HR Policy | A new or changed policy is drafted with the variant each location needs, reviewed by counsel against `<your jurisdiction's rules>`, approved by named people, published at a version, and acknowledged by the people it applies to. | policy-keeper, training-coordinator |
| File a Required Report | Each filing, return and notice on the compliance calendar is prepared from checked data, signed by the named person, filed by its deadline and kept with its receipt. | filing-coordinator, data-quality-check* |
| Respond to an Employment Audit | An audit or inspection of pay, hours, records, benefits or the right to work is logged, each request is answered from the records with only the data asked for, a named person signs the response, and each finding is fixed and closed. | filing-coordinator, employee-record-keeper, questionnaire-responder* |
| Answer a Records Request | A request to see, correct, confirm or delete employee data, from an employee, a former employee or an outside party, is checked for identity and authority, answered with only what it covers within `<your jurisdiction's deadline>`, and recorded. | employee-record-keeper, employee-question-responder |
| Review Access to Employee Data | Each period the access to the HR systems is listed, every person who can open health, investigation or background check records is checked against the named people allowed, and any access nobody approved is removed. | tool-administrator*, employee-record-keeper |

## 5. Agents (44)

| Agent | Purpose | Home stream | Reuse |
|---|---|---|---|
| Workforce planner (`workforce-planner`) | Builds and holds the workforce plan: each team's headcount, roles and labor cost for the year, worked from the business plan and the hiring and leaving the company actually had. It checks each position request against the plan, models the cost and the reporting lines of a reorganization or a layoff, and reports the workforce against the plan each period. | Workforce planning | new |
| Recruiting coordinator (`recruiting-coordinator`) | Runs a hire from the approved position to the accepted offer: the must-haves, the structured interview plan, the posting, the pipeline, the interview loop and the record of the hiring manager's decision, and it makes sure every candidate gets an answer. | Hiring | new |
| Candidate sourcer (`candidate-sourcer`) | Finds people who match a hire's written must-haves through referrals, past applicants who agreed to be kept on file and the sources the company may use, records where each one came from, and drafts the approach the recruiter sends. | Hiring | new |
| Application screener (`application-screener`) | Reads each application against the written must-haves only, with the name, photo, age and other details the step does not need withheld, and writes a short note on each applicant that cites the must-have behind each point, for the recruiter who decides. | Hiring | new |
| Background check (`background-check`) | Runs the checks a role requires, with the candidate's written consent and only at the point `<your jurisdiction's rules>` allow, holds the results where only the named people can see them, and runs the notice and response steps before a person decides on any finding. | Hiring | new |
| Offer builder (`offer-builder`) | Drafts the offer from the approved position and the figure the compensation analyst checked, routes it to the named approvers, sends it once they sign, logs the candidate's asks against the approved limits, and records the signed acceptance. | Hiring | new |
| Compensation analyst (`compensation-analyst`) | Places each job at a level in the company's job framework, keeps a pay range for every level from market data, and checks every offer, pay change and pay review proposal against the range, the budget and the pay of people doing like work. It proposes figures, and named people approve every pay decision. | Pay and benefits | new |
| Payroll administrator (`payroll-administrator`) | Runs each pay period from the changes to the payments: it calculates gross to net under `<your jurisdiction's tax and deduction rules>`, compares the register with the last period, prepares it for the finance check and the named approver, and files the withholding and the year-end statements. It releases no money itself, and an outside payroll provider may hold this role for the company. | Pay and benefits | new |
| Benefits administrator (`benefits-administrator`) | Holds each employee's benefit eligibility and elections, runs open enrollment and each new hire or life event enrollment, sends the elections to the carriers and the deductions to payroll, matches the carriers' bills to the enrollments, and sends the continuation notices when someone leaves. | Pay and benefits | new |
| Leave coordinator (`leave-coordinator`) | Takes each leave request, checks it against the policy and `<your jurisdiction's leave rules>`, collects only the documents needed and keeps health information restricted, tracks the leave and the return date, and sets pay and benefits during the leave for the named person who approves it. | Pay and benefits | new |
| Performance review coordinator (`performance-review-coordinator`) | Runs the review cycle and the promotion round: it requests self-reviews and peer feedback, checks each manager's draft for an example behind every rating and flags remarks about personality, prepares the calibration packs, and records the ratings and promotions the managers and the panels decide. | Performance and development | new |
| Career planner (`career-planner`) | Holds each employee's development plan and the career paths between jobs, prepares the succession review of key roles from the readiness managers record, and matches development actions and internal openings to the people who asked for them. | Performance and development | new |
| Training coordinator (`training-coordinator`) | Assigns required and planned training by role and location, books people onto sessions, chases completion, and keeps the training record that managers and auditors read. | Performance and development | new |
| Employee case keeper (`employee-case-keeper`) | Holds every employee relations case, named or anonymous, from intake to close: it acknowledges the concern, records the route and every decision a named person makes, keeps the clock and the restricted file, and shows the person deciding discipline the outcomes of similar past cases. | Employee relations | new |
| Investigation coordinator (`investigation-coordinator`) | Supports the named investigator from the complaint to the signed findings: it writes the allegations as questions, plans the witnesses and the evidence, schedules the interviews in confidence, keeps the evidence log and the timeline, and sets out the evidence against each allegation. The investigator writes and signs the findings. | Employee relations | new |
| Accommodation coordinator (`accommodation-coordinator`) | Runs a request for a change to a job or a workplace from the request to the review: it sets up the conversation between the employee and the manager, collects only the information needed and keeps it restricted, lists the options with their cost and effect, records the decision a named person makes, and checks the change on its review date. | Employee relations | new |
| Separation coordinator (`separation-coordinator`) | Runs each departure from the confirmed last day to the closed record: the leaving checklist across payroll, benefits, access and property, the handover, the final documents and the exit interview. For a dismissal or a layoff it keeps the record behind the decision and the notice calendar `<your jurisdiction's rules>` set, and it drafts separation terms within the policy. | Leaving the company | new |
| Employee record keeper (`employee-record-keeper`) | Holds each employee's record in the HR system from the hire to the end of the retention period: it creates the record, applies each approved change on its date with its evidence, keeps health, investigation and background check records apart under restricted access, passes changes to payroll, benefits and access, and answers records requests. | HR operations | new |
| Policy keeper (`policy-keeper`) | Holds every HR policy and the handbook at versions, with the variant that applies in each location, drafts changes from approved decisions, collects acknowledgments, and answers which version applied to whom on a given date. | HR operations | new |
| Filing coordinator (`filing-coordinator`) | Keeps the calendar of every filing, return and notice the company owes about its workforce in each location, prepares each one from checked data for a named person to sign, files it by its deadline, and keeps the request log of an audit or an inspection. | HR operations | new |
| Employee question responder (`employee-question-responder`) | Answers employees' questions about pay, benefits, leave and policy from the approved library at its version and inside the promised time, reads the policy that applies to the asker's location, and passes anything personal or sensitive to a named person. | HR operations | new |
| Analytics | Reads the workforce numbers (headcount, hiring, leaving and labor cost) and reports them with their sources for the plan and the workforce report. | Workforce planning | reuses `analytics`, widened in place (decision 7): its purpose names only marketing work, and it widens to the workforce numbers |
| Decision coordinator | Runs the approval of the workforce plan, the decisions in a reorganization, the pay review approval, calibration, promotion panels, the succession review and the choice of benefit plans, and decides nothing itself. | Workforce planning | reuses `decision-coordinator` as it stands |
| Comms manager | Runs the staff announcement of a reorganization or a layoff, from the confirmed decision to the report afterwards. | Workforce planning | reuses `comms-manager` as it stands |
| Reporting manager | Owns the workforce report for each period and sets the results beside the plan. | Workforce planning | reuses `reporting-manager` as it stands |
| Meeting scheduler | Books the intake meeting for a hire and each interview with a candidate, and briefs everyone who attends. | Hiring | reuses `meeting-scheduler` as it stands |
| Copywriter | Writes the job posting from the approved job, inside the company's voice. | Hiring | reuses `copywriter` as it stands |
| Disclosure check | Checks each job posting for the statements each location requires, such as a pay range. | Hiring | reuses `disclosure-check`, widened in place (decision 7): its purpose covers marketing material, and it widens to the statements a job posting must carry |
| Relationship mapper | Finds who at the company already knows a candidate, so a referral comes through the person who holds the relationship. | Hiring | reuses `relationship-mapper` as it stands |
| Researcher | Takes a candidate's references and gathers the market pay data the pay review reads. | Hiring | reuses `researcher` as it stands (its purpose already names a hire) |
| Negotiation coordinator | Logs a candidate's asks on an offer and a leaver's asks on separation terms, and records what was given, traded or refused. | Hiring | reuses `negotiation-coordinator` as it stands |
| Signature manager | Gets offers and separation agreements executed and filed. | Hiring | reuses `signature-manager` as it stands |
| Onboarding manager | Carries each new hire from the signed offer to a confirmed start: the record, the forms, the access and equipment ordered and tested, orientation, and the plan for the first months. | Onboarding | reuses `onboarding-manager`, widened in place (decision 7): its purpose names only a joiner to a revenue team, and it widens to any new hire |
| Wire check | Confirms every change to an employee's bank account through a contact already on file, and checks each payroll payment file against the approved register before a person releases it. | Pay and benefits | reuses `wire-check`, widened in place (decision 7): its purpose is written for a fund, and it widens to employees' bank accounts and the payroll payment file |
| Statistician | Runs the group fairness checks in the pay review and a layoff, and sets the minimum group size below which no survey or workforce figure is shown. | Pay and benefits | reuses `statistician` as it stands, on the restricted data that decision 6 sets |
| Supplier check | Scores the carriers' and the broker's renewal proposals against criteria written down before any proposal arrived. | Pay and benefits | reuses `supplier-check` as it stands |
| Curriculum manager | Builds and keeps the company's learning material, its orientation material and the content of required training at versions. | Performance and development | reuses `curriculum-manager`, widened in place (decision 7): its purpose is written for teaching the product and the market, and it widens to the company's learning program, orientation and required training |
| Commitment keeper | Keeps score on a new hire's plan for the first months, a performance improvement plan and the actions from the employee survey, each item with one owner, one date and a state. | Performance and development | reuses `commitment-keeper`, widened in place (decision 7): its Not line names the joint-planner agent as the author of the plan, and it widens to a plan a manager and an employee agree, held in a restricted record |
| Study manager | Owns the employee survey from the questions to the findings, and keeps each survey comparable with the last one. | Employee relations | reuses `study-manager` as it stands |
| Handover coordinator | Hands a leaver's or a mover's work, contacts and open commitments to a named successor. | Leaving the company | reuses `handover-coordinator`, widened in place (decision 7): its purpose covers a customer relationship, and it widens to the work of a leaver or a mover |
| Redline reviewer | Reads the changes the leaver or the leaver's adviser makes to a separation agreement against the standard text, clause by clause. | Leaving the company | reuses `redline-reviewer` as it stands |
| Tool administrator | Opens a new hire's accounts, closes a leaver's accounts on the last day, and lists who can see what in the HR systems for the access review. | HR operations | reuses `tool-administrator` as it stands (its purpose already closes a leaver's account) |
| Data quality check | Checks the data behind each required filing before the named person signs it. | HR operations | reuses `data-quality-check` as it stands |
| Questionnaire responder | Answers an auditor's or an inspector's request list from approved answers and the records behind them. | HR operations | reuses `questionnaire-responder`, widened in place (decision 7): its purpose covers security, legal, procurement and investor questionnaires, and it widens to an auditor's or an inspector's request list |

## 6. Widened agents

Eight of the twenty-three reused agents needed their purpose or their Not text changed, the same eight decision 7 names. Each change is the smallest one that removes the contradiction with the Human Resources work, and each agent keeps its meaning for the departments it already served. The other fifteen reused agents took their Human Resources processes and activities with no change to either text. Each entry quotes the wording before and after.

1. **Analytics (`analytics`), purpose.** Its examples named only marketing work.
   - Before: "Tracks a campaign against its brief, pulls the wrap-up numbers from every channel, files the weekly status, and audits the scoring model behind lead routing."
   - After: "Tracks a campaign against its brief, pulls the wrap-up numbers from every channel, files the weekly status, audits the scoring model behind lead routing, and reads the headcount, hiring, leaving and labor cost behind a workforce plan and report."
2. **Commitment keeper (`commitment-keeper`), purpose.** It kept score only on a signed joint plan, and a plan about one employee must be restricted.
   - Before: "Keeps score against a joint plan. Every commitment in a signed plan becomes an item with one owner, one date and a state, ..."
   - After: "Keeps score against a joint plan or any other agreed plan, and holds a plan about one employee in a restricted record that only the people the plan names can open. Every commitment in a signed or agreed plan becomes an item with one owner, one date and a state, ..."
3. **Commitment keeper (`commitment-keeper`), Not.** It named the joint-planner agent as the only author of a plan's changes.
   - Before: "Does not decide what changes in the plan or write the amendment, which is the joint-planner agent."
   - After: "Does not decide what changes in the plan or write the amendment, which is the joint-planner agent, or the people who agreed the plan where no joint-planner agent wrote it, such as a manager and an employee."
4. **Curriculum manager (`curriculum-manager`), purpose.** It was written for teaching the product, the market and the sales process.
   - Before: "Holds the material people are taught and keeps it current as the product, the market and the process move."
   - After: "Holds the material people are taught, from a seller's courses to the company's learning program, orientation and required training, and keeps it current as the product, the market, the process, the policies and the rules move."
5. **Disclosure check (`disclosure-check`), purpose.** It covered only marketing material.
   - Before: "That covers the wording a regulator requires beside a claim, the terms that have to appear with a price, the rules a promotion runs under, and what a paid partnership has to say about being paid."
   - After: "That covers the wording a regulator requires beside a claim, the terms that have to appear with a price, the rules a promotion runs under, what a paid partnership has to say about being paid, and the statements a job posting must carry in each location, such as a pay range."
6. **Handover coordinator (`handover-coordinator`), purpose.** It moved only a customer or portfolio relationship.
   - Before: "Moves a relationship from the people who won it to the people who will work it from now on, such as a seller to a delivery team or a deal team to a portfolio team, so nobody on the other side has to repeat themselves."
   - After: "Moves a relationship from the people who won it to the people who will work it from now on, such as a seller to a delivery team or a deal team to a portfolio team, and moves the work, contacts and open commitments of an employee who leaves or changes roles to a named successor, so nobody on the other side has to repeat themselves."
7. **Onboarding manager (`onboarding-manager`), purpose.** It carried only a joiner to a revenue team, and its run closed only on a seller's first customer conversation.
   - Before: "Carries somebody who has just joined a revenue team from a confirmed start date to a real customer conversation they can hold unaided." and "The run stays open until the first conversation has been debriefed and the ramp has been reported."
   - After: "Carries somebody who has just joined a revenue team from a confirmed start date to a real customer conversation they can hold unaided, and carries any new hire from the signed offer through the first day, orientation and the plan for the first months." and "For a seller, the run stays open until the first conversation has been debriefed and the ramp has been reported."
8. **Onboarding manager (`onboarding-manager`), Not.** It now prepares a probation review and tells the new hire the outcome, so it says who decides the probation.
   - Before: "Does not decide whether the joiner is ready, which is the certification-check agent's run and a human signature."
   - After: "Does not decide whether the joiner is ready, which is the certification-check agent's run and a human signature, and does not decide a probation, which the manager confirms, extends or ends."
9. **Questionnaire responder (`questionnaire-responder`), purpose.** It answered only security, legal, procurement and investor questionnaires.
   - Before: "Answers security, legal, procurement and investor due diligence questionnaires from a maintained source of answers rather than from memory."
   - After: "Answers security, legal, procurement and investor due diligence questionnaires, and an auditor's or an inspector's request list, from a maintained source of answers rather than from memory."
10. **Wire check (`wire-check`), purpose.** It was written for a fund's payments alone.
    - Before: "... for the fund's chief financial officer (CFO) and controller, and releases no money itself." and "The point of the job is that money leaves the fund only to accounts proven to be right, ..."
    - After: "... for the fund's chief financial officer (CFO) and controller or an employer's payroll manager and payroll approver, and releases no money itself." and "The point of the job is that money leaves the fund or the payroll only to accounts proven to be right, ..."
    - Added after the sentence on reconciling each call and distribution: "For an employer's payroll it confirms each new employee bank account through a contact already on file, checks each payment in the payroll payment file against the approved register and the verified bank record before a named person releases it, and confirms where each payment landed."
11. **Wire check (`wire-check`), Not.** It named only the CFO and the second signer as the people who release money.
    - Before: "Does not release, approve or sign a payment, which is the CFO and the second signer (people)."
    - After: "Does not release, approve or sign a payment, which is the CFO and the second signer, or for payroll the payroll approver and the second signer (people)."

Two capability descriptions in `skills/wire-check.md` were widened to match: `verify-payment-instructions` now checks each employee's account as well and confirms a change through a contact already on file, and `follow-each-outgoing-payment` now checks each payment a named person releases, such as the chief financial officer or the payroll approver.
