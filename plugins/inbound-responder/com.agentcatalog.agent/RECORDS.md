# The records this abstract agent must leave

This is the contract. An agent implementing `inbound-responder` leaves
the following behind, on every run.

Per inquiry: what was asked in the words it was asked in, the channel
and the arrival time, and the answer time that was promised. The
readings it answered from, each naming the system it came from and when
that reading was current, with any reading that could not be taken named
as unread rather than left out. The consent and do-not-contact check,
and the rule behind any no. The person named to answer. The reply at a
version, with the claim register entry behind every claim it makes. The
send time and channel. Every time offered and whether it was kept. Every
commitment made in the first conversation, with who made it and when it
is due. The answer time set against the promise, with a miss recorded as
a miss.

An agent that leaves less than this does not implement
`inbound-responder`, whatever else it does well.
