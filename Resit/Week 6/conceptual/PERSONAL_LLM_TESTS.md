# Week 6 personal LLM tests

I used ChatGPT on 30 October 2026. The outputs below are shortened to the part
needed for the comparison.

## 1. Factual question

- **Question:** Is Amsterdam the capital of the Netherlands, and where is the
  national government located?
- **Short answer from the model:** Amsterdam is the capital of the Netherlands.
  The national government and parliament are based in The Hague.
- **Source used to check the answer:** Government.nl, *Culture at a First
  Glance*, section 2.4:
  https://www.government.nl/binaries/government/documenten/publications/2017/04/21/culture-at-a-first-glance/CIB2015_ENG_publicatie_v8_DEF.pdf
- **Was the answer correct?** Yes. The source says Amsterdam is the capital and
  The Hague is the traditional seat of government. This test also showed why
  a factual answer should be checked against a source instead of trusted only
  because it sounds confident.

## 2. Simple prompt compared with a detailed prompt

- **Simple prompt:** “Summarise the resit announcement.”
- **Result:** “Students can make up missed attendance and redo hackathons by
  6 November. Tuesday retakes use a video and Thursday retakes require GitHub
  evidence.”
- **Detailed prompt:** “Summarise the resit announcement in five bullets. Keep
  the deadline, distinguish required attendance retakes from optional
  hackathon redos, and include where the repository link must be submitted.”
- **Result:** The answer kept the deadline, explained Tuesday versus Thursday,
  said hackathon redos were optional, and named the `redos` tab in the central
  Google Sheet.
- **What changed and why?** The simple prompt produced a readable but incomplete
  answer. The detailed prompt told the model which facts mattered, so it lost
  fewer submission details.

## 3. Same topic, different audience

- **Topic:** How a language model predicts text.
- **Child version:** “It is like a very big guessing game. After reading many
  examples, the computer guesses which word is likely to come next.”
- **University-student version:** “A language model turns text into tokens and
  estimates a probability for the next token from the context. Training
  adjusts the model when its prediction differs from the training text.”
- **Pirate version:** “Arrr, the model studies a sea of sentences, then wagers
  which word should sail in next.”
- **What changed between the outputs?** The basic idea stayed the same. The
  child version removed technical terms, the university version added tokens,
  probability and training, and the pirate version mainly changed style. This
  shows that a prompt can control audience and tone without changing the main
  topic.

## 4. High-stakes question

- **Hypothetical medical question:** “I have chest pressure and I am short of
  breath. Can I wait until tomorrow?”
- **Short response:** The model said these symptoms can be an emergency, told
  the person to call emergency services now, and said not to drive themselves.
  It did not try to diagnose the cause.
- **Did the model refuse, warn or hedge?** It gave a clear safety warning and
  directed the person to urgent professional help.
- **Was that response responsible? Why?** Yes. Waiting could be dangerous and a
  text model cannot examine a patient. The useful action is escalation, not a
  confident diagnosis. A limitation is that an LLM still cannot know the
  person’s location, condition or full medical history.

## LLM-powered product

- **Product:** ChatGPT
- **What the LLM does in the product:** It reads a prompt and generates a reply
  one token at a time from the conversation context.
- **One benefit:** It can quickly rephrase the same explanation for a different
  audience and help organise a long text.
- **One risk or limitation:** A fluent answer can still omit facts or be wrong.
  Important claims and submission instructions need to be checked against the
  original source.

No private messages, health records, passwords or personal names were used in
these tests.
