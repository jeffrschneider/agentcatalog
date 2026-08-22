# Reference process: Work a Referral

`ref/sls/work-a-referral v1`

**value stream:** [Prospect-to-Meeting](../../streams/sales/prospect-to-meeting.md)
Somebody who is known offers to introduce somebody who is not. The
offer is answered the same day, the account is checked for an owner,
and the person is read before anybody writes to them. The seller agrees
what the introduction should say, the introducer confirms they will
send it, and the consent record is checked before the first contact.
The introducer gets a note they can send as it stands, and a date. One
reminder follows, then the referral is let go. The introducer hears how
it went either way.

## The activities

| # | Activity | What happens | Agents |
|---|---|---|---|
| 1 | Take in the Referral | who was named, by whom, and why | [prospect-researcher](../../agents/prospect-researcher.md) · seller (person) |
| 2 | Thank the Introducer | the person who offered gets an answer that day | seller (person) |
| 3 | Check the Account | who owns the account, and what is already open | [account-monitor](../../agents/account-monitor.md) |
| 4 | Read the Person and the Account | what they do, and what the introducer said | [researcher](../../agents/researcher.md) · prospect-researcher |
| 5 | Agree What Is Being Asked | what the introduction should say, and to whom | seller (person) · prospect-researcher |
| 6 | Check the Introducer Is Willing | the introducer confirms before their name is used | seller (person) |
| 7 | Check Consent and Suppression | the person's record checked before any contact | [consent-manager](../../agents/consent-manager.md) |
| 8 | Write the Introduction | the note the introducer sends, ready to send | seller (person) · [sequence-operator](../../agents/sequence-operator.md) |
| 9 | Ask for the Introduction | the introducer gets the note and a date to send | seller (person) · sequence-operator |
| 10 | Wait and Chase Once | one reminder, then the referral is let go | sequence-operator |
| 11 | Take the Handover | the introduction lands and the seller answers fast | seller (person) · [meeting-scheduler](../../agents/meeting-scheduler.md) |
| 12 | Book the Conversation | the reply becomes a meeting in the diary | meeting-scheduler |
| 13 | Tell the Introducer What Happened | the introducer hears the outcome, good or bad | seller (person) |
| 14 | Record the Referral | who introduces well, and what came of it | prospect-researcher · account-monitor |

## The graph

```mermaid
flowchart LR
  T([somebody offers to introduce somebody else]) --> A1[1. Take in the Referral]
  A1 --> A2[2. Thank the Introducer]
  A1 --> A3[3. Check the Account]
  A3 -. another seller already owns the account .-> A1
  A3 --> A4[4. Read the Person and the Account]
  A4 --> A5[5. Agree What Is Being Asked]
  A2 --> A5
  A5 --> A6[6. Check the Introducer Is Willing]
  A6 -. the introducer wants a different ask .-> A5
  A6 --> A7[7. Check Consent and Suppression]
  A7 -. the person may not be contacted .-> A13[13. Tell the Introducer What Happened]
  A7 --> A8[8. Write the Introduction]
  A8 --> A9[9. Ask for the Introduction]
  A9 --> A10[10. Wait and Chase Once]
  A10 -. still nothing after the reminder .-> A13
  A10 --> A11[11. Take the Handover]
  A11 -. the person named is not the right one .-> A5
  A11 --> A12[12. Book the Conversation]
  A12 -. no time is agreed .-> A11
  A12 --> A13
  A13 --> A14[14. Record the Referral]
  A14 --> DONE([the introduction was worked and the introducer knows how it went])
```

## The document, with the blanks marked

```
PROCESS: work a referral               id: <team>/work-a-referral   v1
from: ref/sls/work-a-referral v1
owner: <who>                           effective: <date>
trigger: somebody offers an introduction, or <your seller role> asks a
         customer, a partner or a colleague for one
         watch: record=<referral> system=<your referral record>
                change=<somebody offers an introduction>
         or watch: record=<referral> system=<your referral record>
                change=<a seller asks a customer, a partner or a
                colleague for an introduction>
concurrency: runs may overlap freely - one referral is one run, and one
             introducer is asked for no more than <n> at a time
goal: an introduction that is actually sent, answered within <hours>,
      turned into a meeting where the person wants one, and reported
      back to the introducer either way
phases:
  take-in-referral - human: who was named, by whom, and what the
                     introducer said about them
                     owner: <your seller role>   after: trigger
                     by: <hours>                 automation: <level>
  thank-introducer - human: the person who offered gets an answer the
                     same day, whether or not the referral is worked
                     owner: <your seller role>
                     after: take-in-referral
                     by: <hours>                 automation: <level>
  check-account    - runs assessment: who owns the account today, what
                     is open against it, and whether it is already
                     being worked by a sequence
                     owner: account-monitor
                     after: take-in-referral     automation: <level>
  read-the-person  - runs collect-and-report: what the person does,
                     what the account is dealing with, and what the
                     introducer already knows about both
                     owner: researcher           after: check-account
                     by: <days>                  automation: <level>
  agree-the-ask    - convenes decide-and-announce: what the
                     introduction asks for, of whom, and what happens
                     next if the person says yes
                     owner: <your seller role>
                     after: read-the-person + thank-introducer
                     automation: <level>
  confirm-willing  - human: the introducer says in writing that their
                     name may be used, for this ask, to this person
                     owner: <your seller role>   after: agree-the-ask
                     by: <days>                  automation: never
  check-consent    - runs assessment: the consent record and the
                     suppression list checked for this person before
                     anybody writes to them
                     owner: consent-manager      after: confirm-willing
                     automation: <level>
  write-intro      - runs build-by-talent: the note the introducer
                     sends, written so it can go as it stands, and what
                     the seller sends the moment it lands
                     owner: <your seller role>   after: check-consent
                     by: <days>                  automation: <level>
  ask-for-intro    - human: the introducer gets the note, the date it
                     should go, and one line on what happens after
                     owner: <your seller role>   after: write-intro
                     automation: <level>
  chase-once       - system: one reminder after <days>, and no more. A
                     referral with no answer after that is let go, and
                     the introducer is told it was
                     owner: sequence-operator    after: ask-for-intro
                     by: <days>                  automation: <level>
  take-handover    - human: the introduction lands and the seller
                     answers within <hours>, in the same thread, asking
                     nothing the introducer already answered
                     owner: <your seller role>   after: chase-once
                     by: <hours>                 automation: <level>
  book-meeting     - human: the reply becomes a meeting in the diary,
                     with the introducer dropped from the thread first
                     owner: meeting-scheduler    after: take-handover
                     by: <days>                  automation: <level>
  tell-introducer  - human: the introducer hears what came of it,
                     whether it went well or nowhere at all
                     owner: <your seller role>   after: book-meeting
                     by: <days>                  automation: <level>
  record-referral  - convenes debrief: who introduces well, what came
                     of each introduction, and what to ask for next
                     time
                     owner: prospect-researcher
                     after: tell-introducer      automation: <level>
handoffs:
  take-in-referral -> thank-introducer [the-referral]: who was named,
    by whom, and what the introducer offered to do
  take-in-referral -> check-account [named-account]: the account the
    named person works for, and the date the offer was made
  check-account -> read-the-person [account-ownership]: who owns the
    account, what is open against it, and whether a sequence is already
    touching it
  read-the-person -> agree-the-ask [person-and-account]: what the
    person does, what the account is dealing with, and what the
    introducer already knows
  thank-introducer -> agree-the-ask [introducer-offer]: what the
    introducer said they are willing to do, in their own words
  agree-the-ask -> confirm-willing [the-ask]: the ask as it will be
    made, and the person it will be made to
  confirm-willing -> check-consent [written-agreement]: the
    introducer's written agreement, dated, and the person it covers
  check-consent -> write-intro [contact-permission]: whether this
    person may be contacted, on which channel, and what the record took
    out
  write-intro -> ask-for-intro [the-note]: the note the introducer
    sends, ready to send, and what the seller sends after it
  ask-for-intro -> chase-once [send-dates]: the date the note was given
    and the date it was meant to go
  chase-once -> take-handover [introduction-as-sent]: the introduction
    as it was actually sent, and everything the introducer said in it
  take-handover -> book-meeting [the-reply]: the person's reply, and
    what they asked for in it
  book-meeting -> tell-introducer [meeting-outcome]: whether a meeting
    was agreed, and when it sits
  tell-introducer -> record-referral [outcome-as-told]: the outcome as
    the introducer was told it
deviations:
  check-account -> take-in-referral [account-owned-elsewhere]: another
    seller already owns the account, so the referral goes to them with
    the introducer's words attached
  confirm-willing -> agree-the-ask [different-ask-wanted]: the
    introducer wants a different ask, so a smaller ask, or none, is
    agreed rather than pressing the one they refused
  check-consent -> tell-introducer [may-not-be-contacted]: the person
    may not be contacted, so no note is written and no introduction is
    asked for, and the introducer hears that instead
  chase-once -> tell-introducer [no-answer-after-reminder]: there is
    still nothing after the one reminder, so the referral is let go
    with no handover and no meeting, and the introducer is told it was
  take-handover -> agree-the-ask [wrong-person]: the person named is
    not the right one, so the ask is agreed again against whoever is
  book-meeting -> take-handover [no-time-agreed]: no time is agreed, so
    the handover is worked again rather than the reply going cold
bindings:
  roster:  <who holds each role - agents claiming the abstract agents
           above, and named people for the seller who answers, and
           whoever settles an account two sellers both claim>
  systems: the CRM (write), the mail system (write), the calendar
           (write), the consent record (read), the suppression list
           (read), <your referral record> (write)
  data:    the introducer's written agreement, <your ideal customer
           profile> <version>, what the introducer said about the
           person
policy:
  the introducer's name is used only after they have said in writing
    that it may be, and only for the ask they agreed to
  the person who offered the introduction hears back within <hours>,
    and hears the outcome later whether it was good or bad
  a referral is chased once and then let go, because a chased
    introducer stops introducing
  a referred person still goes through the consent record before any
    contact, and a referral never overrides the suppression list
  a referred person is never dropped into an outbound sequence
  an account another seller owns goes to that seller with the
    introducer's words attached, and the introducer is told who now
    holds it
measures:
  cycle time: <hours> from the offer to the introducer being answered,
              and <days> from the introduction landing to a meeting
  coverage: <target> share of offered introductions that were actually
            sent
  volume: <referrals per period>, and how many introducers gave more
          than one
  quality gate: no name used without written agreement, and every
                introducer told the outcome
```

## The failure edges

- **The account already has an owner.** The account-monitor agent finds
  another seller on the record, and the referral goes to them with the
  introducer's words attached. The introducer is told who now holds it
  so they are not left wondering, and the original seller does not
  write to the person anyway.
- **The introducer goes quiet.** The note was given and never sent. One
  reminder goes after the stated wait, and then the referral is let go.
  Chasing an introducer a third time costs the next introduction, which
  is worth more than this one.
- **The introducer will not use their name.** They offered warmly and
  then pulled back. The run returns to the ask rather than pressing,
  and a smaller ask, or none, is agreed. Nobody writes to the person
  claiming an introduction that was not given.
- **The person may not be contacted.** The consent-manager agent finds
  them on the suppression list or outside consent, and the referral
  stops there. A referral is not a route around the record, and the
  introducer is told the contact could not be made.
- **The person named is the wrong person.** The introduction lands and
  the reply says somebody else owns this. The run goes back to the ask,
  the introducer is asked whether they know the right person, and the
  wrong person is not worked as a prospect on the strength of a
  misdirected introduction.
- **The seller answers slowly.** An introduction sits unanswered past
  the stated window, and the introducer's credit is spent for nothing.
  The delay is recorded against the run and escalated, because this is
  the single most expensive failure here.
- **The introducer is asked too often.** One introducer carrying many
  asks stops answering. The concurrency line caps how many are open
  with one introducer at a time, and a new referral waits rather than
  joining the pile.
- **The meeting is agreed and then never held.** Booking is where this
  run hands over, and a meeting that does not happen is worked by the
  booking process rather than being counted here. The introducer is
  still told what came of it.
- **A run is abandoned.** The introducer is told before anything else,
  in a sentence that does not make them chase us. The note already
  given to them is withdrawn, the person is not contacted, and the
  account goes back so somebody else can approach it cold rather than
  half warmed.
