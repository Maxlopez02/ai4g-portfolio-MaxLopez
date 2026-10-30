# Week 5 personal NLP product test

- **Product and feature:** ChatGPT, text summarisation
- **Date tested:** 30 October 2026
- **Text used:** The course resit announcement. It contains the deadline,
  attendance rules, different instructions for Tuesday and Thursday, and the
  separate option to redo a hackathon.
- **Prompt:** “Summarise this announcement in five simple bullets. Keep the
  deadline and clearly separate attendance retakes from optional hackathon
  redos. Do not add information.”

## Short output

1. The deadline for all retakes and redos is Friday 6 November at 23:59.
2. If I missed more than two sessions, I need one attendance retake for each
   extra missed session; two half-attendance marks count as one retake.
3. A missed Tuesday conceptual class needs a 5–10 minute face-to-camera video.
4. A missed Thursday technical class needs GitHub proof of the preparation,
   homework and in-class work.
5. Hackathon redos are optional grade improvements and use the original task
   and partner unless the partner is inactive.

## What I noticed

The summary kept the main distinction that I was confused about: attendance
retakes are linked to missed Tuesday or Thursday sessions, while hackathon
redos are optional. It also kept the exact deadline.

The output left out two useful submission details: the `Resit` folder and the
`redos` tab in the Google Sheet. The likely reason is that I forced a long
announcement into only five bullets, so the model prioritised the rules and
deadline. This is a limitation of summarisation: shorter is easier to read,
but details can disappear. I should check a summary against the source before
using it for a deadline or submission.
