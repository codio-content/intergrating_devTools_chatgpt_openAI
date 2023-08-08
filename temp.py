import os
import openai
import secret
openai.api_key=secret.api_key



response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
            {"role": "system", "content": "You are a travel expert specializing in European destinations."},
            {"role":"user","content": "Give me the top 2 tourist destinations in Germany for my honeymoon." }
    ]
)

print(response['choices'][0]['message']['content'])
