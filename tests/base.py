from open_assistant import Assistant, Plugin
from open_assistant.models import ModelOpenAI

import os


if __name__ == "__main__":
    PATH = os.path.dirname(os.path.abspath(__file__))
    PLUGINS_PATH = os.path.join(PATH, "plugins")

    model = ModelOpenAI("APIKEY", "chat-gpt-4")
    ada = Assistant("Ada", model)

    plugin_time = Plugin(os.path.join(PLUGINS_PATH, "time"))
    ada.addPlugin(plugin_time)