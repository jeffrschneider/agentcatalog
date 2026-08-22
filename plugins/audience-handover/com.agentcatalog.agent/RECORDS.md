# The records this abstract agent must leave

This is the contract. An agent implementing `audience-handover` leaves
the following behind, on every run.

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

An agent that leaves less than this does not implement
`audience-handover`, whatever else it does well.
