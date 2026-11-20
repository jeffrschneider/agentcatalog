# The records this abstract agent must leave

This is the contract. An agent implementing
`customer-question-responder` leaves the following behind, on every run.

Each answer leaves the question as it arrived, the category it was read
under, the content and its version, the parts of the record read with
where each was read, each sentence traced to the content or the record
it rests on, the reply as sent with the article it named and its words
saying it comes from an agent and how to reach a person, the time it
took against the service level, and whether the customer said it settled
the question. Each case handed to a person leaves what was found, the
draft, the reason it needs a person and the words the customer was sent.
Each billing question leaves how the message was sorted, the invoice,
charge or payment read, and the article the answer rested on. Each
notice about an incident leaves the approved version sent, the case or
contact it went to, the route, and the time against any deadline an
agreement names. Each notice about a fix leaves its version and the team
lead's approval, each customer it went to and when, each reply and how
it was answered. Nothing in the record shows this agent answering from
general knowledge, sending words a named person had not approved,
sending a reply in a category kept for a person, promising a fix, a date
or money, or changing anything in an account or a bill.

An agent that leaves less than this does not implement
`customer-question-responder`, whatever else it does well.
