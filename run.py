import numpy as np
import datetime as dt
import json

class DiscoveryGenerator():
    def __init__(self):
        self.prompts = self.load_prompts()
        self.date = dt.datetime.now().date()

    def load_prompts(self):
        with open('prompts.json') as f:
            prompts = json.load(f)
        return prompts['prompts']

    def choose(self):
        prompt = np.random.choice(self.prompts)
        return prompt

if __name__ == '__main__':
    prompts = DiscoveryGenerator()
    prompt = prompts.choose()
    print(prompt)
    print("What's an action that you could take to make this a reality?")
    today = dt.datetime.now().date()
    print('{} {}, {}'.format(today.strftime("%B"), today.strftime("%d"), today.strftime("%Y")))
