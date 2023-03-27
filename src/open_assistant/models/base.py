from __future__ import annotations


class Model:

    def __init__(self, id: str) -> None:
        """
        :param id: Model ID
        """
        self.id = id
        self.system = ""
        
    def prompt(self, text: str, max_tokens: int) -> dict:
        """
        :param text: Text to prompt the model
        :param max_tokens: Maximum number of tokens to generate
        :return: Dictionary with "text" and "tokens" keys
        """
        raise NotImplementedError()
    
    def learn(self, plugin: Plugin):
        """
        :param plugin: Plugin object
        """
        raise NotImplementedError()