# -*- coding: utf-8 -*-

# Sound description experiment
#Script by Peer Christensen, spring 2016

'''
DESCRIPTION:
30 clips/trials (incl. 5 warm-up), 2 tones per trial differing in pitch,
Range: C1-C4, key of C
Remember to edit "path" 
'''
from psychopy import core, visual, gui, monitors, sound, event
import random, os
from random import sample

#  VARIABLES
win = visual.Window([1000,800], monitor="testMonitor",color=(-1,-1,-1))
path="/Users/peerchristensen/Desktop/PsPy/voices/"
message1 = visual.TextStim(win, text="Here are first 5 warm-up clips \n\nClick 'Enter' to play the next clip")
message2 = visual.TextStim(win, text="Ready?")
message3 = visual.TextStim(win, text="\n\n\n\n    THE END \n\n  Thank you!")


#PREPARE TRIALS
def prepTrials():
    stim_sound = os.listdir(path)
    dict_s=[]
    i=1
    for s in stim_sound:
        dict_s +=[{i:s}]
        i+=1
    list_sounds=[]
    print dict_s
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
    print conditions
    return conditions

def runExp():
    message1.draw()
    win.flip()
    core.wait(0.8)
    event.waitKeys(keyList=['return'])
    count=0 #a counter for each trial
    for conditions in prepTrials(): #calls prepTrials() and takes the conditions list(s)
        for trial in conditions:
            if count == 5:
                message2.draw()
                win.flip()
                event.waitKeys(keyList=['return'])
                core.wait(0.8)
            trial = sound.Sound(value=path+str(trial))
            core.wait(0.8)
            trial.play()
            win.flip()
            press = event.waitKeys(keyList=['return','space','escape'])
            if press[0] == 'space': #it is mentioned in the instructions that pressing space will replay the stimulus
                core.wait(0.5)
                trial.play()
                core.wait(2)
                count=count
                win.flip()
                event.waitKeys(keyList=['return'])
                core.wait(0.5)
                count+=1
            elif press[0] == 'return':
                core.wait(0.5)
                count+=1
            elif press[0] == 'escape':
                win.close()
                core.quit()
        core.wait(1.5)
    win.flip()
    event.waitKeys(keyList=['return'])
    win.close()   

runExp()
core.quit()
