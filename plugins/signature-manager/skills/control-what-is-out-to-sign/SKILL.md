---
name: control-what-is-out-to-sign
description: Sends the right version to the named signers in the agreed order, such as a supplier agreement or a bank's account and signer forms, files the executed copy with what it rests on, and takes a document back out of signature when it should no longer be out there, such as when the deal is lost. Use it when running `ref/fin/change-a-bank-account-or-signer` and 10 other reference processes.
license: CC-BY-4.0
metadata:
  agent: signature-manager
  agent-version: "1"
---

# Control what is out to sign

## What it does

Sends the right version to the named signers in the agreed order, such
as a supplier agreement or a bank's account and signer forms, files the
executed copy with what it rests on, and takes a document back out of
signature when it should no longer be out there, such as when the deal
is lost. The signing itself stays a human step.

## Where it happens

The agent does this in fifteen activities across eleven reference
processes. Each one names the activity as that process words it.

- **Choose and Engage the Providers**
  - `ref/pc/form-the-fund`, activity 5 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)
- **Execute the Signature**
  - `ref/sls/run-the-close-plan`, activity 15 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Get the Agreement Signed**
  - `ref/fin/choose-a-supplier`, activity 14 -
    [Choose a Supplier](../../../../processes/finance/choose-a-supplier.md)
- **Get the Forms Signed**
  - `ref/fin/change-a-bank-account-or-signer`, activity 10 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Get the Offer Signed**
  - `ref/hr/make-an-offer`, activity 14 -
    [Make an Offer](../../../../processes/human-resources/make-an-offer.md)
- **Send the Subscription Documents**
  - `ref/pc/hold-a-fund-close`, activity 2 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)
- **Sign and Send the Indication**
  - `ref/pc/respond-to-a-sale-process`, activity 16 -
    [Respond to a Sale Process](../../../../processes/private-capital/respond-to-a-sale-process.md)
- **Sign the Adviser's Engagement**
  - `ref/pc/run-a-sale-process`, activity 3 -
    [Run a Sale Process](../../../../processes/private-capital/run-a-sale-process.md)
- **Sign the Agreement**
  - `ref/hr/negotiate-a-separation-agreement`, activity 15 -
    [Negotiate a Separation Agreement](../../../../processes/human-resources/negotiate-a-separation-agreement.md)
- **Sign the Close**
  - `ref/pc/hold-a-fund-close`, activity 10 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)
- **Sign the Closing Documents**
  - `ref/pc/run-the-closing`, activity 10 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)
- **Sign the Confidentiality Agreement**
  - `ref/pc/respond-to-a-sale-process`, activity 6 -
    [Respond to a Sale Process](../../../../processes/private-capital/respond-to-a-sale-process.md)
- **Sign the Formation Documents**
  - `ref/pc/form-the-fund`, activity 15 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)
- **Sign the Sale Agreement**
  - `ref/pc/run-a-sale-process`, activity 15 -
    [Run a Sale Process](../../../../processes/private-capital/run-a-sale-process.md)
- **Stop the Open Work**
  - `ref/sls/record-a-lost-deal`, activity 9 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)

## What to record

Per agreement: the executed document at a version, with each exhibit it
names marked present or missing. The signers on both sides, the
authority each signed under, and the signature date the term runs from.
The buying entity and the selling entity as matched to the entity list,
with the tax and address record for each. Every term off the standard
paper, named as non-standard, with the person who accepted it and the
date. Each promise made during the sale marked binding, carried by a
side letter, or not binding, with the clause behind every binding one.
The signature path as confirmed, and the date and version each document
went out on. What had to be corrected between signature and booking, and
which of it belongs in the next version of the paper. Somebody auditing
a run can say which version was signed, by whom, and what it obliges.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
