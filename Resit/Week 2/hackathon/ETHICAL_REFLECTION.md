# Ethical reflection

Flow State works close to a health-related problem because study overload can contribute to stress. The prototype does not measure mental health, diagnose a condition, or decide whether a student should continue working. Its role is limited to making workload assumptions visible and showing when a seven-day plan does not fit.

## Incorrect deadlines or effort estimates

The language model may misunderstand a relative date or invent information that was not supplied. A wrong date could cause a student to miss coursework. An effort estimate that is too low could create false confidence and increase pressure later.

The prompt requires unknown dates to remain `null` and marks estimated effort as inferred. The next code node parses the response, validates the date format, limits effort values, and adds a visible warning when a deadline or estimate is uncertain. The student still has to compare the plan with the official course information. A future version should let the student edit every extracted task before scheduling starts.

## Overbooking and false reassurance

A planner can cause harm if it fills every available hour or quietly places work after a deadline. That outcome could make an already stressed student feel personally responsible for an impossible plan.

Flow State separates interpretation from scheduling. The language model extracts task information, but JavaScript calculates capacity and schedules the work. The calculation reserves breaks, reduces capacity when the user reports low energy or high stress, and caps focus time. The scheduling node never exceeds the daily limit. Work that cannot fit before its deadline remains unscheduled and appears as a warning. The interface does not promise completion or stress reduction.

The capacity formula is still a rough heuristic, not a scientific measure of what a person can manage. User research is needed to check whether its assumptions are understandable and whether the warnings help rather than discourage students.

## Sensitive information and privacy

Assignment text could contain names, health information, grades, or private circumstances. Sending unnecessary personal data to an AI provider would create privacy and confidentiality risks.

The form asks users not to enter medical details. The AI receives the assignment text and planning date, but it does not need the student's name or stress score to extract tasks. The current workflow does not send email and does not deliberately write submissions to an external spreadsheet. Before any real deployment, the team must document n8n and OpenAI retention settings, define a deletion period, restrict workflow access, and provide a short consent and privacy notice. Sensitive fields should be removed before the model call rather than relying only on instructions to the user.

## Prompt injection and malformed AI output

A student could paste text that looks like an instruction to the model. The model could also return invalid JSON. Either problem could change the extracted tasks or stop the workflow.

The prompt places student text inside explicit delimiters and states that it is untrusted data rather than an instruction. The verification node accepts only the expected fields, checks values, limits the number of tasks to twelve, and removes unsafe title characters. If no valid tasks remain, the workflow uses a clearly labelled placeholder and warns the student. A stronger version should use schema-constrained model output and record validation failures without storing the student's full text.

## Health boundary and high-stress input

The stress field could make the tool look like a clinical assessment even though the number is only used to reduce planning capacity. A student in distress might rely on the plan instead of seeking human help.

The form and result page state that Flow State is a planning aid, not a medical service. The workflow does not diagnose or generate treatment advice. When a student enters a stress level of eight or higher, the result suggests contacting a trusted person or student counsellor. It does not attempt emergency triage. The safest production design would either remove the stress field or explain its limited purpose next to the question and provide institution-approved support information.

## System failure and unequal usefulness

If n8n or the AI provider is unavailable, the student may receive no plan when a deadline is close. The current form also assumes that the user can estimate available time and interpret a text-heavy result. This may work less well for students with limited language proficiency, attention difficulties, irregular care or work duties, or inaccessible devices.

Students must keep official deadlines in their normal course system and should not depend on Flow State as their only record. A deployed version needs a clear failure message, an option to retry without another paid model call, keyboard and screen-reader testing, and user testing with students who have different schedules and accessibility needs.

## What must happen before deployment

The prototype has technical safeguards, but it has not established real-world benefit. Before deployment, the team should:

1. let users confirm and edit extracted tasks before scheduling;
2. test the wording and capacity assumptions with students;
3. publish a privacy notice and retention policy;
4. verify accessibility and failure handling;
5. measure whether students understand overload more clearly without claiming a mental-health outcome.

These steps keep the project within its intended scope: supporting a planning decision while leaving academic and health decisions with the student and relevant professionals.
