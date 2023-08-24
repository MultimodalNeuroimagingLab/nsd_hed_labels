# nsd_hed_labels
This repository contains [Hierarchical Event Descriptors (HED)](https://www.hedtags.org/) labels of 1015 images from the [Natural Scenes Dataset (NSD)](https://naturalscenesdataset.org/) images. This is work in progress...

## Read the Docs 
[https://nsd-hed-labels.readthedocs.io/en/latest/](https://nsd-hed-labels.readthedocs.io/en/latest/)

# Images
1000 images and their annotations are included in the shared1000_HED.tsv. An additional 15 images and their annotations are included in notShown_HED.tsv. The column titled nsd_id corresponds to the ID of the image as seen in the NSD. The cocoId column corresponds to the indentifier in [COCO](https://cocodataset.org/#home) (note: the images used for NSD and these annotations may be a cropped version of the COCO image). Images are shown to participants with a red fixation dot in the center of the image.

# HED tagging
All tags are HED validated and are from the standard schema. Both short-form and long-form annotations are included.

## Tagging specifics
### The following extensions were used throughout the tags (and passed HED validation):
- Natural-feature/Sky
- Natural-feature/Ocean
- Action/Ride
- Man-made-object/Musical-instrument
- Man-made-object/Toy
- Terrain/Sand
- Agent-trait/
  - Newborn (birth to 1 month)
  - Infant (1 month to 1 year)
  - Child (1 year through 12 years)
  - Adolescent (13 years through 17 years)
  - Adult (18 years or older)
  - Older-adult (65 and older)
  
### Foreground and background
Annotations are grouped into Foreground-view and Background-view sections for all images. Counts and agents are only considered in the Foreground-view.

### Word
[5 degrees of the visual field is the maximum area in which we can read and comprehend words.](https://doi.org/10.1101/2021.09.14.460238) The Word tag was reserved for images that contained readable words within 5 degrees of the fixation point.

### Numerosity/Count
Tags only in the foreground of the image include a count and do not specify numbers higher than [4 which is the limit to fast numerosity judgments.](https://doi.org/10.1068/p050327)

### Faces
The Face tag is always accompanied by an Away-from tag (side-profile) or a Towards tag (full face) as measures of how prominent a face is.

### Agents
Agent tags (Human-agent and Animal-agent) are used in addition to their Item tags (Human and Animal) when there is evidence of an active motion within the image. Good examples of this are legs in an active walking/running motion, water spray from a surfboard to show it is moving through the water, and snow spray from skis to show movement through the snow.

# Contributors (alphabetically)
If you make substantial changes to this repository, please also feel free to add your name as a contributor
- Tal Pal Attia
- Dora Hermes
- Claire Holmes 
