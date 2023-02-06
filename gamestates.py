# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:37:01 2023

@author: James
"""
from UIcomprehension import * 

gamestates = {
    'choosing_order':(buttonpush, on_choosing_order),
    'place_initial':(select_node,on_place_initial ),
    'rolling_dice':(buttonpush, on_rolling_dice),
    'waiting_for_discard':(buttonpush, on_waiting_for_discard),
    'choosing_dev_card_to_use':(buttonpush, on_choosing_dev_card_to_use),
    'moving_bandit':(select_node, on_moving_bandit),
    'choosing_victim':(select_player, on_choosing_victim),
    'stealing_card':(select_opp_card, on_stealing_card),
    'postroll_pending':(buttonpush, on_postroll_pending),
    'build_select':(buttonpush, on_build_select),
    'choosing_cityspot':(select_node, on_choosing_cityspot),
    'placing_settlement':(select_node, on_placing_settlement),
    'placing_road':(select_edge, on_placing_road),
    'choosing_tradein':(buttonpush, on_choosing_tradein),
    'picking_cards':(select_my_cards, on_picking_cards),
    'choosing_trade':(buttonpush, on_choosing_trade),
    'trade_offered':(buttonpush, on_trade_offered)
    
    
    }


def runstate(state, inp, data):
    ifunc, ofunc  = gamestates[state][0]
    
    
    #output fuinctions should take the datastruct specifically so that it can
    #implement boardstate and playerstate changes
    
    ofunc(ifunc(inp), data)
    
    #game state is set in the output function
    
    
    
    
    
def placing_settlement(inp, data):
    '''Inp is from  select_node, so it will be a row,column
    the endpoint for this action is postroll_pending'''
    #TODO: I want these functions to interact ONLY with GAME level functions
    #Currently its implemented in the heirarchy hex/node->board->player need to add game at that top level
    #since it has self.turns, self.currentplayer and all that, and use those functions in 
    #these gamestate transition functions
    row, col = inp
    