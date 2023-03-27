import os
import json


class Plugin:

    def __init__(self, path: str) -> None:
        self.path = path
        self.path_data = os.path.join(path, "data")

        with open(os.path.join(self.path, "manifest.json"), "r") as f:
            self.manifest = json.load(f)
    
    def getInfos(self):
        lines = 0
        tokens = 0
        for line in self.readData():
            lines += 1
            tokens += len(line["input"].split(" "))
            tokens += len(line["output"].split(" "))
        return {
            "lines": lines,
            "tokens": tokens
        }

    def readData(self):
        files = os.listdir(self.path_data) # all .jsonl
        for file in files:
            with open(os.path.join(self.path_data, file), "r") as f:
                for line in f:
                    yield json.loads(line)