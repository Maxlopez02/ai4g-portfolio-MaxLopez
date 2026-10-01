# Workflow demo script

The two workflow screenshots in the original deck were placed under the wrong headings. Use the text-to-image screenshot on slide 3 and the image-to-video screenshot on slide 4.

## Slide 3: Workflow 1, text to image

**Narration, about 27 seconds**

> This workflow creates the key frame that anchors every shot. Juggernaut XL generates the image from a positive prompt, while the negative prompt removes people, text, logos, deformation, and blur. ControlNet uses the loaded reference image to hold the window geometry in place. The KSampler runs for 30 steps with CFG five, a Karras schedule, and 0.5 denoise. Changing the environment prompt creates a new era without losing the same viewpoint.

**What to point at**

1. Positive and negative prompt nodes on the left.
2. Checkpoint loader and ControlNet connection.
3. KSampler settings in the centre.
4. Decoded preview on the right.

## Slide 4: Workflow 2, image to video

**Narration, about 27 seconds**

> This workflow turns a generated still into a five-second clip. The input image is resized to half a megapixel, and its width and height are passed into the MiniMax H3 image-to-video node. The prompt asks for subtle motion outside the window while the interior stays fixed. We use the same image as the first frame, run nine turbo steps, and save the result as an MP4. This preserves the window composition while animating smoke, rain, stars, or debris.

**What to point at**

1. Input image and resize nodes on the left.
2. Width and height connections entering MiniMax H3.
3. Motion prompt and five-second duration.
4. Nine turbo steps and the save-video node.

## Recording note

The included MP3 files use a system voice as a timing draft. For the most natural presentation, record these scripts once in your own voice and replace the draft files before uploading them to Drive.
