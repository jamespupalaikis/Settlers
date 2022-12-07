#3 subtypes: a hex, a node, and an edge
#all will be inheritors of a superclass: board_spot
#Board_spots will have the function b.connected() which will pass back a triple:
    #with a list of "connected" hexes, nodes, and edges, in order
# Board_spots also have a b.get_loc() function, which will pass a double, with:
    #the coordinate location on the board, plus an angle if it is an edge. 


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
        
    def __repr__(self):
        return f'A {self.resource} hex, number {self.number}'
    
   def connected(self):
   
       
   @staticmethod
   def hex_adj_hex(row, col):
       
    
class node_spot(board_spot):
    def __init__(self, loc):
        self.loc = loc
        self.settled = []
        
    def __repr__(self):
        return f'A node located at {self.loc}'
    
class edge_spot(board_spot):
    def __init__(self, loc):
        self.loc = loc
        self.road = []
        
    def __repr__(self):
        return f'An edge located at {self.loc}'
    
    
        
    
        
