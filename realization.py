#!/usr/bin/python2

import numpy as np
import scipy as sp


# Function to generate a Markov chain realization given a transition matrix and an initial state

def realize(init_state,transprob,spacesize,musiclength):
  cumtransprob = np.cumsum(transprob,axis=1) 
  outputstream = np.zeros(musiclength,dtype=int)
  outputstream[0] = init_state
  curr_state = init_state

  for i in np.arange(1,musiclength):
	r = sp.random.rand()
	#In row = initstate, find the column whose cumulative probability is just less than the uniform random number you generated
	new_state = np.argmax(cumtransprob[curr_state] > r)
	outputstream[i] = new_state
	curr_state = new_state
	
  return outputstream




