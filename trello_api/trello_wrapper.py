import requests             #to send API requests
import os 

class trello_wrapper:
    def __init__(self, key, token):
        self.query = {
            "key": os.environ.get("TRELLO_KEY"),
            "token": os.environ.get("TRELLO_TOKEN")
        }
        
        #headers for a request
        self.headers = {
            "Accept": "application/json"
        }

        #some useful endpoints
        self.boards_list_url = "https://api.trello.com/1/boards/{}/lists"
        self.board_labels = "https://api.trello.com/1/boards/{}/labels"
        self.cards_url = "https://api.trello.com/1/cards"