#!/usr/bin/env python2

# 
# Given MIDI file, with some essential details, write out the unigram state transitions
#

# Essential constants. See appropriate README to figure out how to adjust these
FILE_NAME = "unigrams.dat";
N_UNIGRAMS = 34;
N_GRAMS = 2;

# Compute state-space size
N_STATES = N_UNIGRAMS**N_GRAMS;

# print "Number of states:" + str(N_STATES)

# Create state variable
state = 0;
count = 0;

# Read file
f = open( FILE_NAME, 'r' );

for line in f:
    unigram = int( line );
    count += 1;
    state = (state * N_UNIGRAMS + unigram) % N_STATES; # Like a base-N_UNIGRAMS shift register with N_GRAMS memory locations
    if count % N_GRAMS == 0:
        print state
        count = 0

