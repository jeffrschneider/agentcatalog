# billing-administrator

## build-the-invoice

Opens the invoice on its billing date, reads the booking at its version,
checks that the usage reading is complete for a customer billed on use,
builds each line from the booking and the usage, and applies the
indirect tax each line carries.

covers:
- Apply the Indirect Tax
- Build the Invoice Lines
- Check the Usage Reading Is Complete
- Open the Invoice
- Supply the Booking at Its Version

## check-the-invoice

Checks the invoice for every field the local invoice rules require, and
traces every line to the booking with the total set beside the last
invoice on the same agreement.

covers:
- Check What the Invoice Must Show
- Check the Invoice Against the Booking

## issue-and-send

Numbers and issues the invoice in its series, sends it on its date in
the form the customer asked for, confirms that the customer received it,
and puts a rejected invoice right as the billing lead decides.

covers:
- Confirm the Customer Received It
- Correct a Rejected Invoice
- Number and Issue the Invoice
- Send the Invoice in the Customer's Form

## pass-the-billing-on

Passes each issued invoice to receivables and the ledger, and gives the
period's invoices and credit notes to revenue accounting.

covers:
- Pass What Was Billed On
- Take In What Was Billed

## correct-a-disputed-invoice

Recomputes the disputed lines on their own from the same records, drafts
the credit note or the replacement for exactly what was decided, and
issues it once the named approver has approved it. The same work issues
the credit note for a refund or a goodwill credit a named person in
support decided, once that person has approved it.

covers:
- Draft the Credit Note or Replacement
- Issue the Credit Note and Any Replacement
- Recompute the Invoice Independently
- Draft the Credit Note
- Issue the Credit Note

## learn-from-each-invoice

Feeds the cause of each dispute back to the booking, the meter, the
template or the price, and records which invoices were late, rejected or
reviewed and what changes before the next run.

covers:
- Feed the Cause Back
- Record What the Run Taught
