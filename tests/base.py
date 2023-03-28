from open_assistant import Assistant, Plugin
from open_assistant.models import ModelOpenAI

import os


if __name__ == "__main__":
    PLUGINS_PATH = os.path.join(os.path.abspath(__file__), "plugins")

    model = ModelOpenAI("APIKEY", "chat-gpt-4")
    ass = Assistant("Ass", model)

    plugin_time = Plugin(os.path.join(PLUGINS_PATH, "time"))
    ass.addPlugin(plugin_time)