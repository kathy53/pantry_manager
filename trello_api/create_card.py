"""
Function to create a card  on a list and know the ID
"""

import requests

def create_card(self, board_list, labels, card_name, description):
    additional_params = {
        "idList": board_list["id"],
        "name": card_name,
        "idLabels": labels,
        "desc": description
    }

    new_card =requests.post(
        self.cards_url,
        headers= self.headers,
        params = {**self.query, **additional_params}
    )

    return new_card.json()