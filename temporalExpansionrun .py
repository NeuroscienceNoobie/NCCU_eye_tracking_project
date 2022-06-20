# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 01:20:03 2022
@author: yu
"""
import numpy as np
import os
import random

import itertools
import random
import numpy as np

import psychopy
from psychopy import visual, core, event, data, gui 
from psychopy.hardware import keyboard
import glob 

import random

ddir = 'C:\\Users\yu\Desktop\img3'
os.chdir(ddir)
print(os.getcwd())

# get name of all png files in directory 
filelist=os.listdir(ddir)
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(fichier.endswith(".jpg")):
        filelist.remove(fichier)

# get the last four scrambled files
filelist4s = filelist[-4:]

#rand the filelist
random.shuffle(filelist)

# append the two lists together 
# to make the first four items as a baseline 5 sec duration training 
print(filelist)


expInfo = {'subjnum':''}
expInfo['dateStr'] = data.getDateStr()
dlg = gui.DlgFromDict(expInfo, title='UTP', fixed=['expInfo'])
filenameMain = expInfo['subjnum'] + '_' + expInfo['dateStr']
dataFile = open(filenameMain+'.csv', 'w',encoding='utf-8')
dataFile.write('trial_num, img, response, RT \n')

kb = keyboard.Keyboard()
event.globalKeys.clear()
def byebye():
    win.close()
    core.quit()
event.globalKeys.add(key='q',func=byebye)


filelist = filelist[-16:] #be ware for weird .jpg hidden files 
jitList_ITI = np.random.uniform(0.1, 1.5, 50)

refreshRate = 240

# Open Window
colorspace= 'rgb255'
win = visual.Window([1920,1080],monitor='MSI 240Hz', 
                    units="pix",color = [0, 0, 0],colorSpace='rgb255', 
                    fullscr=True, screen =1)

#training session 
nTrial = 0
for k in range(len(filelist4s)):
    stim = psychopy.visual.ImageStim(win,filelist4s[k])
    stim.draw()
    win.flip()
    core.wait(5)
    win.flip()
    print(jitList_ITI[k])
    core.wait(jitList_ITI[k])
                                 

event.waitKeys(keyList=['r'], modifiers=False, timeStamped=False, clearEvents=True)################ added for break


# testing session
nTrial = 0
for k in range(len(filelist)):
    stim = psychopy.visual.ImageStim(win,filelist[k])
    stim.draw()
    win.flip()
    core.wait(5)
    win.flip()
    print(jitList_ITI[k])
    core.wait(jitList_ITI[k])
    
    key =[]        
    keyPressed = 0
    kb.clearEvents()
    kb.clock.reset()
    framecounter =0
    while keyPressed == 0: 
          win.flip()
          
          thisKey = kb.getKeys(['left','right'])
          if len(thisKey) > 0:
            key = thisKey[0]
            if key.name == 'left':
                 dataFile.write('%d, %s, %s, %.5f\n' %(nTrial, filelist[k], 's', thisKey[0].rt))
                 keyPressed =1
                 print('Response made:','Shorter Pressed')
                 break
             
            elif key.name == 'right':
                 dataFile.write('%d, %s, %s, %.5f\n' %(nTrial, filelist[k], 'l', thisKey[0].rt))
                 keyPressed =1
                 print('Response made:','Longer Pressed')
                 break
    nTrial+=1


dataFile.close()
win.close()
core.quit()




