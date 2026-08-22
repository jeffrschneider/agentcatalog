---
name: clear-a-source-for-use
description: Checks a proposed clip, image, font, piece of music or appearance release against the rights record and says whether it may be used on the channels and in the territories the piece will run on. Use it when running `ref/mkt/approve-marketing-material` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: rights-register
  agent-version: "1"
---

# Clear a source for use

## What it does

Checks a proposed clip, image, font, piece of music or appearance
release against the rights record and says whether it may be used on the
channels and in the territories the piece will run on. A source it
cannot establish rights for comes back as uncleared, with what is
missing.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Check the Sources Can Be Used**
  - `ref/mkt/video-asset`, activity 4 -
    [Produce Video Asset](../../../../processes/marketing/video-asset.md)
- **Clear the Rights**
  - `ref/mkt/customer-case-study`, activity 5 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)
  - `ref/mkt/video-asset`, activity 12 -
    [Produce Video Asset](../../../../processes/marketing/video-asset.md)
- **Clear the Rights for These Channels**
  - `ref/mkt/traffic-ad-creative`, activity 3 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Confirm the Rights**
  - `ref/mkt/approve-marketing-material`, activity 7 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)

## What to record

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

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
