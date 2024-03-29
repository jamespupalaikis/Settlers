# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:02:34 2022

@author: James
"""

from tkinter import *
import numpy.random as rand

from time import sleep
import math
import drawFunctions as draw
import board as bd
import game
import players
import UIcomprehension as UI
####################################
# Programmed in event-based paradigm; 
# timer_fired updates at 10hz (one refresh every event.timerDelay ms)
# cavas redrawn each timer fire. Mouse and keys register an event.
####################################


#TODO



########################

def init(data):
    '''Initializes data struct'''
    
    #the fundamental hex edge length
    # data.l = 90
    playerlist = [players.player(1, 'jim1'),players.player(2, 'jim2'),
               players.player(3, 'jim3'),players.player(4, 'jim4')]
    data.game = game.classic_game(playerlist,4)
    
    data.board = data.game.board
    
    data.color_map = {1: 'red', 2: 'purple', 3: 'light blue', 4: 'magenta'}
    data.board.roads.add_road(((1,1),(1,2)), 3)
    data.board.roads.add_road(((4,5),(5,4)), 4)
    
    data.board.settle((3,4), 2)
    
    
    
    data.board.settle((4,7), 1)
    data.board.upgrade_to_city((4,7))
    
    pass

########Draw board Fns############################################################







    
############################################################################
#Event update functions#
def mouse_pressed(event, data):
    loc = (event.x, event.y)
    #print(UI.select_hex(loc)) 
    print(UI.select_road(loc))

def key_pressed(event, data):
    pass
    

def timer_fired(data):
    pass

def redraw_all(canvas, data):
    
    x,y = bd.node_spot.placement(5, 6)
    
    h = 90 * math.sqrt(3/4) 
    r = 10




    
    draw.draw_board_area(canvas, data)
    draw.draw_roads(data.board.roads, canvas, data)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill = 'red')
    
    for node in data.board.settled:
        #(node)
        draw.draw_settlement(node, canvas, data)
        pass
        

##############
# use the run function as-is
####################################

def run(width=300, height=300):
    def redraw_allWrapper(canvas, data):
        canvas.delete(ALL)
        redraw_all(canvas, data)
        canvas.update()    

    def mouse_pressedWrapper(event, canvas, data):
        #print('mpwrapper')
        mouse_pressed(event, data)
        
        redraw_allWrapper(canvas, data)

    def key_pressedWrapper(event, canvas, data):
        key_pressed(event, data)
        redraw_allWrapper(canvas, data)

    def timer_firedWrapper(canvas, data):
        timer_fired(data)
        redraw_allWrapper(canvas, data)
        # pause, then call timer_fired again
        canvas.after(data.timerDelay, timer_firedWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mouse_pressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            key_pressedWrapper(event, canvas, data))
    timer_firedWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

#
run(1600, 900)