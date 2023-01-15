# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:00:25 2023

@author: James
"""

#This will house all of the functions for finding locations when clicking stuff
#or navigating to stuff
#basically anything needed to interact between the canvas/mouse and the game
#besides the drawfunctions. This won't do any drawing

import numpy as np



#177,312,447,582,717
#First 
a = [489,645,801,957,1113]

#a = [567,723,879,1035]
for i in a:
    print(i-78)
155
#upper_boundaries: 110, 245, 380, 515,650, ###785
#left_bounds: 411,567,723,879,1035
#Other left: 489,645,801,957

hex_upper = np.array([110,245,380,515,650])
hex_left = np.array([[567,723,879,10000,10000],
            [489,645,801,957,  10000],
            [411,567,723,879,  1035],
            [489,645,801,957,  10000],
            [567,723,879,10000,10000]])
hex_row_max= np.array([1035,1113,1191,1113,1035])

def select_hex(mouseloc):
    x,y = mouseloc
    r, c = -1,-1

    for newentry in hex_upper:
        if(y >= newentry):
            r += 1
        else:
            break
    if(y > 785):
        r = -1
    
    rowlist = hex_left[r]
    for newentry in rowlist:
        if(x > newentry):
            c += 1
        else:
            break
    if(x > hex_row_max[r]):
        c = -1
    
    return (r,c)
    
    

def select_road(mouseloc):
    #TODO
    pass

def select_node(mouseloc):
    #TODO
    pass

