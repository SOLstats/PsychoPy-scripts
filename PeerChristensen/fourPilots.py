#Peer Christensen
#September 2017

'''
DESCRIPTION:
    
this script will be used to conduct four quick pilot studies
with auditory stimuli differing either in PITCH, DURATION, LOUDNESS or TEMPORAL LATENCY.
Each experiment contains two warm-up trials (my suggestion) to familiarise participants
with the sound clips, and five clips to be described one-by-one. 
However, this is changed by setting the nStim variable to desired number of stimuli.
The order of the four experiments is randomized.
Press ENTER to go through the stimuli.

#NOTE: Change the set of integers in expOrder to run a specific set or a single experiment
# 1 = Pitch
# 2 = Duration
# 3 = Loudness
# 4 = Latency
'''
from psychopy import core, visual, gui, monitors, sound, event
import random, os
from random import sample
import numpy as np

win = visual.Window([1000,800], monitor="testMonitor",color=(-1,-1,-1))
path="/Users/peerchristensen/Desktop/PsPy/voices/"

#Ordering experiments
expOrder=[1,2,3,4] 
random.shuffle(expOrder)

#Number of stimuli per experiment
nStim=7

#Text
message1= visual.TextStim(win, text="PITCH")
message2= visual.TextStim(win, text="DURATION")
message3= visual.TextStim(win, text="LOUDNESS")
message4= visual.TextStim(win, text="LATENCY")

#Prepare PITCH trials
def prepTrialsPitch():
    stim_sound = os.listdir(path)
    random.shuffle(stim_sound)
    stim_sound=stim_sound[0:nStim]
    dict_s=[]
    i=1
    for s in stim_sound:
        dict_s +=[{i:s}]
        i+=1
    list_sounds=[]
    for i in dict_s:
        list_sounds+=i.values()
    cond1=list_sounds
    conditions=[cond1]
    for i in conditions:
        random.shuffle(i)
    for i in conditions:
        for j in i:
            if "DS" in j:
                i.remove(j)
    return conditions
    
def runExperiments():
    for exp in expOrder:
        if exp == 1:
            print("PITCH")
            message1.draw()
            win.flip()
            core.wait(0.8)
            event.waitKeys(keyList=['return'])
            count=1
            for conditions in prepTrialsPitch():
                for t in conditions:
                    trialNum=visual.TextStim(win=win,text=str(count))
                    trialNum.draw()
                    print("Trial num: " + str(count))
                    win.flip()
                    trial = sound.Sound(value=path+str(t))
                    print(trial)
                    core.wait(0.5)
                    trial.play()
                    core.wait(0.5)
                    win.flip()
                    event.waitKeys(keyList=['return'])
                    count+=1
        elif exp == 2:
            print("DURATION")
            dStim1=list(np.arange(1,5.1,0.5))
            dStim2=list(np.arange(1,5.1,0.5))
            random.shuffle(dStim1)
            random.shuffle(dStim2)
            message2.draw()
            win.flip()
            core.wait(0.8)
            event.waitKeys(keyList=['return'])
            for i in range(1,(nStim+1)):
                trialNum=visual.TextStim(win=win,text=str(i))
                trialNum.draw()
                win.flip()
                stim1=sound.Sound('A',octave=3,sampleRate=44100,secs=dStim1[i],stereo=True)
                stim2=sound.Sound('A',octave=3,sampleRate=44100,secs=dStim2[i],stereo=True)
                core.wait(1)
                stim1.play()
                core.wait(dStim1[i])
                print("Trial num: " + str(i))
                print(dStim1[i])
                core.wait(2)
                stim2.play()
                print(dStim2[i])
                core.wait(0.2)
                win.flip()
                event.waitKeys(keyList=['return'])
        elif exp == 3:
            print("LOUDNESS")
            lStim1=np.arange(0.1,1.1,0.1)
            lStim1 = lStim1.tolist()
            lStim2=np.arange(0.1,1.1,0.1)
            lStim2 = lStim2.tolist()
            random.shuffle(lStim1)
            random.shuffle(lStim2)
            message3.draw()
            win.flip()
            core.wait(0.8)
            event.waitKeys(keyList=['return'])
            for i in range(1,(nStim+1)):
                trialNum=visual.TextStim(win=win,text=str(i))
                trialNum.draw()
                win.flip()
                stim1=sound.Sound('A',octave=3,sampleRate=44100,secs=2,stereo=True)
                stim1.setVolume(lStim1[i])
                stim2=sound.Sound('A',octave=3,sampleRate=44100,secs=2,stereo=True)
                stim2.setVolume(lStim2[i])
                core.wait(1)
                stim1.play()
                core.wait(2)
                print("Trial num: " + str(i))
                print(lStim1[i])
                core.wait(2)
                stim2.play()
                print(lStim2[i])
                core.wait(0.2)
                win.flip()
                event.waitKeys(keyList=['return'])
        else:
            print("LATENCY")
            late=list(np.arange(1,10,1))
            random.shuffle(late)
            message4.draw()
            win.flip()
            core.wait(0.8)
            event.waitKeys(keyList=['return'])
            for i in range(1,(nStim+1)):
                trialNum=visual.TextStim(win=win,text=str(i))
                trialNum.draw()
                win.flip()
                stim=sound.Sound('A',octave=3,sampleRate=44100,secs=1.5,stereo=True)
                core.wait(1)
                stim.play()
                core.wait(1.5)
                print("Trial num: " + str(i))
                print(str(late[i]) + " secs")
                core.wait(late[i])
                stim.play()
                core.wait(0.2)
                win.flip()
                event.waitKeys(keyList=['return'])
        win.close

runExperiments()
core.quit
    

