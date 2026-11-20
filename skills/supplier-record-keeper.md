# supplier-record-keeper

## collect-a-new-suppliers-details

Takes in the request for a supplier with no record, and collects its
legal name, address, contacts, payment terms and bank details in one
request, with the tax forms and numbers the local rules require for each
place the company buys from it.

covers:
- Collect What Tax Rules Require
- Collect the Supplier's Details
- Take in the Request for a Supplier

## assemble-and-open-the-record

Assembles the record at a version with every field's evidence and the
result of every check, opens it for orders and payments once a named
approver has approved it, and tells the requester and the supplier.

covers:
- Assemble the Record
- Open the Record for Use
- Tell the Requester and the Supplier

## hold-a-bank-detail-change

Logs a request to change a supplier's bank details as it arrived, keeps
the message and its attachments unchanged as evidence, and holds the
change so every payment keeps going to the account on the record.

covers:
- Hold the Change
- Keep the Request as Evidence
- Take in the Request

## apply-an-approved-change

Applies an approved change on its date with the old details kept with
their dates, tells the supplier through the contact on file, and closes
the change with who asked, who confirmed and who approved.

covers:
- Apply the Change on Its Date
- Close the Change on the Record
- Tell the Supplier

## record-what-the-record-taught

Records which details came late, which checks stalled, which duplicates
were caught, the signs of fraud seen and how long each confirmation
took.

covers:
- Record What the Change Taught
- Record What the Setup Taught
