# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:19:05 2022

@author: James
"""
from tkinter import *
import numpy.random as rand

from time import sleep
import math
from collections import defaultdict

import board as bd












def draw_board_area(canvas, data):
    canvas.create_rectangle(400,50, 1200, 850)
    
    for row in data.board.hex_list:
        for _hex in row:
            if(_hex):
                draw_hex(_hex, canvas, data)
    
    
    pass

def draw_hex(_hex, canvas, data):
    #loc is the row, col coordinate format
    l = data.l
    x, y = _hex.placement()
    h = math.sqrt(3/4)* l
    
    a = (x, y-l)
    b = (x+h, y-l/2)
    c = (x+h, y+l/2)
    d = (x, y+l)
    e = (x-h, y+l/2)
    f = (x-h, y-l/2)
    fillDict = {'sheep': 'light green', 'wood': 'green', 'brick': 'orange', 
                'wheat': 'yellow', 'stone': 'gray', 'desert': 'tan'}
    canvas.create_polygon(a,b,c,d,e,f, fill = fillDict[_hex.resource], 
                          outline = 'black')
    
    rad = 25
    canvas.create_oval(x-rad,y-rad,x+rad,y+rad, fill = 'white')
    
    numDict = defaultdict(lambda : 'black')
    numDict[6] = 'red'
    numDict[8] = 'red'
    canvas.create_text(x,y,text=_hex.number, fill=numDict[_hex.number], 
                       font="bold")
    
#print(bd.hex_spot.hex_adj_hex(1, 1))