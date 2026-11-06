# Ethical reflection

At first, I saw Flow State mainly as a practical planning tool. While rebuilding it, I realised that a bad plan can make the exact problem worse. If the tool misunderstands a deadline or makes an impossible week look manageable, a student could trust it and end up with more stress.

## The AI can be wrong

The AI reads the student's task description. It may misunderstand a phrase such as “next Friday”, guess how long an assignment takes or return broken data. A wrong deadline is not a harmless mistake if a student relies on it.

I therefore did not let the AI create the final schedule. Its output goes through a separate check that validates dates and effort values. A missing deadline stays missing, and a guessed time estimate is labelled as a guess. The result also tells the student to compare everything with the official course information.

This reduces the risk, but it does not remove it. My next improvement would be a confirmation screen where the student can correct every task before the schedule is calculated.

## An “efficient” plan can still be unhealthy

It would have been easy to fill every free hour with study blocks. I decided not to do that. The workflow reserves break time, caps the daily focus time and lowers the estimate when the student reports low energy or high stress. If the work does not fit, it stays unscheduled and the student sees a warning.

That warning matters more than producing a full-looking timetable. The student should not be blamed for failing to complete a workload that was unrealistic from the start.

The calculation is still only a rule I designed; it is not a scientific measurement of someone's capacity. I would need feedback from students before knowing whether the limits and warnings actually feel useful.

## Privacy

Students may type names, grades or personal circumstances into the task box, even when the form asks them not to include medical information. Sending that text to an AI provider creates a privacy risk.

The workflow only needs the task text and planning date for the AI step. It does not deliberately save submissions to a spreadsheet or send them by email. Before real use, I would need to check the retention settings of both n8n and OpenAI, set a deletion period, limit who can access the workflow and add a clear privacy notice. I would also remove unnecessary personal fields before the model call instead of relying only on a warning in the form.

## The stress question

I included a 1–10 stress question to make the plan less demanding when someone already feels overloaded. The risk is that this looks like a mental-health test. It is not one, and the workflow cannot judge whether somebody is safe or needs treatment.

The result calls Flow State a planning aid and not a medical service. A score of eight or higher adds a suggestion to speak with a trusted person or student counsellor. If this were developed further, I would consider removing the question or explaining much more clearly why it is asked and how it affects the calculation.

## Who might be left out

The current result is text-heavy and assumes that students can estimate their own available time. That may be harder for people with attention difficulties, limited English, changing work shifts or caring responsibilities. The workflow also depends on n8n and the AI provider being available.

Before offering it to real students, I would test it with people who have different schedules and accessibility needs. It also needs keyboard and screen-reader testing, a clear error message and a way to try again if the AI call fails.

## My conclusion

Flow State should help a student notice an overloaded week; it should not decide what the student is capable of. I think separating the AI interpretation from the rule-based scheduler was the right choice. However, I would not present this prototype as proven or ready for real student data. It still needs an edit-and-confirm step, privacy rules, accessibility testing and feedback from students themselves.
