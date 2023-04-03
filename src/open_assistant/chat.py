from __future__ import annotations

import time
from enum import Enum


class Author(Enum):
    USER = 0
    ASSISTANT = 1


class Message:

    def __init__(self, text: str, author: Author):
        self.text = text
        self.author = author
        self.timestamp = time.time()
        

class Chat:

    def __init__(self, id: str, assistant: Assistant):
        self.id = id
        self.history: list[Message] = []
    
    def getHistory(self, user_prefix= "", user_suffix= "\n", assistant_prefix= "", assistant_suffix= "\n"):
        """Get the chat history in a formated way.
        """
        history = ""
        for chat in chat.history:
            if chat.author == Author.USER:
                history += user_prefix + chat.text + user_suffix
            else: # chat.author == Author.ASSISTANT
                history += assistant_prefix + chat.text + assistant_suffix
        return history
