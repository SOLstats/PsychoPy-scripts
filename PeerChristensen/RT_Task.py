# Speeded response task testing cross-modal correspondences for pitch

#import
from psychopy.visual import Circle
from psychopy import visual, event, core, sound, gui
import random, os, csv

#log
log_path = '/Users/peerchristensen/Desktop/RT_logs/' 
info = {'participant':'','age':'','language':"",'gender':['male', 'female']}
if not gui.DlgFromDict(info, order=['participant', 'age', 'language', 'gender']).OK:      
    core.quit()  
log = open(log_path+str(info['participant'])+".csv",'w')   
writer = csv.writer(log, delimiter=";")
cols="participant","language","gender","age","condition","block","trial","sound","visual","key","RT"
writer.writerow(cols)

#window
win = visual.Window(fullscr=False,useRetina=False,allowGUI=True,monitor='testMonitor',units='pix',color=(0,0,0))
black=[-1,-1,-1]
center = [-0.1,0]

#constants
if int(info['participant']) % 2 == 0:
    conditions = ['size','height']
else:
     conditions = ['height', 'size']   
nBlocks = 1
nTrials = 4

#time
RT=core.Clock()

#sound stimuli
highSound = sound.Sound('A',octave=4,sampleRate=44100,secs=0.120,stereo=True,name = "high")
lowSound  = sound.Sound('A',octave=2,sampleRate=44100,secs=0.150,stereo=True,name = "low")
sounds=[highSound,lowSound] * (nTrials/2)
    
# Visual stimuli
#fixation cross
fixCross = visual.TextStim(win, text="+",pos=center,units="deg", color=black,height=3)
#HEIGHT
circleHIGH = Circle(win=win,units="deg",radius= 3, fillColor=black,lineColor=black,pos=[-0.1,8],name="high")
circleLOW = Circle(win=win,units="deg",radius= 3, fillColor=black,lineColor=black,pos=[-0.1,-8],name="low")
#SIZE
circleBIG = Circle(win=win,units="deg",radius= 6, fillColor=black,lineColor=black,pos=center,name="big")
circleSMALL = Circle(win=win,units="deg",radius= 1.5, fillColor=black,lineColor=black,pos=center,name="small")

stimsSize= [circleBIG,circleSMALL] * (nTrials/2)
stimsHeight=[circleHIGH,circleLOW] * (nTrials/2)

time=core.Clock()
#experiment
for condition in conditions:
    core.wait(2)
    if condition == "size":
        stims=stimsSize
    else:
        stims=stimsHeight
    for block in range(1,nBlocks+1):
        random.shuffle(sounds)
        random.shuffle(stims)
        core.wait(1)
        for i in range(len(stims)):
            fixCross.draw()
            win.flip()
            core.wait(0.50)
            stims[i].draw()
            win.flip()
            sounds[i].play()
            RT.reset()
            core.wait(0.120)
            win.flip()
            press = event.waitKeys(keyList=["s","k"], timeStamped=RT)
            row=info['participant'],info['language'],info['gender'],info['age'],condition,block,i+1,sounds[i].name,stims[i].name,press[0][0],press[0][1]
            writer.writerow(row)
        win.flip()
        core.wait(1)
        event.waitKeys('return')
        core.wait(2)
#estimate=time.getTime()
win.close()
core.quit()

#pathSounds="/Users/peerchristensen/Desktop/PsPy/responseTaskSounds/"
#sounds=os.listdir(pathSounds)
#sounds.remove(".DS_Store") 