from .plugin import Plugin

import pkg_resources


class Assistant:

    def __init__(self, id, model) -> None:
        self.id = id
        self.model = model
        self.plugins = []

        self.system = pkg_resources.resource_string('open_assistant', "system.txt").decode("utf-8")
    
    def addPlugin(self, plugin: Plugin) -> None:
        """Fine-tune the model so it learns the plugin.
        """
        self.model.learn(plugin)
        self.plugins.append(plugin)
    
    def prompt(self, text: str) -> None:
        return self.model.prompt(self.system, text, 1000)