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
    l = _hex.l
    loc = _hex.loc
    
    x, y = _hex.placement(loc[0],loc[1])
    h = math.sqrt(3/4)* l
    #print(h)
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
    #canvas.create_text(x, y+20, text=f"(,{int(x)})")
    
    
def draw_node(_node, canvas, data):
    pass

def draw_roads(roads, canvas, data):
    data.color_map
    for tm,road in roads.l:
        #print('a', road)
        p1,p2 = roads.placement(road)
        #tm = roads.check_road(road)
        canvas.create_line(p1[0],p1[1],p2[0],p2[1], fill = data.color_map[tm],
                           width = 9)
        
def draw_settlement(node, canvas, data):
    assert node.settled != -1
    loc = node.loc
    x, y = node.placement(loc[0], loc[1])
    tm = node.settled
    
    if(node.city == False):
    
        canvas.create_rectangle(x-15, y-15, x + 15, y+15, fill = data.color_map[tm])
        x1,y1 = x-25, y-15
        x2,y2 = x + 25, y-15
        x3,y3 = x, y-30
        canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill = data.color_map[tm] )
    else:
        canvas.create_rectangle(x-25, y-15, x + 25, y+15, fill = data.color_map[tm])
        canvas.create_rectangle(x-25, y-30, x, y-15, fill = data.color_map[tm])
        
    
    
    
#print(bd.hex_spot.hex_adj_hex(1, 1))