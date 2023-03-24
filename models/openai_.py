import base

import openai


class ModelOpenAI(base.Model):

    def __init__(self, api_key, model_id):
        openai.api_key = api_key
        self.id = model_id

    def prompt(self, text, max_tokens, n= 1, temperature= 1.0):
        response = openai.Completion.create(
            engine= self.id,
            prompt= text,
            max_tokens= max_tokens,
            n= n,
            temperature= temperature,
            stop= None,
        )
        return [choice.text.strip() for choice in response.choices]


# Test
if __name__ == "__main__":
    model = ModelOpenAI("", "text-davinci-002")
    prompt_text = "Once upon a time"
    completions = model.prompt(prompt_text, 100, n= 3)
