"""
Function to retrieve one label from a given list
"""
import requests
def get_one_board_labels(self, board, label_name):
    labels = requests.get(
        self.board_labels.format(board["id"]),
        headers =self.headers,
        params =self.query
    )

    label = [board_label for board_label in labels.json() if board_label["name"] == label_name]
    return label[0]