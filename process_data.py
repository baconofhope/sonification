import csv
import midiutil
import numpy as np
import math
import random

csv_input = "./china_stats.csv"
midi_output = "china.mid"

def normalize(x):
    return x / x.max(axis=0)

def compose_midi(stats):
    beats_1 = [2, 1, 0.5, 0.25]
    beats_2 = [0.5, 1, 2, 4]

    C_minor_scale_1 = [60, 62, 63, 65, 67, 68, 70]
    C_major_scale = [72, 74, 76, 77, 79, 81, 83]
    C_arpeggio_scale = [72, 76, 79, 84]
    minor_scale = [36, 38, 39, 41, 43, 44, 47]

    volumes_1 = [50, 70, 90, 110]
    volumes_2 = [80, 95, 110, 125]

    measure = 4 #4 beats represents 1 day
    track = 0
    channel = 0
    time = 0
    tempo = 200  # beats per minute
    program = 0 # instrument: piano
    midi_file = midiutil.MIDIFile(1, deinterleave=False, adjust_origin=False)
    midi_file.addTempo(track, time, tempo)
    midi_file.addProgramChange(track, channel, time, program)

    maxs = stats.max(axis=0)
    for row in stats:

        #cases
        cases = row[0]
        cases_quartile = math.ceil(cases/maxs[0]*4) - 1

        if cases <= 0:
            rand_volume = 30 + int(random.gauss((0), (10)))
            rand = random.randint(0, 3)
            note2 = C_major_scale[random.randint(0, 6)]
            midi_file.addNote(track, channel, C_arpeggio_scale[rand], time, 2, rand_volume)
            midi_file.addNote(track, channel, note2, time+measure/2, 2, rand_volume)

        else:
            offset = 0
            while offset < 4:
                length = beats_1[cases_quartile]
                note = C_minor_scale_1[int(cases+1+offset*measure) % 7]
                midi_file.addNote(track, channel, note, time + offset, length, volumes_1[cases_quartile])
                offset += length

        # deaths
        val = row[1]
        quartile = math.ceil(val/maxs[1]*measure) - 1
        note = minor_scale[val % 7]
        note2 = minor_scale[(val+2) % 7]
        offset = 0
        for i in range(0, quartile+1):
            midi_file.addNote(track, channel, note, time + offset, beats_2[quartile], volumes_2[quartile])
            midi_file.addNote(track, channel, note2, time + offset, beats_2[quartile], volumes_2[quartile])
            offset += beats_2[quartile]*4
        time += measure
    save_midi(midi_file)


def save_midi(midi_file):
    filename = midi_output
    with open(filename, 'wb') as output_file:
        midi_file.writeFile(output_file)
        print('midi file saved')

with open(csv_input, 'rt') as csvfile:
    reader = csv.DictReader(csvfile, quotechar='"')
    stats = []
    for row in reader:
        stats.append([int(row["new_cases"]), int(row["new_deaths"])])
    data_array = np.array(stats)
    compose_midi(data_array)
