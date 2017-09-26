
from psychopy import core, visual, gui, monitors, sound, event
import random, os
from random import sample
import csv
import numpy as np
core.wait(0.5)

path="/Users/peerchristensen/Desktop/PsPy/timeAge/"
log_path = '/Users/peerchristensen/Desktop/PsPy/timeAge/timeAgeLogs/' 

info = {'participant':'','age':'','language':"",'gender':['male', 'female']}
if not gui.DlgFromDict(info, order=['participant', 'age', 'language', 'gender']).OK:      
    core.quit()  
    
log = open(log_path+str(info['participant'])+".csv",'wb')   
writer = csv.writer(log, delimiter=";")
cols="participant","language","gender","age","trial","image","t","estimate","diff"
writer.writerow(cols)

win = visual.Window(fullscr=True, monitor="testMonitor",color=(-1,-1,-1))
qMark = visual.TextStim(win, text="?")
startMes = visual.TextStim(win, text="Hit ENTER to begin")
nextMes = visual.TextStim(win, text="Hit ENTER")

images=[]
for file in os.listdir(path): 
    if file.lower().endswith(".jpg"):
        images.append(file)
        
def runExp():
    stims=list(np.arange(1,10,0.5)) #change according to desired stim length
    random.shuffle(stims)
    core.wait(0.5)
    startMes.draw()
    win.flip()
    event.waitKeys(keyList=['return'])
    win.flip()
    for i in range(1,10):
        trialNum=visual.TextStim(win=win,text=str(i))
        random.shuffle(images)
        img = visual.ImageStim(win, image=images[0])
        print("####################\nTrial num: " + str(i))
        print(str(images[0]))
        print("Time: " + str(stims[i]))
        core.wait(1.5)
        trialNum.draw()
        win.flip()
        core.wait(1.5)
        win.flip()
        core.wait(2.5)
        img.draw()
        win.flip()
        core.wait(stims[i])
        win.flip()
        core.wait(1.5)
        qMark.draw()
        win.flip()
        event.waitKeys(keyList=['return'])
        clock=core.Clock()
        event.waitKeys(keyList=['return'])
        estimate=clock.getTime()
        win.flip()
        core.wait(0.5)
        diff = estimate - stims[i]
        print("Estimate: " + str(estimate))
        print("diff: " + str(diff))
        nextMes.draw()
        win.flip()
        row=info['participant'],info['language'],info['gender'],info['age'],i,images[0],stims[i],round(estimate,3),round(diff,3)
        writer.writerow(row)
        images.pop(0) #limits each picture to a single trial
        press = event.waitKeys(keyList=['return','escape'])
        if press[0] == "return":        
            core.wait(0.5)
        else:
            log.close()
            win.close()
            core.quit()

runExp()
win.close()
core.quit

#Open online survey,e.g. LHQ
#import webbrowser as web
#surveyURL = 'http://' #full URL goes here
#web.open(surveyURL) 