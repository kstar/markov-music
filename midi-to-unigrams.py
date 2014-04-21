#!/usr/bin/env python2

# 
# Given MIDI file, with some essential details, write out the unigram state transitions
#

# Essential constants. See appropriate README to figure out how to adjust these

import midi
import re

FILE_NAME = "/tmp/bwv1041a-solo.mid";
BASE_TICK = 60;
N_NOTES = 32;
LOWEST_NOTE = 56;

# Initializations
current_state = 0;

# Open the MIDI file
pattern = midi.read_midifile( FILE_NAME );


# Read the file for note on and off events
for line in pattern:
    for event in line:
        if type(event) == midi.events.NoteOffEvent or type(event) == midi.events.NoteOnEvent:

            # Write the state enough number of times
            for x in range(0, int( round( float(event.tick) / float(BASE_TICK) ) ) ):
                print current_state

            if type(event) == midi.events.NoteOffEvent or event.get_velocity() <= 0:
                if event.get_pitch() == current_state + LOWEST_NOTE - 1:
                    current_state = 0;
            else:
                current_state = event.get_pitch() - LOWEST_NOTE + 1;
