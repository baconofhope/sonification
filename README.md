# Data sonification

Similarly to how data visualization maps a dataset to visual components, sonification maps data to sounds. Data sonification has become a popular method in data journalism, especially for the podcast format (see [example](https://www.revealnews.org/article/listen-to-the-music-of-seismic-activity-in-oklahoma/) from Reveal).

To learn more about data sonification I recommend this [podcast episode with Hannah Davis](https://datastori.es/turning-data-into-sound-with-hannah-davis).

# Sonification based on COVID-19 data

In this piece I mapped basic data from the COVID-19 epidemic. When the epidemic began, those of us lucky to be away from the epicenters of the disease nervously tracked its progress via the basic statistics. The second-hand experience of the pandemic via statistics is what I tried to capture.

I want to emphasize that this project is not meant to capture the tragedy or magnitude of the epidemic itself.  Furthermore, I feel conflicted about whether it is even appropriate to apply sonification to data that represents human lives. The number of deaths is not just a number - many people spent their last days in panic and disorder, without their family by their sides. 

This piano piece uses data from China and spans the beginning of the pandemic to its initial relapse in May. Listen to the [sample piece](https://raw.githubusercontent.com/baconofhope/sonification/master/china.mp3). 

# Implementation
## Mapping

In the piece, I wanted to capture the feeling of unease and anxiety as the magnitude of the pandemic grew and then easing into relief as the numbers fell.  The date, number of cases, and number of deaths were mapped to notes on a piano.

The piece was written with a time signature of 4/4, with each day in time corresponding to one measure. The number of cases was mapped to the right-hand part and the number of deaths to the left-hand part. The magnitude of the number determined the volume and tempo - larger numbers correspond to higher volume and a faster tempo. The value of the number was used to select a note from the C-minor scale. For dates when there were no new cases, notes were generated at random from the C-major scale. 


## Technical details
I used Hannah Davis's [workshop project](https://github.com/handav/workshop/blob/master/python/Python3/Py3_ufo_by_sighting.py) as a starting point because  it provided a framework for sonification with Python and MIDI.
Python was used to process the data and map each data point into a series of notes. The library Midiutil was used to generate a MIDI file, which was then converted into a mp3 using GarageBand.

# Future work
I am working on a visual component to add to the piece.  
