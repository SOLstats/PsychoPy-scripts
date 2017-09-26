# -*- coding: utf-8 -*-

# Sound description experiment
#Script by Peer Christensen, spring 2016

'''
DESCRIPTION:
This script is intended to present fully randomized auditory stimuli in two rounds.
30 clips/trials (incl. 5 warm-up), 2 tones per trial differing in pitch,
Range: C1-C4, key of C
Participant info and stimulus list are logged.
Edit "path" and "s_path" variables for each system
'''
from psychopy import core, visual, gui, monitors, sound, event
import random, os
from random import sample

#  VARIABLES
win = visual.Window([1000,800], monitor="testMonitor",color=(-1,-1,-1))
path='/Users/peerchristensen/Desktop/PsychoPy/voices/' 
message1 = visual.TextStim(win, text=u"H\u00E4r kommer 5 exempel \n\nKlicka 'Enter' mellan varje")
message2 = visual.TextStim(win, text=u"\n\n\n\n\u00C4r ni redo?")
message3 = visual.TextStim(win, text=u"\n\n\n\n    slut på experimentet \n\n  Tack f\u00F6r er deltagande!")

#DIALOG
info = {'subject':''}
if not gui.DlgFromDict(info, order=['subject']).OK:
    core.quit()

#DATAFILE
s_path = '/Users/peerchristensen/Desktop/PsychoPy/logs/'
datafile = open(s_path+str(info['subject']), 'a')
datafile.write(str([info])+'\n')

#PREPARE TRIALSqq
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
            row= trial #the indices correspond to condition and trial numbers... 
            #...given filetypes like "c1s1.wav" 
            datafile.write(str(row)+'\n')
            trial = sound.SoundPyo(value=path+str(trial))
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
                datafile.close()
                win.close()
                core.quit()
        core.wait(1.5)
    win.flip()
    datafile.close()
    win.flip()
    event.waitKeys(keyList=['return'])
    win.close()   

runExp()
core.quit()
