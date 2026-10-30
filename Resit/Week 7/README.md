# Week 7 resits

## Conceptual — Computer vision

Prepare and record a 5–10 minute face-to-camera presentation covering:

- [ ] A three-class Teachable Machine image model with at least 30 examples per
  class, a screenshot, testing procedure and one analysed failure.
- [ ] Two sourced computer-vision systems: purpose, beneficiaries, possible
  harms and a responsible-use safeguard.
- [ ] How computers represent images and three preprocessing methods, including
  possible information loss, distortion or bias.
- [ ] How neural networks learn and why image data is challenging.
- [ ] What CNNs are and why they suit image data.
- [ ] Convolution explained step by step with a simple visual or example.
- [ ] One use of a CNN on non-image data and how the data is structured.

## Technical — Computer-vision MVP

Create an individual, reproducible version of the missed group workshop:

- [x] Choose object recognition, landmark detection or segmentation.
- [x] Define a small MVP that helps a real user.
- [x] Use only images that are safe and permitted to publish.
- [x] Record ground-truth answers before evaluating the model.
- [x] Explain the preprocessing pipeline.
- [x] Choose and justify an evaluation metric.
- [x] Demonstrate the working MVP and document where it fails.
- [x] Explain who could be harmed by failures and what safeguard is needed.

Use `technical/Week7_Object_Recognition_Resit.ipynb`. The notebook already
contains the taught workflow and stops if fewer than 10 photos or incomplete
ground truth are supplied; its result and failure sections must come from the
real run.

## DataCamp

- [ ] Image Processing in Python, chapters 1 and 2.
- [ ] Deep Learning for Images with PyTorch, chapter 2 Object Recognition.
- [ ] Deep Learning for Images with PyTorch, chapter 3 Image Segmentation.

## Completion status

The conceptual slide deck is prepared. Brightspace and the official workshop
slides name three starter notebooks, but the files are not published in the
course content. A course-level object-recognition version was therefore
recreated from the official brief. It has now been run on 10 personal photos:
all 7 code cells executed successfully with saved outputs and no errors. The
result was 90% exact-count accuracy and 0.6 mean absolute count error. Max must
finish the Teachable Machine evidence, add DataCamp proof, and record the
conceptual video.
