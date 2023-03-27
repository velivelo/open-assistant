from .base import Model

import requests


class ModelOpenAI(Model):

    def __init__(self, api_key, id):
        """
        :param api_key: OpenAI API key
        :param id: OpenAI model ID"""
        self.headers = { "Content-Type": "application/json", "Authorization": f"Bearer {api_key}" }

    def prompt(self, system, text, max_tokens):
        response = openai.Completion.create(
            engine= self.id,
            prompt= text,
            max_tokens= max_tokens,
            n= 1,
            temperature= 1.0,
            stop= None,
        )
        return [choice.text.strip() for choice in response.choices]

    def learn(self, plugin):
        """"""
        data = [line for line in plugin.getData()]
        response = requests.post("https://api.openai.com/v1/datasets", headers= self.headers, data= data)

        self.dataset_id = response.json()["id"]




# Test
if __name__ == "__main__":
    model = ModelOpenAI("", "text-davinci-002")
    prompt_text = "Once upon a time"
    completions = model.prompt("", prompt_text, 100, n= 3)
