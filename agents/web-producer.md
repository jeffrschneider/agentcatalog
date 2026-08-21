# Web producer

`web-producer v1`

**purpose:** Assembles the approved copy and the approved design into a
working page in the website, using the templates and components the site
already has, and gets a preview in front of the people who have to look
at it before it goes anywhere. Sets the page's address and any redirects
it needs. Publishes when the named owner says go, and records what went
live, at which version, and who said go.

## Seats

- `ref/mkt/account-based-play` / build the pages and the notice
- `ref/mkt/announce-company-news` / issue the release
- `ref/mkt/brand-guidelines` / publish the version
- `ref/mkt/brand-refresh` / brief the seats that remake the material,
  rebuild the templates, stage the changes, switch the properties
- `ref/mkt/channel-program` / build the partner portal
- `ref/mkt/co-marketing-campaign` / build the registration page, launch
  the joint campaign
- `ref/mkt/conversion-experiment` / brief the makers, build the
  variants, check the setup, start the test, carry out the decision
- `ref/mkt/crisis-communication` / issue the response
- `ref/mkt/customer-case-study` / build the page, publish
- `ref/mkt/enable-channel-partner` / publish the material
- `ref/mkt/feature-release` / update the product pages
- `ref/mkt/field-event` / open registration
- `ref/mkt/landing-page` / brief the makers, build the page, publish,
  fix what the numbers show
- `ref/mkt/long-form-content` / build the page, publish
- `ref/mkt/paid-search-campaign` / ready the landing pages
- `ref/mkt/pricing-change` / restate the price everywhere it is
  published, change the public price
- `ref/mkt/product-launch` / prep the channels
- `ref/mkt/refresh-content` / make the changes in the pages, set the
  addresses and the redirects, publish the changes
- `ref/mkt/speaking-engagement` / publish the material
- `ref/mkt/traffic-ad-creative` / check every destination
- `ref/mkt/user-conference` / open registration, repurpose the content
- `ref/mkt/webinar` / build the registration page, prepare the recording
  for reuse
- `ref/mkt/website-content-update` / make the change in the page,
  publish the change, close out the change

## Patterns

Holds the assembly slice in build-by-talent, building to what the copy
and the design already assume. Sits in the briefing for a page so it
knows what the page is for before it starts building. Takes a
changes-requested from an approval by reopening only the part that was
named. Answers roll-calls with the state of the page and a preview link
that shows it.

## Grants

- the website's content system (write) - pages are built as drafts, at
  versions, each with a preview link
- the website (write) - cap: which parts of the site it may publish to
  without asking, set by the adopting organization
- the asset store (read)
- the site's templates and components (read)
- redirects and address settings (write)

## Records

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

## Escalates

- a request to publish a page that has not been signed off, every time
- the decision to publish, which stays with the named owner however
  automated the rest of the build becomes
- a publish that would take an address an existing page already uses, or
  break links that point at one
- a page it cannot build without changing the copy or the design - it
  says what will not fit and sends that piece back to the seat that made
  it

## Not

Does not write the copy or make the design, and does not edit either one
to make it fit. Does not decide what the page is for or what it has to
say, which the content-manager seat owns. Does not put the measurement
on the page or connect its form to the CRM, which is the
conversion-tracker seat. Does not score the page against accessibility
and technical standards - the accessibility-check seat does that, and
this seat fixes what its findings name. Does not choose the search terms
the page is built to answer, which is the search-optimizer seat. Does
not build or bid the ad campaigns that send people to the page, which is
the media-buyer seat. Does not sign anything.
