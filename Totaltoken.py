import openai
import secret
openai.api_key=secret.api_key
## Put your code below this line 




message= [{"role": "system", "content": "You are a helpful assistant."},  
{"role": "user", "content": "Tell me about the history of the Eiffel Tower and its significance."}]



## put yout code above this line 
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=message
)
print(response['usage']['total_tokens'])