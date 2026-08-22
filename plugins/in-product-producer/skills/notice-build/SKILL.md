---
name: notice-build
description: Assembles a notice that appears inside the running product from copy and design that have already been signed off, and puts the tracking on it so what people do with it can be counted afterwards. Use it when running `ref/mkt/account-based-play`.
license: CC-BY-4.0
metadata:
  agent: in-product-producer
  agent-version: "1"
---

# Notice build

## What it does

Assembles a notice that appears inside the running product from copy and
design that have already been signed off, and puts the tracking on it so
what people do with it can be counted afterwards. It also builds the
pages that sit behind the notice when the run needs them.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Build the Pages and the Notice**
  - `ref/mkt/account-based-play`, activity 13 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)

## What to record

The notice at a version, with a preview that shows it the way an account
will see it. The audience at a version, with the count of accounts that
have the feature, the count left after the exclusion rules were applied,
and the rule behind every removal. The run settings as they were set,
naming where in the product the notice appears, the date it starts, the
date it ends, and how often one person sees it. The go record naming the
version that went live, the time it was switched on, and the person who
said go. The takedown record naming the version that came down and the
date it came down. The report afterwards, giving the accounts that saw
the notice, the people who did what it asked, the people who dismissed
it and the people who did nothing. Anything it could not verify is
recorded as unverified instead of being left out.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
