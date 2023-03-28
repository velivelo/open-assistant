from open_assistant import Assistant, Plugin, Chat, Message, Author
from open_assistant.models import ModelOpenAI

import os


if __name__ == "__main__":
    PLUGINS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "plugins")

    plugin_time = Plugin(os.path.join(PLUGINS_PATH, "time"))
    print(plugin_time.getSize())
    print([line for line in plugin_time.readData()])

    model = ModelOpenAI("APIKEY", "chat-gpt-4")
    ass = Assistant("Ass", model)
    chat = Chat("chat 1", ass)

    # ass.addPlugin(plugin_time)

    while True:
        user_input = input("> ")
        if user_input == "":
            break
        response = ass.prompt(chat, user_input, debug= True)
        chat.history.extend([Message(user_input, Author.USER), Message(response["text"], Author.ASSISTANT)])
        print(response["text"])