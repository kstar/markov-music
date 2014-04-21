# Simple markov music generator

1. Read a MIDI file and convert that to an internal representation.

2. Model as a Markov process: Populate matrix of transition probabilities.

3. Use the learned model to generate a music sequence based on some initial state.


# Typical paradigm of operations

1. Prune the MIDI file to contain a single channel with no
   polyphony. Use various commands (as seen in Akarsh's scratch file)
   to identify various aspects of the MIDI file. Set these parameters
   in _all_ the python scripts.

2. Run midi-to-unigrams.py to generate a list of unigrams from the
   MIDI file. This program dumps to stdout, so you might want to
   redirect the output into a file. The input MIDI file is set in the
   python script.

3. Run unigrams-to-ngrams.py to generate a list of n-grams from the
   MIDI file. The input file is specified in the python script. The
   program dumps to stdout, so you might want to redirect the output
   into a file. The 'n' of n-grams is specified inside the file. Last
   few notes may be clipped, especially for large 'n'.

4. Run the appropriate scripts to generate the Markov model (TODO:
   Fill in details).

5. Run the appropriate scripts to generate random realizations of the
   Markov model (TODO: Fill in the details).

6. Convert the n-grams from the Markov model back into unigrams using
   ngrams-to-unigrams.py. This script takes the input file on the
   command line (as the first argument), and outputs to stdout.

7. Resynthesize a MIDI file from the unigrams. The script takes both
   the input file (first argument) containing unigrams and the output
   MIDI file (second argument) as command-line arguments. Tempo,
   instrument, transpose and other settings are specified in the
   python script.
