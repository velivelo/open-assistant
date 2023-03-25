from plugin import Plugin


class Assistant:

    def __init__(self, id, model) -> None:
        self.id = id
        self.model = model
        self.plugins = []

        with open("system.txt", "r") as f:
            self.system = f.read()
    
    def addPlugin(self, plugin: Plugin) -> None:
        """Fine-tune the model so it learns the plugin.
        """
        self.model.learn(plugin)
        self.plugins.append(plugin)
    
    def prompt(self, text: str) -> None:
        return self.model.prompt(self.system, text, 1000)