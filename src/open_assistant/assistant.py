from .models import Model
from .plugin import Plugin

import pkg_resources
import json


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
    
    def addPlugin(self, plugin: Plugin):
        """Fine-tune the model so it learns the plugin.
        :param plugin: Plugin object
        """
        self.model.learn(plugin)
        self.plugins.append(plugin)
    
    def prompt(self, text: str, max_tokens= 4096, max_steps= 2, debug= False) -> dict:
        """
        :param text: Text to prompt the model
        :param max_tokens: Maximum number of total tokens (prompt + completion)
        :param max_steps: Maximum number of steps to try to get a response
        :param debug: If True, the model will print the debug texts
        :return: Dictionary with "text" and "usage" keys
        """
        # TODO: voir pr ajouter User : et You : dans le prompt
        # TODO: enlever du system la fin
        # TODO: gérer la mémoire, cad qu'il faut retenir les échanges précédents (pas garder les étapes actions, juste les textes)

        for i in range(max_steps): 
            prompt_formated = "User :\n" + json.stringify({
                "prompt": text,
            }) + "\nYou :\n"

            response = self.model.prompt(prompt_formated, max_tokens)
            completion_obj = json.loads(response["text"]) # if error it means the model doesn't understand how to respond
            
            if "completion" in completion_obj:
                return {
                    "text": completion_obj["completion"],
                    "usage": 0, # sum of all usage
                }
            
            locals_ = {}
            if "actions" in completion_obj: # there should be actions if no completion
                for action in completion_obj["actions"]:
                    locals_[action["id"]] = None # TODO: implement actions
            
            prompt_obj_str = json.stringify({
                "locals": locals_,
                "prompt": text,
            })

        return {
            "text": f"The assistant failed to figure a response in {max_steps} steps.",
            "usage": 0,
        }
            

                
            
            
        
        