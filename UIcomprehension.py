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
from math import floor


#hex center heights 177,312,447,582,717
#First 
#a = [489,645,801,957,1113]

#a = [567,723,879,1035]

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


     
node_heights=[95,230, 365,500,635, 770]
sep = 77.94228634059948
start = [400+2*sep, 400+sep ,400,400, 400+sep, 400+2*sep]
#starts to each row
nodecol = [start[row]+12 for row in range(6)]
nodecolnum = [7,9,11,11,9,7]

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
    
def select_node(mouseloc):
    ytol = 45
    xtol = 40#h/2
    x, y = mouseloc
    r,c = -1, -1
    
    for i in range(len(node_heights)):
        h = node_heights[i]
        interval = (h-ytol, h+ytol)
        if(y > interval[0] and y < interval[1]):
            r = i
            break
    
    startingval = nodecol[r]
    xs = [startingval + v*sep for v in range(nodecolnum[r])]
    
    for i in range(len(xs)):
        xspot = xs[i]
        interval = (xspot - xtol, xspot + xtol)
        if(x > interval[0] and x < interval[1]):
            c = i
            break
    return (r,c)
 

def select_road(mouseloc):
    #TODO
    pass


