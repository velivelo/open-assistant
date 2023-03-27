from .plugin import Plugin

import pkg_resources


class Assistant:

    def __init__(self, id, model) -> None:
        """
        :param id: Assistant ID
        :param model: Model object
        """
        self.id = id
        self.model = model
        self.model.system = pkg_resources.resource_string("open_assistant", "system.txt").decode("utf-8")
        self.plugins = []
    
    def addPlugin(self, plugin: Plugin) -> None:
        """Fine-tune the model so it learns the plugin.
        :param plugin: Plugin object
        """
        self.model.learn(plugin)
        self.plugins.append(plugin)
    
    def prompt(self, text: str) -> dict:
        """
        :param text: Text to prompt the model
        """
        return self.model.prompt(text, 1000)