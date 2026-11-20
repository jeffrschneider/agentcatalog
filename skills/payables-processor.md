# payables-processor

## check-a-supplier-invoice

Captures every field of an invoice, checks the supplier's record and
bank details, looks for a duplicate, reads the invoice against the local
invoice rules, finds its purchase order, matches it to the order and the
receipt, and asks the supplier for a correction when it is wrong.

covers:
- Ask the Supplier for a Correction
- Capture the Invoice
- Check What the Invoice Must Show
- Check for a Duplicate
- Check the Supplier Record
- Find the Purchase Order
- Match the Invoice

## code-and-post

Codes each invoice and each approved claim to its account, cost center,
tax code and period, marks each invoice ready to pay with its due date
and the approval behind it, and posts it to the ledger.

covers:
- Code the Claim to the Ledger
- Code the Invoice
- Mark the Invoice Ready to Pay
- Post the Invoice to the Ledger

## prepare-the-payment-run

Opens each payment run, gathers the approved items that fall due and the
credits owed, holds back each item that cannot be paid with its reason,
proposes the run with the discounts worth taking, and builds the payment
file from the approved run to verified details.

covers:
- Build the Payment File
- Gather the Items Due
- Hold What Cannot Be Paid
- Open the Payment Run
- Propose the Claim for Payment
- Propose the Run

## close-out-each-payment

Sends each payee its remittance advice, records the payments in the
ledger, passes any part of a claim treated as pay to payroll before its
cutoff, and confirms each employee's payment against the bank's report.

covers:
- Confirm the Employee Was Paid
- Pass the Part Treated as Pay to Payroll
- Record the Payments in the Ledger
- Send the Remittance Advice

## keep-the-evidence

Keeps each invoice, each receipt and each approval for the period the
local retention rule sets, marked paid, duplicate, returned or refused.

covers:
- Keep the Invoice
- Keep the Receipts

## report-what-is-owed

Gives the cash forecast each approved invoice and open order by the week
it falls due, and the daily cash position the payments due out that day
with the approval behind each.

covers:
- Gather What the Company Owes
- List the Payments Due Today

## record-what-payables-taught

Records the cause of each invoice exception, the items held from each
run, the payments returned and the discounts missed, and what the next
invoice or run does differently.

covers:
- Record What the Invoice Taught
- Record What the Run Taught
