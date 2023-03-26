"""
Moving cards between lists using card ID 
"""

import requests

def move_card(self, card, new_board):
    additional_params= {
        "idBoard": new_board["id"]
    }

    update_card= requests.put