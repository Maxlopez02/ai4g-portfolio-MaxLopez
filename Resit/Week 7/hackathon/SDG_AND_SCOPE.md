# K2 and K3 evidence: SDG relevance and MVP scope

## K2: SDG 15, target 15.8

UN target 15.8 calls for measures that reduce the impact of invasive alien
species on land and water ecosystems and support control of priority species.
The Dutch NVWA reports that giant hogweed can form dense vegetation that fully
displaces other plant species and can be confused with native common hogweed.

Hogweed Guard NL supports that target through a limited decision-support chain:

1. A Dutch nature volunteer sees a plant that resembles hogweed.
2. The AI model compares it with two native look-alikes.
3. The app returns a cautious screening result or withholds the answer.
4. The volunteer records the location and asks a site manager or species expert
   to confirm the plant before any action.

The intended benefit is earlier, safer expert reporting of a possible invasive
plant while reducing avoidable removal of native look-alikes. The MVP does not
claim that image classification alone controls invasive species.

## K3: exact MVP boundary

| Included in the resit | Explicitly excluded |
| --- | --- |
| One primary user: Dutch nature volunteer | General public plant-identification app |
| One input: a single plant photograph | Live camera, map, GPS or batch upload |
| Three classes: giant hogweed, common hogweed, cow parsley | Every Dutch plant or every hogweed species |
| One outcome: class score or “uncertain” | Confirmed botanical identification |
| One next step: request expert confirmation | Removal, medical or legal advice |
| Streamlit interface and Roboflow Workflow | Accounts, notifications and production deployment |

This is intentionally a small screening prototype. Success means the complete
photo-to-model-to-cautious-result flow works and the limitations stay visible.

## Sources

- UN Goal 15 and target 15.8: https://sdgs.un.org/goals/goal15
- NVWA giant hogweed factsheet: https://www.nvwa.nl/documenten/planten-in-de-natuur/exoten/risicobeoordelingen/factsheet-reuzenberenklauw
