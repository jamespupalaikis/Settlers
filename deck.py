# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:35:42 2023

@author: James
"""
import random as rand
#Here we will put the resources deck, and handle deck operations
class deck:
    def __init__(self):
        self.deck = []
        
    def add_cards(self, cards):
        self.deck.extend(cards)
        
    def shuffle_deck(self):
        rand.shuffled(self.deck)
        
    def draw_one(self):
        return self.deck.pop(0)
    
    def peek(self):
        return self.deck[0]
    
    def populate(self):#Fill up the deck and shuffle it
        #TODO
        pass
    
    
    
    

