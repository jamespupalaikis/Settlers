'''
THIS FILE: 
'''


#3 subtypes: a hex, a node, and an edge
#all will be inheritors of a superclass: board_spot
#Board_spots will have the function b.connected() which will pass back a triple:
    #with a list of "connected" hexes, nodes, and edges, in order
# Board_spots also have a b.get_loc() function, which will pass a double, with:
    #the coordinate location on the board, plus an angle if it is an edge. 

import math
import numpy as np
import random as rand
from collections import defaultdict

global l 
l = 90 


class board_spot:
    def __init__(self):

        #the row, num_in_row of the piece
        self.loc = (0,0) 
        
    def __repr__(self):
        return 'A unassigned board spot'
    
    
    
    
class hex_spot(board_spot):
    def __init__(self, loc, resource, number):
        self.loc = loc
        self.resource = resource
        self.number = number
        self.l = l
        
    def __repr__(self):
        return f'A {self.resource} hex, number {self.number}'
    
    def connected(self):
        row, col = self.loc
        hexes = hex_spot.hex_adj_hex(row, col)
        nodes = hex_spot.hex_adj_node(row, col)
        return hexes, nodes, []
       
    @staticmethod
    def placement(r,c):

       row, col = r,c
       h = math.sqrt(3/4)* l
       
       
       colstart = [400+3*h, 400+2*h ,400+h, 400+2*h, 400+3*h]
       x = colstart[row] + col*(2*h)
       
       row1 = 50 + l
       y = row1 + row*(3*l/2)
       
       return (x+12, y+37)
      
    @staticmethod
    def hex_adj_hex(row, col):
        adj = []
        if(col != 0):
           adj.append((row,col-1))
       
        if(row == 0 or row == 4):
            if(col != 2):
                adj.append((row, col + 1))
            
            if(row == 0):
                adj.append((row+1, col))
                adj.append((row+1, col+1))
            else:#row is 4
                adj.append((row-1, col))
                adj.append((row-1, col+1))
            
        elif(row == 1 or row == 3):

            if( row == 1):
                if(col != 3):
                    adj.append((row - 1, col))
                    adj.append((row, col + 1))
                if(col != 0):
                    adj.append((row-1, col-1))
                adj.append((row+1, col))
                adj.append((row+1, col + 1))
        
            else: #row is 3
                if(col != 3):
                    adj.append((row, col +1))
                    adj.append((row+1, col))
                if(col != 0):
                    adj.append((row + 1, col-1))
                adj.append((row-1, col))
                adj.append((row-1, col+1))
            
        else:#row is 2
            if(col == 0):
                adj.append((1,0))
                adj.append((3,0))
                adj.append((2,1))
            elif(col == 4):
                adj.append((1,3))
                adj.append((3,3))
            else:
                adj.append((row-1,col-1))
                adj.append((row+1,col-1))
                adj.append((row-1,col))
                adj.append((row+1,col))
                adj.append((row, col+1))
        return adj
            
                 
    @staticmethod
    def hex_adj_node(row, col):
        if(row in (0,1)):
            adj = [(row, 2*col), (row, 2*col+1), (row, 2*col+2),
                   (row+1, 2*col+1), (row+1, 2*col+2), (row+1, 2*col+3)]
        elif(row == 2):
            adj = [(row, 2*col), (row, 2*col+1), (row, 2*col+2),
                  (row+1, 2*col), (row+1, 2*col+1), (row+1, 2*col+2)]
        else:
            adj = [(row, 2*col+1), (row, 2*col+2), (row, 2*col+3),
                   (row+1, 2*col), (row+1, 2*col+1), (row+1, 2*col+2)]
        return adj
    


    
    
class node_spot(board_spot):
    def __init__(self, loc):
        self.loc = loc
        self.settled = -1 #False
        self.city = False
        self.l = l
        
    def __repr__(self):
        return 'Node', str(self.loc)
    
    
    def settle_node(self, team):
        assert(self.settled == -1)
        self.settled = team
        
    def build_city(self):
        assert(self.settled)
        self.city = True
    
        return f'A node located at {self.loc}'
    
    
    @staticmethod
    def placement(row, col):
        '''convert row, col into an x,y(from the top) coordinate pixel location'''

        
        h = math.sqrt(3/4) * l
        
        def get_init(row):
            colstart = [400+3*h, 400+2*h ,400+h, 400+2*h, 400+3*h]
            row1 = 50 + l
            y = row1 + row*(3*l/2)
            return colstart[row]+12, y+37
        
        def above(row, col):
            x0,y0 = get_init(row)
            if(col %2 == 0):#is even
                eveninit = (x0-h, y0-(l/2))
                return (eveninit[0]+ h*col, eveninit[1] )
                
            else:#is odd
                oddinit = (x0, y0-l)
                return (oddinit[0]+ h*(col-1), oddinit[1] )
            
        def below(row, col):
            x0,y0 = get_init(row)
            if(col %2 == 0):#is even
                eveninit = (x0-h, y0+(l/2))
                #return eveninit
                return (eveninit[0]+ h*col, eveninit[1] )
                
            else:#is odd
                oddinit = (x0, y0+l)
                return (oddinit[0]+ h*(col-1), oddinit[1] )
        
        
        if(row <= 2):
            return above(row, col)
        else:
            return below(row-1, col)
            
        
            
            
        
        
        pass
    
    def node_adj_nodes(self):
        row, col = self.loc
        colnum = [6,8,10,10,8,6]
        adj = []
        
        
        if(col != 0):
            adj.append((row, col-1))
        if(col < colnum[row]):
            adj.append((row, col+1))
        
        def isodd(n):
            return n%2 == 1
        
        
        if(row == 0):
            if(not isodd(col)):
                adj.append((2, col+1))
        elif(row == 1):
            if(isodd(col)):
                adj.append((1, col-1))
            else:
                adj.append((3, col+ 1))
        elif(row == 2):
            if(isodd(col)):
                adj.append((1, col-1))
            else:
                adj.append(3, col)
        elif(row == 3):
            if(isodd(col)):
                adj.append((4, col-1))
            else:
                adj.append(2, col)
        elif(row == 4):
            if(isodd(col)):
                adj.append((5, col-1))
            else:
                adj.append((3, col+1))
        elif(row == 5):
            if(not isodd(col)):
                adj.append(4 ,col+1)
        return adj
    
    
            
                

    def node_adj_edges(self):
        #TODO
        pass
    
class edges():
    #This will hold ALL the roads in the game. 
    #Why? well in my mind at least, regarding 
    #checking if a road is legal, how long each road chain is, and whether a 
    #node is settleable, the math works out easier if the roads are just 
    #defined as a pair of nodes that the road exists between. 
    #in this case, we'll need to carefully control functions on the road 
    #dict/array, to avoid the parity cases from flipping the nodes in a pair.
    def __init__(self):
        


        def default():
            return defaultdict(lambda:None)
        self.roads = defaultdict(default)
        self.l = []
        
    def __repr__(self):
        return f'The edges object'
    
    @staticmethod
    def order(coords):#comes in as ((row1,col1), (row2,col2))
        a,b = coords
        if(a > b):
            return (b,a)
        return coords
        
    def check_road(self,coords):
        coords = self.order(coords)
        check = self.roads[coords[0]][coords[1]]
        if(check is None):
            return -1
        
        return check
        
    def add_road(self, coords, team):
        coords = self.order(coords)
        d1 = self.roads[coords[0]]
        d1[coords[1]] = team
        self.l.append(coords)
        return coords
        
    def remove_road(self, coords):
        coords = self.order(coords)
        d1 = self.roads[coords[0]]
        self.l.remove(coords)
        del d1[coords[1]]
    
    @staticmethod    
    def placement( coords):

        p1 = node_spot.placement(coords[0][0], coords[0][1])
        p2 = node_spot.placement(coords[1][0], coords[1][1])
        return p1,p2
    
        
    
###########Unified Board################################
        
class board:
    def __init__(self, mode = 'Classic'):

        self.settled = []
        self.make_hexes()
        self.make_nodes()
        self.roads = edges()
        
        #self.settlements = set()
        self.robber = self.desert
        
        
        
    def make_hexes(self):
        '''Populates a self.hex_list array with hexes, with resources chosen 
        from the resources list, same with numbers. '''
        redo = True
        while( redo):
            redo = False
            resources = ['sheep', 'sheep', 'sheep', 'sheep',
                         'wheat', 'wheat', 'wheat', 'wheat',
                         'wood', 'wood', 'wood', 'wood', 
                         'stone', 'stone', 'stone', 
                         'brick', 'brick', 'brick', 
                         'desert']
            
            numbers = [[2,3,3,4,4,5,5,9,9,10,10,11,11,12],[8,8,6,6],17, 13]
            rand.shuffle(resources)
    
            excluded = []
            self.hex_list = np.ndarray(shape=(5,5), dtype = board_spot)
            
            
            
            colnum = [3,4,5,4,3]
    
            for row in range(5):
                for col in range(colnum[row]):
    
                    #pop off a resource from the list to add
                    res = resources.pop()
                    
                    #only add a number if not desert
                    if(res != 'desert'):
                        
                        if(numbers[2] == 0):
                            num = (numbers[0]+numbers[1]).pop()
                            
                        #check for adjacent reds
                        elif((row,col) in excluded):

                            if(numbers[3] <= 0):
                                redo = True
                                break
                            #print((row, col), excluded)
                            
                            roll = rand.randint(0,numbers[3])
                          
                            num = numbers[0].pop(roll)
                            #print(roll, num)
                            
                            numbers[3] -= 1
                            
                        else:#not excluded
                            
                            if(numbers[3]+1==numbers[2]):
                                num = numbers[1].pop()
                                excluded.extend( hex_spot.hex_adj_hex(row,col))
                                
                            else:
                                roll = rand.randint(0,numbers[2])
                                if(roll <= numbers[3]):#not red 
                                
                                    #decrement non-red count
                                    numbers[3] -=1
                                    
                                    num = numbers[0].pop(roll)
                                    
                                    
                                else:#is a red number
                                    num = numbers[1].pop(roll-numbers[3]-1)
                                    excluded.extend( hex_spot.hex_adj_hex(row,col))
                                    #print(f'excluded updated {excluded}')
                        numbers[2] -= 1#decrement total count
                    else:
                        num = 0
                        self.desert = (row,col)
                    
                    #make the hex, add to array
                    self.hex_list[row][col] = hex_spot((row,col), res,num)
        
    def make_nodes(self):
        self.node_list = np.ndarray(shape=(6,11), dtype=board_spot)
        colnum = [7,9,11,11,9,7]
        
        for row in range(6):
            for col in range(colnum[row]):
                self.node_list[row][col] = node_spot((row,col))
                
    def settle(self,loc, player):
        #checks for hand reqs come from player level; 
        #I suppose the checks for location should too
        node = self.node_list[loc[0]][loc[1]]
        node.settle_node(player)
        self.settled.append(node)
    
    def upgrade_to_city(self,loc):
        node = self.node_list[loc[0]][loc[1]] 
        node.build_city()
        
        

a = edges()
a.add_road(((1,1),(1,3)), 3)
a.add_road(((1,1),(1,2)), 2)
print(a.l)
a.remove_road(((1,1),(1,3)))
print(a.l)

print(a.roads[(1,1)].keys())
print(a.check_road(((1,1),(1,3))))