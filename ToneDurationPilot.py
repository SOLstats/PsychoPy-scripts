# Sound duration pilot script

from psychopy import core, visual, gui, monitors, sound, event
import random, os
from random import sample

path="/Users/peerchristensen/Desktop/PsPy/ToneDurationStimuli/"
win = visual.Window([1000,800], monitor="testMonitor",color=(-1,-1,-1))

stimList = os.listdir(path)
random.shuffle(stimList)
for file in stimList:
    if "DS" in str(file):
        stimList.remove(file)
    
def runExp():
    event.waitKeys(keyList=['return'])
    for file in stimList:
        trial = sound.Sound(value=path+str(file))
        core.wait(0.6)
        trial.play()
        win.flip()
        press = event.waitKeys(keyList=['return','space','escape'])
        if press[0] == 'space': #it is mentioned in the instructions that pressing space will replay the stimulus
            core.wait(0.6)
            trial.play()
            core.wait(2)
            win.flip()
            event.waitKeys(keyList=['return'])
            core.wait(0.2)
        elif press[0] == 'return':
            core.wait(0.5)
        elif press[0] == 'escape':
            win.close()
            core.quit()
        core.wait(1.5)
    win.flip()
    event.waitKeys(keyList=['return'])
    win.close()
    core.quit()
    
runExp()
core.quit()
