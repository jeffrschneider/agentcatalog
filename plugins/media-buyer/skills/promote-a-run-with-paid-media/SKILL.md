---
name: promote-a-run-with-paid-media
description: Runs the paid push behind an event, a session or a piece of content, pointed at whatever counts as a response, such as a registration or a read. Use it when running `ref/mkt/field-event` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Promote a run with paid media

## What it does

Runs the paid push behind an event, a session or a piece of content,
pointed at whatever counts as a response, such as a registration or a
read.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Promote the Conference**
  - `ref/mkt/user-conference`, activity 8 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Promote the Event**
  - `ref/mkt/field-event`, activity 9 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Promote the Piece**
  - `ref/mkt/long-form-content`, activity 15 -
    [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)
- **Promote the Session**
  - `ref/mkt/webinar`, activity 8 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
