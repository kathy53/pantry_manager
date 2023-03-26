"""
Function to retrieve a trello list
"""
import requests
def get_one_list(self, board, name):
    board_lists = requests.get(
        self.boards_list_url.format(board["id"]),
        headers= self.headers,
        params =self.query
    )
    board = [board_list for board_list in board_lists.json() if board_list["name"] == name]

    return board[0]