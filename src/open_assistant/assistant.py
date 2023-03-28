from .models import Model
from .plugin import Plugin
from .chat import Chat

import pkg_resources
import json
import requests
from urllib.parse import urlparse


class Assistant:

    def __init__(self, id: str, model: Model):
        """
        :param id: Assistant ID
        :param model: Model object
        """
        self.id = id
        self.model = model
        self.model.system = pkg_resources.resource_string("open_assistant", "system_debug.txt").decode("utf-8")
        self.plugins = []
        self.api_keys = {}
    
    def addPlugin(self, plugin: Plugin):
        """Fine-tune the model so it learns the plugin.
        :param plugin: Plugin object
        """
        self.model.learn(plugin)
        self.plugins.append(plugin)
    
    def handleAction(self, action: dict) -> dict:
        """
        :param action: Action dictionary
        :return: Locals disctionary
        """
        headers = { "Content-Type": "application/json" }

        domain = urlparse(action["endpoint"]).netloc
        if domain in self.api_keys:
            headers["Authorization"] = f"Bearer {self.api_keys[domain]}"
        
        response = requests.request(
            url= action["endpoint"],
            method= action["method"],
            headers= headers,
            json= action["json"] if "json" in action else None,
        )

        # TODO: we should teach the model which keys are requested for a precise 
        # request so the big responses don't take too much tokens
        return response.json()


    def prompt(self, chat: Chat, text: str, max_tokens= 4096, max_steps= 2, debug= False) -> dict:
        """
        :param chat: Chat object
        :param text: Text to prompt the model
        :param max_tokens: Maximum number of total tokens (prompt + completion) per step
        :param max_steps: Maximum number of steps to try to get a response
        :param debug: If True, the model will print the debug texts
        :return: Dictionary with "text" and "usage" keys
        """
        # TODO: ajouter le chat history de la conversation dans le système
        prompt_formated = {
            "prompt": text,
        }
        usage = 0

        for i in range(max_steps): 
            response = self.model.prompt(f"User :\n{json.stringify(prompt_formated)}\nYou :\n", max_tokens)
            usage += response["usage"]["total_tokens"]
            completion_formated = json.loads(response["text"]) # if error here -> too bad model
            
            if "completion" in completion_formated:
                return {
                    "text": completion_formated["completion"],
                    "usage": usage,
                }
            
            locals_ = {}
            for action in completion_formated["actions"]: # if error here -> too bad model
                locals_[action["id"]] = self.handleAction(action)
            
            prompt_formated.setdefault("locals", {}).update(locals_)

        return {
            "text": f"I failed to figure a response in {max_steps} steps.",
            "usage": usage,
        }
            

                
            
            
        
        