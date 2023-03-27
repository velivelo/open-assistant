from __future__ import annotations

from .base import Model

import openai


class ModelOpenAI(Model):

    def __init__(self, id: str, api_key: str):
        """
        :param id: OpenAI model ID
        :param api_key: OpenAI API key"""
        super.__init__(id)
        openai.api_key = api_key

    def prompt(self, text: str, max_tokens: int):
        response = openai.Completion.create(
            engine= self.id,
            prompt= text,
            max_tokens= max_tokens,
            n= 1,
            temperature= 1.0,
            stop= None,
        )
        return { 
            "text": response.choices[0].text,
            "tokens": response.choices[0].tokens
        }

    def learn(self, plugin: Plugin):
        data = [line for line in plugin.getData()]
        response = openai.Dataset.create(data= data)
        dataset_id = response["id"]
        print("A fine-tuning job has been created. dataset_id: " + dataset_id)
