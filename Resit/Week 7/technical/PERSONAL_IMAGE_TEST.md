# Week 7 starter-notebook evidence

The official slides name three starter notebooks, but the files were not
available in Brightspace when checked on 30 October 2026. The recreated
course-level notebook therefore follows the same object-recognition brief.

Complete after adding your own images:

- Technique chosen: Object recognition
- User and small MVP goal: Count everyday reusable drink bottles in a small
  set of photos, so a student event organiser can estimate how many bottles
  are already in use before providing disposable cups.
- At least 10 permitted photos taken by me: Yes — ten photos, with no
  recognisable people.
- Image filenames or folder: `week7_photos/`
- Ground-truth labels written before running the model: Yes — seven images
  contain one bottle and three contain zero bottles. The counts were entered
  in the notebook before the model was run.
- Evaluation metric: Mean absolute count error (MAE), supported by exact-count
  accuracy.
- Model result and score: Mean absolute count error 0.6 bottles per photo;
  exact-count accuracy 90%; 7 true bottles and 13 predicted bottles in total.
- One real failure: `one_bottle_01.png` contained one bottle, but the model
  predicted seven.
- Likely reason: The real bottle was detected, but several narrow containers
  and dark vertical objects in the kitchen background were also marked as
  bottles, creating six false positives.
- Who could be harmed by this type of failure? An event organiser could trust
  the overcount and provide too few drinking options. The same error pattern
  would be more serious in a safety or medical setting.
- Safeguard or human check: Show the marked image and confidence values, let a
  person correct the count, and test more rooms, lighting conditions and
  bottle types before wider use.

Only commit photos that are safe and permitted to publish.
