#!/usr/bin/env python2

#
# Unpack n-grams into unigrams
#

import sys

# Essential constants. See appropriate README to figure out how to adjust these
FILE_NAME = sys.argv[1];
N_UNIGRAMS = 34;
N_GRAMS = 2;

# Compute state-space size
N_STATES = N_UNIGRAMS**N_GRAMS;

# Read file
f = open( FILE_NAME, 'r' );

for line in f:
    state = int( line );
    unigrams = list(); # Empty list of unigrams
    for x in (0, N_GRAMS):  # Unpack in the reverse order
        unigram = state % N_UNIGRAMS;
        state = (state - unigram)/N_UNIGRAMS;
        unigrams.append( unigram );
    unigrams.reverse(); # Reverse the order to get the correct order
    for unigram in unigrams: # Print
        print unigram;

        
