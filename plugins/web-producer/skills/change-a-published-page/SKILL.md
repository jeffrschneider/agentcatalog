---
name: change-a-published-page
description: Puts an approved change into a page that is already live and leaves it as a draft for the people who have to look at it. Use it when running `ref/mkt/feature-release` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Change a published page

## What it does

Puts an approved change into a page that is already live and leaves it
as a draft for the people who have to look at it. The change may be new
wording, new visuals, a new figure, or a fix to the part of the page
people are leaving from.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Fix What the Numbers Show**
  - `ref/mkt/landing-page`, activity 14 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)
- **Make the Change in the Page**
  - `ref/mkt/website-content-update`, activity 9 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)
- **Make the Changes in the Pages**
  - `ref/mkt/refresh-content`, activity 16 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Restate the Price Everywhere It Is Published**
  - `ref/mkt/pricing-change`, activity 7 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Update the Product Pages**
  - `ref/mkt/feature-release`, activity 6 -
    [Announce Feature Release](../../../../processes/marketing/feature-release.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
