#!/usr/bin/env python2

# 
# Given unigrams, with some essential details, write a MIDI file containing the music
#
# Usage: <command> <input (unigrams) file> <output (MIDI) file>

import midi
import sys

# Essential constants. See appropriate README to figure out how to adjust these
INPUT_FILE = sys.argv[1];
OUTPUT_FILE = sys.argv[2];
BPM = 93; # Tempo in BPM
LOWEST_NOTE = 56; # Decide how much transpose
INSTRUMENT = 40; # Choose the instrument rendering the music
BASE_TICK = 25;

unigrams = open( INPUT_FILE, "r" );

prev_unigram = 0; # No sound to start with
tick_count = 0;

pattern = midi.Pattern();

track = midi.Track();
pattern.append( track );

set_instrument_event = midi.ProgramChangeEvent();
set_instrument_event.set_value( INSTRUMENT );
track.append( set_instrument_event );

set_tempo_event = midi.SetTempoEvent();
set_tempo_event.set_bpm( BPM );
track.append( set_tempo_event );

for unigram_string in unigrams:
    tick_count = tick_count + 1;
    unigram = int( unigram_string );
    if unigram != prev_unigram:
        note = unigram + ( LOWEST_NOTE - 1 );
        previous_note = prev_unigram + ( LOWEST_NOTE - 1 );

        if prev_unigram != 0: # First turn off any notes that are playing already
            event = midi.NoteOffEvent( tick = tick_count * BASE_TICK, velocity = 0, pitch = previous_note );
            track.append( event );
            tick_count = 0;

        if unigram != 0: # We have a new note, so play it
            event = midi.NoteOnEvent( tick = tick_count * BASE_TICK, velocity = 120, pitch = note );
            track.append( event );
            tick_count = 0;

    prev_unigram = unigram


eot = midi.EndOfTrackEvent( tick = 1 );
track.append( eot );
midi.write_midifile( OUTPUT_FILE, pattern );
