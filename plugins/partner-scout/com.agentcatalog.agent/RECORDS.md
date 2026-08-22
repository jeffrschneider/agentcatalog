# The records this abstract agent must leave

This is the contract. An agent implementing `partner-scout` leaves the
following behind, on every run.

The search bounds it was given, including the companies it may not
touch. Every candidate with the source it came from and the date it was
read. Every removal with the reason it was removed. Every score against
the closing test with the evidence line behind it and the date that
evidence was read, so a second person scoring the same candidate can get
the same answer or say where they differ. The approach as sent, the
date, and what each candidate was told. The replies, the refusals and
the silences, each dated.

An agent that leaves less than this does not implement `partner-scout`,
whatever else it does well.
