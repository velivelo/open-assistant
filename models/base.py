class Model:

    def __init__(self) -> None:
        self.id = None

    def prompt(self, text, max_tokens):
        raise NotImplementedError()