# The records this abstract agent must leave

This is the contract. An agent implementing `rights-register` leaves the
following behind, on every run.

The rights record, with one entry per source saying what the source is,
who granted it, what the license covers, the channels and territories it
may run on, the date it starts, the date it ends, and where the document
is kept. A verdict for every source put to it before production, naming
the source, the channels and territories it was checked against, the
answer, and the term the answer rests on. For every finished asset, the
list of sources it rests on, each tied to the rights record entry that
cleared it and the version of the asset that used it. A dated warning
for every license running out, naming the published work that rests on
it and the date the license ends. A source whose rights it could not
establish is recorded as uncleared, with what is missing, rather than
being left out.

An agent that leaves less than this does not implement
`rights-register`, whatever else it does well.
