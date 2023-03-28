import os
import json
from typing import Generator


class Plugin:
    """A plugin is a knowledge base for an assistant.
    It contains a set of data in the form of input/output pairs.
    It is used to teach an assistant about general knowledge, api documentations, system commands, etc.
    """

    def __init__(self, path: str):
        """
        :param path: Path to the plugin folder
        """
        self.path = path
        self.path_data = os.path.join(path, "data")

        with open(os.path.join(self.path, "manifest.json"), "r") as f:
            manifest = json.load(f)

        self.name = manifest["name"]
        self.version = manifest["version"]
        self.description = manifest["description"]
        self.author = manifest["author"]
    
    def getSize(self) -> dict:
        """
        :return: Dictionary with "lines" and "tokens" keys
        """
        lines = 0
        tokens = 0
        for line in self.readData():
            lines += 1
            tokens += len(line["input"].split(" "))
            tokens += len(line["output"].split(" "))
        return {
            "lines": lines,
            "tokens": tokens,
        }

    def readData(self) -> Generator:
        """
        :return: Generator of dictionaries with "input" and "output" keys
        """
        files = os.listdir(self.path_data) # all .jsonl
        for file in files:
            with open(os.path.join(self.path_data, file), "r") as f:
                for line in f:
                    yield json.loads(line)