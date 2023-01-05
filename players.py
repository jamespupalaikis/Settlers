# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 20:05:31 2022

@author: James
"""
import board as bd


class player:
    def __init__(self, key,name='asshole'):
        self.key = key
        self.name = name
        self.vp = 0
        self.settlements = []#and cities
        self.hand = [[],[],[],[],[]]#sheep, wheat, wood, stone, brick
        self.knights  = 0
        self.dev_cards = []
        self.roads = []
        #roads will be tracked on one master list on the board object, like settlements
        #still hold coords of roads, i guess, for can_build_road
        
        
        
        
    
    def assign_name(self, name):
        self.name = name
    
    def add_resources(self, res_to_add):
        self.resources.expand(res_to_add)
        
        
    def can_settle(self, spot):
        #takes spot as a double of coords
        if(not(self.hand[1] and self.hand[2] and self.hand[3] and self.hand[4])):
            return False
        #Check for another settlement there
        #check for NOT an adjacent settled node
        #check for a road connected
        #if road placement is properly enforced this should be all thats needed
        
        
            
        pass
    
    def can_build_road(self, spot, board):
        #resource check
        if(not(self.hand[2]  and self.hand[4])):
            return False
        
        #check for an adjacent friendly road
        
        #check that there are no other roads here
        check = board.roads.check_road(spot)
        if(check == -1):
            return False
            
        #cannot have a road adj to an enemy settled node
        #TODO 
        pass
        
    def build_settlement(self, loc, board):
        node = board.node_list[loc[0]][loc[1]]
        if(self.can_settle(loc)):
            self.settlements.append(node)
            self.hand[1].pop()
            self.hand[2].pop()
            self.hand[3].pop()
            self.hand[4].pop()
            board.settle(loc, self.key)
            
            
            
            
    def build_road(self, spot):
        if(self.can_build_road(spot)):
            #TODO
            pass
    
    def upgrade_settlement(self, spot):
        if(self.can_build_city(spot)):
            #TODO
            pass
        
        