"""
Function to retrieve the board ID
This info is stored among a lot of info into the board-URL plus ".json"

"""
import requests
def get_board(self, board):
    board =requests.get(
        f"{board}.json",
        headers = self.headers,
        params =self.query
    )

    return board.json()