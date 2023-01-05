# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:54:12 2022

@author: James
"""
#Deals with the interface of the entire game. Will contain the board, but allow
#functionality between the players, cards,etc with the board. 

import random as rand





class classic_game:
    def __init__(self, players, playernum):
        #Each player needs a key assigned! dont forget that
        assert(len(players) == playernum)
        self.players = players
        self.playernum = playernum
        
        rolls = self.get_player_order()
        self.order = [i[1] for i in rolls]
        
        
        
        
        
    def get_player_order(self):
        self.turn = 0
        rolls = []
        i = 0
        while(i < self.playernum):
            r1 = rand.randint(1,6)
            r2 = rand.randint(1,6)
            rolls.append(r1+r2,self.players[i], r1, r2) 
            i += 1
            
        rolls.sort(reverse=True)
        return rolls
    
    def play_turn(self, player):
        pass
    


