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