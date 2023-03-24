
class Plugin:

    def __init__(self, path: str) -> None:
        self.path = path


class Assistant:

    def __init__(self, id, model) -> None:
        self.id = id
        self.model = model
        self.plugins = []
    
    def addPlugin(self, plugin: Plugin) -> None:
        """Fine-tune the model so it learns the plugin.
        """
        self.modeL.learn(plugin)
    
    def prompt(self, prompt: str) -> None:
        system = \
"""Tu es un assistant virtuel."""
        return self.model.prompt(system + prompt)


if __name__ == "__main__":
    model = Model.fromOpenAI("chat-gpt-4")
    ada = Assistant("Ada", model)

    plugin_time = Plugin("plugins/time")
    ada.addPlugin(plugin_time)