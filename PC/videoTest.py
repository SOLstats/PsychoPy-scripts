
# -*- coding: utf-8 -*-

# Script testing video files in PsychoPy

#NOTES: 

#an error occurred and the audio device
#had to be changed to['Built-in Output'] in "Preferences"

# For the videos to play, I had to recode the video files
# to: AAC, H.264 (codecs). This is easily done in Finder (on mac os)

#.DS_store files are a major problem for mac users!
#This script uses a function to remove them


from psychopy import visual, core, event, sound, gui
import random, os, time

#load and shuffle videos
pathVids= ‘/your-path/folder-name/‘
vids = os.listdir(pathVids)
random.shuffle(vids)
vids.remove(".DS_Store") 
print(vids) #check video order, check for "DS" files
        
#create display window
win = visual.Window([1000,800],allowGUI=True,monitor='testMonitor',winType='pyglet',units='norm',color=(-1,-1,-1))

#define main function
def playVids():
    for vid in vids:
        v = visual.MovieStim2(win, pathVids+vid)
        core.wait(2)
        win.flip()
        #press=event.waitKeys(keyList=['return']) #waits for the participant to press 'return'
        while v.status != visual.FINISHED: #On my system the videos appear to only play inside a 'while' loop
            v.draw()
            win.flip()
        print(vid) #shows latest played vid (to check for errors in individual files)
    #event.waitKeys(keyList=['return'])
    win.close()

# call the main function and play videos
playVids()
        


