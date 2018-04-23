# Explicit pitch association task: ~HEIGHT & ~SIZE

# TO DO
#log, csv output
#add sound files

#import
from psychopy.visual import Circle
from psychopy import visual, event, core, sound, gui
import random, os
import numpy as np
import csv

#log
log_path = '/Users/peerchristensen/Desktop/choice_logs/' 
info = {'participant':'','age':'','language':"",'gender':['male', 'female']}
if not gui.DlgFromDict(info, order=['participant', 'age', 'language', 'gender']).OK:      
    core.quit()  
    
log = open(log_path+str(info['participant'])+".csv",'wb')   
writer = csv.writer(log, delimiter=";")
cols="participant","language","gender","age","trial","voice","left","right","choice","choiceName"
writer.writerow(cols)

#window
win = visual.Window(fullscr=False,useRetina=True,allowGUI=True,monitor='testMonitor',units='pix',color=(0,0,0))
win.update()

#n trials
nTrials=8
#Visual stimuli
black=[-1,-1,-1]
leftPos= -300
rightPos= 300

#HEIGHT
circleHIGH = Circle(win=win,units="pix",radius= 100, fillColor=black,lineColor=black,pos=[0,300],name="high")
circleLOW = Circle(win=win,units="pix",radius= 100, fillColor=black,lineColor=black,pos=[0,-300],name="low")
#SIZE
circleBIG = Circle(win=win,units="pix",radius= 200, fillColor=black,lineColor=black,pos=[0,0],name="big")
circleSMALL = Circle(win=win,units="pix",radius= 50, fillColor=black,lineColor=black,pos=[0,0],name="small")
#Visual stimulus lists

completeList=[[circleSMALL, circleBIG],
    [circleLOW, circleHIGH],[circleHIGH, circleSMALL],
    [circleLOW, circleBIG]] * (nTrials/4)
random.shuffle(completeList)

#Auditory stimuli
highSound = sound.Sound('A',octave=5,sampleRate=44100,secs=0.8,stereo=True,name = "high")
lowSound  = sound.Sound('A',octave=2,sampleRate=44100,secs=0.8,stereo=True,name = "low")
completeSounds = [highSound,lowSound] * (nTrials/2)
random.shuffle(completeSounds)

for i in range(0,nTrials):
    trial=i+1
    print(i)
    win.flip()
    core.wait(0.3)
    completeSounds[i].play()
    print(completeSounds[i].name)
    core.wait(1)
    stimLeft=completeList[i][0]
    stimRight=completeList[i][1]
    if stimLeft.name=="high":
        stimLeft.pos = [-450,300]
    elif stimLeft.name=="low":
        stimLeft.pos = [-450,-300]
    else:
        stimLeft.pos = [-450,0]
    if stimRight.name=="high":
        stimRight.pos = [400,300]
    elif stimRight.name=="low":
        stimRight.pos = [400,-300]
    else:
        stimRight.pos = [400,0]
    print(stimLeft.name)
    print(stimRight.name)
    stimLeft.draw()
    stimRight.draw()
    win.flip()
    key = event.waitKeys(keyList=['s','k'])
    if key[0] == "s":
        choice = "left"
        choiceName = stimLeft.name
    else:
        choice = "right"
        choiceName = stimRight.name
    print(key,choice,choiceName)
    row=info['participant'],info['language'],info['gender'],info['age'],trial,completeSounds[i].name,stimLeft.name,stimRight.name,choice,choiceName
    writer.writerow(row)
    core.wait(0.5)
    

#pathSounds="/Users/peerchristensen/Desktop/PsPy/responseTaskSounds/"
#sounds=os.listdir(pathSounds)
#sounds.remove(".DS_Store") 
#trialx = sound.Sound(value=path+str(t))

win.close()
core.quit()