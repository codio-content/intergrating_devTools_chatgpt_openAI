import os
import openai
import secret
# CODIO SOLUTION BEGIN 
openai.api_key=secret.api_key

def chatgpt_code_review(file_path):
    # Check if file exists
    if not os.path.isfile(file_path):
        return "File not found."
    
    # Open the file and read the code
    with open(file_path, 'r') as file:
        code = file.read()

    # Send the code for review
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a code review assistant that provides feedback and suggests improvements for Python code."},
                {"role": "user", "content": code},
            ],
        )
        # Return the assistant's reply
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)

# CODIO SOLUTION END 

