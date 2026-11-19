# employee-question-responder

## sort-each-question

Takes in each question, matches the asker to one employee record before
reading anything about a person, and reads whether the question is
personal or sensitive. It passes any that is to the named person for
its subject, with the employee told who has it.

covers:
- Confirm Who Is Asking
- Pass It to a Named Person
- Spot What Is Personal or Sensitive
- Take in the Question

## answer-from-the-library

Reads only the facts that decide which answer applies, matches an
approved answer that rests on the policy version in force, reads it
back against the policy, and answers with the source and its version
inside the promised time. It asks whether the answer settled the
question and closes the question on the record.

covers:
- Answer the Employee
- Check the Question Is Settled
- Close the Question on the Record
- Match an Approved Answer
- Read Only What Decides the Answer
- Read the Answer Against the Policy

## route-records-requests

Recognizes a records request in the help channel, acknowledges it with
its deadline in the approved text, and answers questions about the
answer from the approved text, passing any question about what was
withheld to the privacy lead.

covers:
- Acknowledge the Request
- Answer Questions About the Answer
- Take in the Request
