
class Plugin:

    def __init__(self, path: str) -> None:
        self.path = path


class APICaller:
    
    format = r"$[(?P<data_name>=.+) (?P<api_address>.+)]"


class Assistant:

    def __init__(self) -> None:
        self.plugins = []
    
    def learnPlugin(self, plugin: Plugin) -> None:
        pass
    
    def prompt(self, prompt: str) -> None:
        system = \
"""Tu es un assistant virtuel."""