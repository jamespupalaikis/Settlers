# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:37:01 2023

@author: James
"""

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


def runstate(state, endpoint, )