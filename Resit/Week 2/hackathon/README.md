# Flow State — Hackathon 2 redo

Flow State is a small n8n tool for students who have several deadlines in one week and do not know how to divide the work. The student types the assignments in their own words and says when they can study. The workflow turns that information into a seven-day plan and, importantly, says when the work simply does not fit.

I rebuilt the project after the first assessment. The earlier version relied too much on one AI prompt and did not automate enough of the actual planning process. In this version, AI has one limited job: reading messy task descriptions. Normal code checks the AI output, calculates the available time and builds the schedule.

## Submission

- [Presentation](Flow-State-Presentation.pptx)
- [Narrated demo](Flow-State-Demo.mp4)
- [n8n workflow](Flow-State-n8n-Workflow.json)
- [Ethical reflection](ETHICAL_REFLECTION.md)

## The problem I chose

This is meant for adult HBO and WO students who have several assignments due soon. A calendar can store deadlines, but it still leaves the student to decide what to do each day. A chatbot can suggest a plan, but it may make mistakes with dates or quietly schedule more hours than are available.

Flow State combines the useful part of AI—understanding loosely written text—with fixed scheduling rules. It is connected to SDG 3, Good Health and Well-being, because unrealistic planning can add to study stress. The 2025 Dutch student monitor reported that 53% of participating HBO and WO students experienced a lot or very high stress, with study named most often as the source. [RIVM and Trimbos report](https://www.rivm.nl/publicaties/monitor-mentale-gezondheid-en-middelengebruik-studenten-hbo-en-wo-2025).

I am not claiming that this prototype improves mental health. It only tackles one practical part of the problem: noticing an unrealistic week before the student commits to it.

## What happens after the form is submitted

1. The workflow checks and cleans the form answers.
2. It calculates a rough daily focus limit from the student's available hours, study days, energy and preferred session length.
3. OpenAI extracts task names, deadlines and estimated effort from the student's text.
4. A separate code step checks the AI response. Missing dates and guessed effort stay visible instead of being presented as facts.
5. The scheduler divides the tasks over the next seven days without exceeding the calculated daily limit.
6. The student sees the plan, warnings and any work that could not be scheduled before its deadline.

This is more than displaying an AI answer. The model does not control the schedule, and its answer is checked before the workflow uses it.

## What I tested

I ran three different inputs through the n8n test form:

| Test | Result |
| --- | --- |
| Two clear tasks totalling 7 hours | All 7 hours were scheduled. |
| A 22-hour workload with very little available time | Only 1.25 hours fitted; the other 20.75 hours were shown as unscheduled. |
| A task without a clear date or time estimate | No deadline was invented. The temporary 1.5-hour estimate was marked as a guess. |

These tests show that the main workflow works. They do not replace testing with actual students.

## Try it in n8n

1. Import `Flow-State-n8n-Workflow.json`.
2. Select an OpenAI credential in the node called **04 AI Task Interpreter**.
3. Run the workflow and open the test form.
4. Enter a few real or fictional assignments and the time available.
5. Check the plan, especially the warnings and unscheduled hours.

The plan currently appears on the result page. It is not emailed or saved to a spreadsheet.

## Limits I am aware of

- The capacity calculation is a rough estimate based on the student's own answers.
- The tool covers only the next seven days.
- The student cannot yet correct the extracted tasks before the schedule is made.
- It does not connect to a school calendar or learning platform.
- The demo shows the tested results, but it is not one continuous live screen recording.

The [ethical reflection](ETHICAL_REFLECTION.md) explains the risks and the changes I would make before using this with real students.
