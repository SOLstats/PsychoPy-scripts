from psychopy import core, visual, gui, monitors, sound, event
import random, os
from random import sample
import numpy as np

win= visual.Window([1000,800], monitor="testMonitor",color=(-1,-1,-1))

durations=[]
for i in np.arange(1,5.1,0.5):
    durations.append(i)
random.shuffle(durations)

durations2=[]
for i in np.arange(1,5.1,0.5):
    durations2.append(i)
random.shuffle(durations2)

def runExp():
    event.waitKeys(keyList=['return'])
    core.wait(0.6)
    for i in range(0,len(durations)):
        trialNum=visual.TextStim(win=win,text=str(i+1))
        trialNum.draw()
        win.flip()
        stim1=sound.Sound('A',octave=3,sampleRate=44100,secs=durations[i],stereo=True)
        stim2=sound.Sound('A',octave=3,sampleRate=44100,secs=durations2[i],stereo=True)
        core.wait(1)
        stim1.play()
        core.wait(durations[i])
        print("Trial num: " + str(i+1))
        print(durations[i])
        core.wait(2)
        stim2.play()
        print(durations2[i])
        core.wait(0.2)
        win.flip()
        event.waitKeys(keyList=['return'])

runExp()
win.close()
core.quit()