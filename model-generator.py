#!/usr/bin/python2

import numpy as np
import scipy as sp
from scipy.sparse import lil_matrix


# Function to read input file and increment corresponding elements of the matrix.

def learn(inputdata,spacesize=34*34):
  	old_state = 0 # Too lazy to tell it what to do for the first value it reads. For some reason it seems to be okay even if I do not specify this -- but that would be bad handling of an indefinite edge case

	transprob = np.zeros((spacesize,spacesize))
	
	#transprob = lil_matrix((spacesize,spacesize))
	#transprob.tocsr()

	for curr_state in np.nditer(inputdata):
	  transprob[old_state,curr_state] = transprob[old_state,curr_state] + 1
	  old_state = curr_state

	# Normalizing each row to unity

	for row in transprob:
	  if (sum(row)!=0):
	  	row /= sum(row)
	
	#rowsums = transprob.sum(axis=1)
	#nonzero = rowsums > 0
	#normtransprob = np.empty(transprob)
	#transprob[nonzero] = transprob[nonzero] / rowsums[nonzero,np.newaxis] # Seems to be called broadcasting
	#transprob = normtransprob

	return transprob




# Sparse matrix for storing transition probabilities
space_size = 34*34 # Can be made as an argument to the function later -- hardcoded N 

# Actually readin the data from file
#trainingdata = np.fromfile("digrams.dat",dtype=int,count=-1,sep="\n")

# LEARNING

#learn(trainingdata)
#print transitionprob

# Storing it as a sparse matrix -- ONLY IF THERE IS A NEED
# sparse_transprob = sp.sparse.csr_matrix(transprob)

#  -- TEST CODE -- 
#b = np.random.randint(0,2,10000)
#b = b.astype(int)
#
#np.savetxt('statelist.dat',b,fmt="%5i")
#
#samplemusic = np.fromfile("statelist.dat",dtype=int,count=-1,sep="\n")
#
#execfile("model-generator.py")



