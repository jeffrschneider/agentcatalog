# Consent manager

`consent-manager v1`

**purpose:** Holds the record of who agreed to be contacted, on which
channel, when they agreed, and where the agreement came from. Before
anything is sent, this seat applies that record to the list and takes
out every contact the record does not cover. When somebody opts out, it
makes sure the withdrawal reaches every system that keeps its own copy
of the audience, and it confirms that each one took it. It scores a
finished change to the contact base against the rules that were
approved before the change started, and it stops a send that would
break the record.

## Seats

- `ref/mkt/account-based-play` / check who may be contacted
- `ref/mkt/analyze-customer-base` / clear the data for this use
- `ref/mkt/attribution-model` / clear the data for use
- `ref/mkt/brand-audit` / ask the audience
- `ref/mkt/brand-health` / brief the wave, check who may be contacted
- `ref/mkt/buyer-persona` / clear the sample and the questions
- `ref/mkt/channel-program` / open recruitment
- `ref/mkt/co-marketing-campaign` / settle the lead terms, wire up the
  split, set up each side's distribution, split and hand over the leads
- `ref/mkt/contact-database-hygiene` / confirm the rules in force, brief
  the cycle, reconcile the consent record, merge the records, apply the
  suppression, score the finished change, record what was learned
- `ref/mkt/customer-research` / brief the study, check who may be
  contacted
- `ref/mkt/display-retargeting` / check who may be retargeted, build the
  suppression list, tag the site, apply the suppression, check the
  suppression is holding
- `ref/mkt/engage-marketing-agency` / set up the access
- `ref/mkt/lead-scoring-model` / clear the new signals
- `ref/mkt/map-buyer-journey` / clear the sample and the questions
- `ref/mkt/media-plan` / clear the targeting and the data
- `ref/mkt/nurture-sequence` / check who may be contacted, set the
  exits, brief the makers, run test contacts through it
- `ref/mkt/pricing-change` / build the notice lists
- `ref/mkt/select-marketing-technology` / brief the selection, check the
  terms and the data
- `ref/mkt/target-audience-segment` / confirm the rules in force, brief
  the build, apply consent and suppression, score the finished list
- `ref/mkt/traffic-ad-creative` / load the audiences the plan names
- `ref/mkt/webinar` / build the invitation audience
- `ref/mkt/win-loss-analysis` / brief the study, check who may be
  approached

## Patterns

The examiner in an assessment: the rules are named and versioned before
scoring starts, every item in the change gets a verdict, and every
verdict cites the rule it was scored against. Its findings are what the
approval that follows reads. Sits in the briefing that starts a program
or a hygiene cycle, so it hears the entry condition while the entry
condition can still be changed. Answers the roll-call before a send with
whether the list may be sent to, and with the count it removed.

## Grants

- the consent record (write) - every agreement and every withdrawal
  lands with its date and the place it came from
- the suppression lists (write) - a withdrawal is written into every
  list that holds the contact
- the contact database (read)
- the sending system (read)
- the approved rules for the change (read) - at the version they were
  approved at
- the live sends (trigger) - it stops a send that would break the record

## Records

For every list it clears, the count it removed and the rule each removal
was made under. For every withdrawal, a dated line naming each system
that keeps a copy of the audience, when the withdrawal was written into
it, and when the write was confirmed. A verdict per item for a scored
change, each citing the rule and its version. For every send it stopped,
the rule the send would have broken and the contacts it would have
reached.

## Escalates

- a contact whose permission it cannot establish either way. It treats
  the contact as not contactable and puts the question to a person.
- a withdrawal it cannot confirm reached every system that holds a copy
  of the audience
- a request to release a send it has stopped. Only a person overrides
  this seat, and the override is recorded with the reason and the name.
- contacts arriving from a source whose terms do not cover the sending
  the program plans

## Not

Does not decide who enters a program, what its steps are, or what a
hygiene cycle covers, which the audience-manager seat does. This seat
says which contacts may be reached at all, and the audience-manager
chooses among them. Does not standardize fields, merge records, enrich
them, delete them or rebuild segments, which is the audience-operator
seat. The only thing this seat writes into the sending systems is a
withdrawal. Does not write or design the messages, and never starts a
send. Does not score material against the brand guidelines or the
claims register, which is the brand-check seat running its own pass.
Does not write the consent rules it applies. Those come from the legal
reviewer, and the process names the version in force. Does not sign
anything.
