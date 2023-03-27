from __future__ import annotations

from .base import Model

import openai


class ModelOpenAI(Model):

    def __init__(self, id: str, api_key: str):
        """
        :param id: OpenAI model ID
        :param api_key: OpenAI API key
        """
        super.__init__(id)
        openai.api_key = api_key

    def prompt(self, text: str, max_tokens: int) -> dict:
        response = openai.Completion.create(
            engine= self.id,
            prompt= self.system + text,
            max_tokens= max_tokens,
        )
        return { 
            "text": response.choices[0].text,
            "usage": response.usage # prompt_tokens, completion_tokens, total_tokens
        }

    def learn(self, plugin: Plugin):
        data = [line for line in plugin.getData()]
        response = openai.Dataset.create(data= data)
        dataset_id = response["id"]

        response = openai.FineTuning.create(
            model= "text-davinci-003",
            dataset_id= dataset_id,
            n_epochs= 1,
            learning_rate= "1e-5",
            batch_size= 4,
            num_warmup_steps= 10,
        )
        fine_tuning_id = response["id"]

        print(f"A fine-tuning job has been created. dataset_id= {dataset_id}, fine_tuning_id= {fine_tuning_id}")
