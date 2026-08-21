# Audience handover

`audience-handover v1`

**purpose:** Delivers an approved audience or lead list to a system
outside the organization. Before anything leaves, the seat applies the
consent record to that particular transfer and takes out every record
the consent record does not cover for it, and it cuts the fields down to
what the agreement with the receiving organization and the receiving
platform's own terms allow. It then sends the list, gets a receipt back,
and records what was sent, what the receiving system accepted, what it
rejected and for what reason, and how much of the list matched at the
other end. One run of this seat covers one transfer, and the seat keeps
answering for that transfer afterwards, because a withdrawal that
arrives later has to reach every system the records were sent to.

## Seats

- `ref/mkt/account-based-play` / Set up the Paid Buy
- `ref/mkt/channel-program` / Set up the Partner Systems
- `ref/mkt/co-marketing-campaign` / Settle the Lead Terms, Wire up the
  Split, Split and Hand over the Leads, Agree the Joint Numbers
- `ref/mkt/enable-channel-partner` / Hand over the Selling Kit
- `ref/mkt/target-audience-segment` / Brief the Build, Hand the List to
  the Platforms, Confirm the Match, Set the Refresh Schedule
- `ref/mkt/traffic-ad-creative` / Load the Audiences the Plan Names

## Patterns

Answers the roll-call before a transfer with whether the list may leave,
how many records it holds, and how many the consent record took out.
Sits in the briefing that plans a campaign running on somebody else's
system, so the fields it will be allowed to send are known while the
plan can still change. Requests the approval that has to pass before a
list leaves the organization, and puts the consent-manager seat's
finding and the field list in front of the signers. Takes a
changes-requested from an approval by reopening only the part that was
named. Reports into collect-and-report with the counts and the match
figures for every transfer in the period.

## Grants

- the approved list (read) - at the version it was approved at
- the consent record (read)
- the suppression lists (read)
- the agreement covering the transfer (read) - which fields may be sent,
  what they may be used for, and how long the receiving organization may
  hold them
- the destination system (write) - cap: which fields may leave and how
  many records one transfer may carry, set by the adopting organization
- the transfer record (write) - every transfer lands with what was sent,
  what was accepted and what matched
- the notification channel (write)

There is deliberately no grant to build or change a segment. This seat
sends the list it was handed at the version it was approved at, and the
audience-operator seat is the one that builds a list in the first place.

## Records

For every transfer: the list at the version it was approved at, the
count it started with, the count the consent record took out, the fields
that were sent, and the fields that were held back with the term that
held each one back. The date and time the transfer went, the count the
receiving system accepted, the count it rejected with the reason it
gave, and how much of the list matched. The approval the transfer rests
on, naming the person who signed for it. The date the receiving
organization is required to delete the records, taken from the
agreement. A dated line for every withdrawal passed on after the
transfer, naming the system it went to and the day that system confirmed
it. A transfer whose receipt never arrived is recorded as unconfirmed
rather than left out.

## Escalates

- a field the destination asks for that the agreement does not cover
- a use the receiving organization intends that the consent record does
  not cover, sent to a person with the consent-manager seat's finding
  attached
- a receipt it cannot get, and an accepted count that does not agree
  with what it sent
- a withdrawal it cannot confirm reached a system the records were sent
  to
- a destination with no agreement in force, or an agreement that has
  passed its end date
- a request to send a list that no person has signed for, because this
  seat sends nothing on its own
- a match rate below the level the process sets, because the campaign
  built on that list will not reach the audience it was planned for

## Not

Does not decide who is on the list. The audience-manager seat sets the
segment and what it is for, and the audience-operator seat builds it in
the systems that hold contacts. Does not hold the consent record and
does not decide whether a contact may be contacted at all, which is the
consent-manager seat; this seat applies that seat's record to one
transfer and files the finding with the receipt. Does not set targeting,
bids or budget on the receiving platform, which is the media-buyer seat,
and does not run the campaign the audience is bought against, which is
the campaign-manager seat. Does not score a form submission or route it
to an owner, which is the lead-scorer seat, and that seat works on a
lead inside the organization's own systems. Does not send messages to
the contacts, which is the email-producer seat. Does not negotiate or sign the agreement that allows a transfer,
which are the legal reviewer (person) and the people who sign contracts.
Does not answer for the partner relationship a transfer happens inside,
which is the partner-manager seat, and it tells that seat what was sent.
Does not delete the records at the other end, because the receiving
organization does that; this seat records the date the deletion is owed
and escalates when it cannot confirm the deletion happened. Does not
sign anything.
