import os
import json


class Plugin:

    def __init__(self, path: str) -> None:
        self.path = path
        self.path_data = os.path.join(path, "data")

        with open(os.path.join(self.path, "manifest.json"), "r") as f:
            self.manifest = json.load(f)
    
    def readData(self):
        self.path_data = os.path.join(self.path, "data")
        files = os.listdir(self.path_data) # all .jsonl
        for file in files:
            with open(os.path.join(self.path_data, file), "r") as f:
                for line in f:
                    yield json.load(line)