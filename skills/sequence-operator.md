# sequence-operator

## plan-the-touches-and-the-cadence

Takes the signed list in and splits it into groups that get different
wording. Writes the touches for each group and each position, and sets
how many go out, how far apart, on which days, and when the sequence
gives up on somebody who never answers.

covers:
- Take in the List
- Split the List into Groups
- Write the Touches
- Set the Cadence

## send-the-touches

Prepares the sending, then works the cadence across mail, phone and
social on the day each touch is due, inside the cap each channel sets.

covers:
- Prepare the Sending
- Send the First Touch
- Make the Calls
- Run the Social Touches

## keep-the-sending-healthy

Reads the bounces, complaints and blocks every day the sequence is live
against the thresholds set for them, and stops the sending when a
threshold is passed.

covers:
- Keep the Sending Healthy

## answer-what-comes-back

Reads every reply the same day and sorts it into wants a conversation,
not now, wrong person or stop. A reply stops the sequence on every
channel before the next scheduled send, and a stop suppresses the person
everywhere and not only where they said it. A reply that wants a
conversation goes on with the whole thread attached.

covers:
- Watch for Replies
- Stop on a Reply
- Handle Opt-Outs
- Hand over the Positive Replies

## stop-and-close-a-sequence

Stops the touches the moment a meeting is confirmed, and does not start
them again. Closes the sequence at the end, cancels the touches still
scheduled, and reports what was sent, what came back and what the run
taught.

covers:
- Stop the Outbound Touches
- Close the Sequence
- Report and Record What Was Learned

## ask-for-an-introduction

Writes the note an introducer can send as it stands, gets it to them
with a date, and sends one reminder before the referral is let go.

covers:
- Write the Introduction
- Ask for the Introduction
- Wait and Chase Once
