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
        self.hand = {'sheep': 0, 'wheat':0, 'wood':0, 'stone':0, 'brick':0}
        #sheep, wheat, wood, stone, brick
        self.knights  = 0
        self.dev_cards = []
        self.roads = []
        self.ports = {}
        
        #roads will be tracked on one master list on the board object, like settlements
        #still hold coords of roads, i guess, for can_build_road
        
        
        
        
    
    def assign_name(self, name):
        self.name = name
    
    def add_resources(self, res_to_add):
        self.resources.expand(res_to_add)
        
        
    def can_settle(self, spot, board, first = False):#
        #takes spot as a double of coords
        if(not(self.hand['sheep'] and self.hand['wood'] and self.hand['wheat']
               and self.hand['brick'])):
            return False
        #Check for another settlement there
        #check for NOT an adjacent settled node
        #check for a road connected
        #if road placement is properly enforced this should be all thats needed
        if(board.node_list[spot[0]][spot[1]].settled != -1):
            return False
        
        adj = bd.node_spot.node_adj_nodes(spot)
        for adjspot in adj:
            node = board.node_list[adjspot[0]][adjspot[1]]
            if(node.settled != -1):
                return False
        
        adjedges = bd.node_spot.node_adj_edges(spot)
        for edge in adjedges:
            if(edge in self.roads):
                return True
        return False
        
        
        
        
            
        pass
    
    def can_build_road(self, spot, board): #Spot comes in as ((x1,y1), (x2,y2))
    

        #resource check
        if(not(self.hand['wood']  and self.hand['brick'])):
            return False
        
        #CONDITIONS
        #must not be THROugha an adj civ
        #must be adjacent friendly road OR adj friendly civilization on n1 or n2
        #check that there are no other roads here
        
        check = board.roads.check_road(spot)
        if(check == -1):
            return False
        
        n1,n2 = spot
        
        node1 = board.node_list[n1[0]][n1[1]]      
        node2 = board.node_list[n2[0]][n2[1]]  
        
        if(node1.settled == self.key or node2.settled == self.key):
            #if adj friendly settlement, can build. 
            return True
        
        for team, road in board.roads.l:
            if n1 in road or n2 in road:
                if(team == self.key):
                    if(n1 in road):#ceck node1 for enemy settlement
                        return (node1.settled == -1 or node1.settled == self.team)
                            
                    elif(n2 in road):
                        return (node1.settled == -1 or node1.settled == self.team)
                        
                    
        return False
        #                   
            
        #cannot have a road adj to an enemy settled node
        #TODO 
        pass
        
    
    def can_build_city(self,spot, board):
        if(self.hand['stone'] < 3 or self.hand['wheat']):
            return False
        if(self.board.node_list[spot[0]][spot[1]].settled != self.key):
            return False
        
        return True
    
    
    
    def build_settlement(self, loc, board):
        node = board.node_list[loc[0]][loc[1]]
        if(self.can_settle(loc)):
            self.settlements.append(node)
            self.hand['sheep'] -= 1
            self.hand['wood'] -= 1
            self.hand['wheat'] -= 1
            self.hand['brick'] -= 1
            board.settle(loc, self.key)
            
            
            
            
    def build_road(self, spot, board):
        if(self.can_build_road(spot)):
            self.hand['wood'] -= 1
            self.hand['brick'] -= 1
            board.build_road(spot, self.key)
            self.roads.append(bd.edges.order(spot))
            pass
    
    def upgrade_settlement(self, spot, board):
        if(self.can_build_city(spot)):
            board.upgrade_to_city(spot)
            pass
        
        