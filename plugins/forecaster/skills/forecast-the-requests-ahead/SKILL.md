---
name: forecast-the-requests-ahead
description: Models the requests each support channel will receive in each interval from the history, the season and the events already known, such as releases, campaigns and price changes, with each assumption written beside the number it produced, and sets last period's forecast beside what arrived with the reason for each miss. Use it when running `ref/sup/forecast-support-volume`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Forecast the requests ahead

## What it does

Models the requests each support channel will receive in each interval
from the history, the season and the events already known, such as
releases, campaigns and price changes, with each assumption written
beside the number it produced, and sets last period's forecast beside
what arrived with the reason for each miss.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Compare the Last Forecast with What Arrived**
  - `ref/sup/forecast-support-volume`, activity 5 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)
- **Gather the Events Ahead**
  - `ref/sup/forecast-support-volume`, activity 4 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)
- **Model the Requests Ahead**
  - `ref/sup/forecast-support-volume`, activity 6 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)

## What to record

Every model at a version, saying which data it was fit on, over what
period, and which records it left out and why. Every prediction with the
model version that produced it and the inputs it was computed from, so
somebody can run it again and see whether the answer still holds. Every
assumption written beside the number it drives, naming where the
assumption came from and how far the number moves when the assumption
moves. A back-test result whenever the agent says a profile would have
picked the right customers, showing what the profile would have selected
and what actually happened to those accounts. A list of every rate it
could not source, marked unsourced, carried into the report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
