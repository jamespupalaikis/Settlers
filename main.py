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
####################################
# Programmed in event-based paradigm; 
# timer_fired updates at 10hz (one refresh every event.timerDelay ms)
# cavas redrawn each timer fire. Mouse and keys register an event.
####################################


#TODO


# need to fix the sleep timer so that it sleeps while the proper turn instructions are shown
# polish win screen/add replay button


#AMBITIOUS GOALS: 
# implement animations (this might be a disaster)
# implement full games



########################

def init(data):
    '''Initializes data struct'''
    
    #the fundamental hex edge length
    data.l = 90
    data.board = bd.board()

    pass

########Draw board Fns############################################################







    
############################################################################
#Event update functions#
def mouse_pressed(event, data):
    pass
       

def key_pressed(event, data):
    pass
    

def timer_fired(data):
    pass

def redraw_all(canvas, data):
    draw.draw_board_area(canvas, data)
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