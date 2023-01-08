# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:54:12 2022

@author: James
"""
#Deals with the interface of the entire game. Will contain the board, but allow
#functionality between the players, cards,etc with the board. 

import random as rand
import board as bd


#ALL STATES:
'''
waiting for roll
waiting for discard
waiting for robber move
waiting to take card
waiting to build... 
-> waiting for placement for settlement
-> waiting for placement for road
-> waiting for city loc
-> waiting for card target
'''



class classic_game:
    def __init__(self, players, playernum):
        #Each player needs a key assigned! dont forget that
        assert(len(players) == playernum)
        
        self.board = bd.board()
        self.players = players
        self.playernum = playernum
        playerdict = {}
        
        #Index players according to key
        for player in players:
            playerdict[player.key] = player
            
        
        rolls = self.get_player_order()
        self.order = [i[1] for i in rolls]
        
        self.currentplayer = self.order[0]
        self.turn  = 0 #used to get whose turn it is
        self.state = "wait_place_settlement_0"
    
        
        
        
################################INITIALIZATION STUFF ##########################    
    def get_player_order(self):
        self.turn = 0
        rolls = []
        i = 0
        while(i < self.playernum):
            r1 = rand.randint(1,6)
            r2 = rand.randint(1,6)
            rolls.append((r1+r2,self.players[i].key, r1, r2)) 
            i += 1
            
        rolls.sort(reverse=True)
        return rolls
    
    #def play_turn(self, player):
        #pass

    def initial_placement(self, loc):
        assert(self.state == "wait_place_settlement_0")
        
        self.currentplayer.build_settlement(loc)


###############################################################################    

    def pay_out_roll(self, roll):
        #TODO
        pass
    
    def make_roll(self):
        #TODO
        #If(roll != 7)
        #self.pay_out_roll(roll)???
        #return roll
        pass
    
    def move_robber(self, loc):
        #TODO
        pass
    
    def steal_card(self, playerfrom):
        #TODO
        pass
    
    def build_settlement(self):
        #TODO
        pass
    
    def build_road(self):
        #TODO
        pass
    
    def upgrade_to_city(self):
        #TODO
        pass
    
    
    
        
        
    
    


