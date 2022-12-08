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
        row, col = self.loc
        hexes = hex_spot.hex_adj_hex(row, col)
        
       
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
        self.settled = []
        
    def __repr__(self):
        return f'A node located at {self.loc}'
    
    @staticmethod
    def node_adj_edges(loc):
        

    
class edge_spot(board_spot):
    def __init__(self, loc):
        self.loc = loc
        self.road = []
        
    def __repr__(self):
        return f'An edge located at {self.loc}'
    
    
        
print(sorted(hex_spot.hex_adj_node(4,1))) 
        
