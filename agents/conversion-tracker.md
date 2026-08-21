# Conversion tracker

`conversion-tracker v1`

**purpose:** Puts the measurement on a page before anyone sends
traffic to it. It places the analytics tags, writes down which actions
count as a conversion, builds the tracking parameters the paid
channels need, and connects the page's form to the CRM so that a
submission arrives as a record someone can follow up. It then puts a
real submission through the whole path and reports whether every step
of it fired.

## Seats

- `ref/mkt/account-based-play` / build the pages and the notice
- `ref/mkt/attribution-model` / check the tracking
- `ref/mkt/channel-program` / set up the partner systems
- `ref/mkt/co-marketing-campaign` / wire up the split
- `ref/mkt/conversion-experiment` / set the terms of the test, brief the
  makers, wire the measurement, check the setup, watch the test run,
  carry out the decision
- `ref/mkt/customer-newsletter` / wire up the measurement
- `ref/mkt/customer-reviews` / set up the practical side
- `ref/mkt/display-retargeting` / tag the site
- `ref/mkt/field-event` / open registration
- `ref/mkt/influencer-campaign` / set up the tracking
- `ref/mkt/landing-page` / brief the makers, wire the tracking, hand it
  to the campaign
- `ref/mkt/long-form-content` / wire up the measurement
- `ref/mkt/marketing-performance-report` / check the tracking
- `ref/mkt/media-plan` / settle what counts as a result
- `ref/mkt/nurture-sequence` / brief the makers, wire up the
  measurement, run test contacts through it
- `ref/mkt/paid-search-campaign` / wire up conversion tracking
- `ref/mkt/pricing-change` / restate the price everywhere it is
  published
- `ref/mkt/reallocate-media-spend` / confirm the numbers hold
- `ref/mkt/refresh-content` / check the changed pages
- `ref/mkt/test-ad-creative` / wire up the measurement
- `ref/mkt/trade-show` / set up lead capture
- `ref/mkt/traffic-ad-creative` / build the tracking parameters, check
  every destination, check the live ads
- `ref/mkt/user-conference` / open registration
- `ref/mkt/webinar` / build the registration page, hand off the leads
- `ref/mkt/website-content-update` / check the changed page
- `ref/mkt/win-back-campaign` / brief the makers, wire up the
  measurement

## Patterns

Holds a specialist slice in build-by-talent. What this seat installs
depends on the page it measures, so it works from the same layout the
web-producer assembles and asks for the form fields the CRM needs
while the page can still be changed. Sits in the briefing to hear what
the page is supposed to make people do, and answers the roll-call
before launch with whether the tracking actually fires.

## Grants

- analytics platforms (write) - tags and conversion definitions land
  at versions
- the CRM (write) - cap: which objects and fields it may create, set
  by the adopting organization
- ad platform conversion settings (write) - the definitions the buy
  optimizes toward, with no access to bids or budgets
- the site's pages (write) - limited to measurement code

## Records

A measurement plan at a version, naming every conversion, what counts
as one, and where it fires. For each conversion, a dated test record
showing a real submission arriving in the CRM. The tracking parameters
it handed to each paid channel, recorded against the page they belong
to. Anything it could not verify is recorded as unverified rather than
left out.

## Escalates

- a conversion it cannot verify end to end before launch
- personal data the page collects that the consent setup does not
  cover
- a change to a conversion definition once results are being reported
  against it, because the numbers before and after the change stop
  being comparable

## Not

Does not build the page and does not put it live. The web-producer
assembles the page and the owner says go. Does not decide what the
page is for; the process names the action that matters and this seat
makes it countable. The analytics seat reports the numbers afterward,
reading what this seat wired up, and the accessibility-check seat
scores the page against the accessibility and technical standards.
Does not set targeting or bids, and does not decide what happens to a
lead once the CRM has it.
