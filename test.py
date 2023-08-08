import os
import openai
import secret
openai.api_key=secret.api_key


prompts =""
### FREEZE CODE BEGIN
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts)

print(response['choices'][0]['text'].strip())
### FREEZE CODE END