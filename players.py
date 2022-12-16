# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 20:05:31 2022

@author: James
"""

class player:
    def __init__(self, name='asshole'):
        self.name = name
        self.vp = 0
        self.settlements = []#and cities
        self.hand = []
        self.knights  = 0
        self.dev_cards = []
        #roads will be tracked on one master list on the board object, like settlements
        
        
    
    def assign_name(self, name):
        self.name = name
    
    def add_resources(self, res_to_add):
        self.resources.expand(res_to_add)
        
        
    def can_settle(self, spot):
        pass
    
    def can_build_road(self, spot):
        pass
        
    def build_settlement(self, node_to_settle):
        if(self.can_settle(node_to_settle.loc)):
            self.settlements.append(node_to_settle)
            
            
            
    def build_road(self, spot):
        