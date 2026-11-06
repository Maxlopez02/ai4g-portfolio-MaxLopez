# Flow State

Flow State is an n8n study planner for adult HBO and WO students who have several assignments due within the same week. A student pastes an unstructured list of tasks and deadlines, enters the time they actually have, and receives a seven-day plan that does not schedule more work than the stated capacity.

The prototype is linked to SDG 3: Good Health and Well-being. It addresses one specific contributor to study stress: making plans that look possible but require more hours than the student has. In the 2025 Dutch student monitor, 53% of participating HBO and WO students reported a lot or very high stress in the previous four weeks. Study was the most frequently reported stress source. Source: [RIVM and Trimbos, Monitor Mentale gezondheid en Middelengebruik Studenten hbo en wo 2025](https://www.rivm.nl/publicaties/monitor-mentale-gezondheid-en-middelengebruik-studenten-hbo-en-wo-2025).

## Final submission files

- [Presentation](Flow-State-Presentation.pptx)
- [Narrated demo](Flow-State-Demo.mp4)
- [Importable n8n workflow](Flow-State-n8n-Workflow.json)
- [Ethical reflection](ETHICAL_REFLECTION.md)

## Intended user

Flow State is for adult HBO and WO students who:

- have several assignments or deadlines in the next seven days;
- can give a rough estimate of their available study time;
- need help turning free-form task notes into a realistic first plan.

It is not intended for minors, crisis support, diagnosis, therapy, or decisions about academic requirements. Students must confirm official deadlines and effort estimates themselves.

## What the user enters

The form asks for:

- first name;
- assignments and deadlines in free text;
- hours available per study day;
- available study days;
- energy level;
- current stress on a 1–10 scale;
- preferred focus-session length.

The form tells users not to enter sensitive medical information.

## How the workflow works

The workflow contains nine connected n8n nodes.

1. **Student Intake Form** collects the planning information.
2. **Validate and Normalise** cleans the fields, checks ranges, and converts the selected weekdays.
3. **Calculate Focus Capacity** reduces raw availability to an estimated focus limit. It reserves break time and applies transparent energy and stress factors.
4. **Prepare AI Extraction** places the student's task text inside a bounded prompt and treats it as untrusted data.
5. **AI Task Interpreter** uses OpenAI `gpt-4o-mini` to convert the free text into structured task JSON: title, due date, estimated hours, whether the estimate was inferred, and confidence.
6. **Verify AI Task JSON** rejects malformed output, checks dates and effort values, limits the task count, and adds warnings for assumptions or missing deadlines.
7. **Schedule Without Overbooking** uses JavaScript rather than the language model to place tasks before their deadlines. It never exceeds the calculated daily capacity and reports work that cannot fit.
8. **Render Student Plan** creates the result page with the schedule and its warnings.
9. **Show Plan to Student** displays the result immediately in the form.

The AI step is necessary because students can describe the same assignment in many ways. A fixed form cannot reliably extract task titles, relative dates, and effort information from that text. The language model does not decide the final schedule. Code verifies its output and enforces the time limits.

## Why a calendar or chatbot is not enough

A calendar requires the student to structure every task and decide how much work belongs on each day. A normal chatbot can interpret free text, but its arithmetic and deadline handling can be inconsistent. Flow State connects free-text extraction with deterministic checks. Its most important output is sometimes a warning that the submitted workload cannot fit.

## Tested scenarios

The prototype was tested through the authenticated n8n Cloud test form.

| Scenario | Input condition | Observed result |
| --- | --- | --- |
| Feasible workload | Two tasks with clear dates and 7 hours of work | 7 hours scheduled and 0 hours left unscheduled |
| Overload | 22 hours of work with insufficient time before the deadlines | 1.25 hours scheduled and 20.75 hours shown as unscheduled |
| Uncertain information | A presentation without a reliable date or effort estimate | No deadline invented; a 1.5-hour provisional estimate was visibly flagged |

These tests show functional behaviour. They do not prove that the tool reduces stress. User testing with students is still needed.

## Run the prototype

1. Import `Flow-State-n8n-Workflow.json` into n8n.
2. Open **04 AI Task Interpreter** and select an OpenAI credential with access to `gpt-4o-mini`.
3. Save the workflow and choose **Execute workflow** to open the test form.
4. Submit a realistic set of assignments and available hours.
5. Check the result page, especially inferred estimates, missing dates, and unscheduled hours.

The current workflow does not send email and does not deliberately append form data to an external spreadsheet. The result appears in the form response.

## Current limitations

- Capacity is an estimate based on self-reported time, energy, and stress.
- Missing effort is provisionally estimated at 1.5 hours and clearly marked as inferred.
- The planner covers seven days only.
- The workflow does not edit a plan after submission or sync with a calendar.
- Provider and n8n retention settings must be reviewed before use with real student data.
- The narrated video documents the tested workflow and outcomes, but it is not a continuous live screen capture.

## Responsible use

Flow State supports planning. It must not be presented as a mental-health assessment or as proof that a student can safely handle a workload. The [ethical reflection](ETHICAL_REFLECTION.md) explains the main risks, the safeguards already implemented, and the next changes required before real deployment.
