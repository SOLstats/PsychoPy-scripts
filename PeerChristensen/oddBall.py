# A simple example of an oddball paradigm

# Peer Christensen
# hr.pchristensen@gmail.com

''' 
DESCRIPTION: This script shows how a simple oddball paradigm can be implemented in PsychoPy.
In this case oddball stimuli occur after two or three normal stimuli
'''

import numpy as np

''' UNUSED
stim=list(range(1,21))
odd=list(np.random.choice(2,21))
odd=[x+3 for x in odd]
'''

a=[0,0,1]
b=[0,0,0,1]

odds=list(np.random.choice(2,10)) #generates a random sequence of 0s and 1s. Length = 10
stims=[]
for i in odds:
    if i == 0:
        stims.append(a)
    else:
        stims.append(b)
        
stims=[x for l in stims for x in l]
