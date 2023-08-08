import os
import openai
import secret
openai.api_key=secret.api_key
## Put your code below this line 
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's a good book to read on a rainy day?"}
    ],
  n=3,
  temperature=0.7
)


print(response['choices'][0]['message']['content'])