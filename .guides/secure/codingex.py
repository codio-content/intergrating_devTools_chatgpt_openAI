import os
import openai
import sys
sys.path.insert(1, '/home/codio/workspace')
import secret
openai.api_key=secret.api_key
import exerc  # import the module containing the student's work

def test_chatgpt_code_review():
    # Create a path to the file
    file_path = os.path.join(os.getcwd(), 'temp.py')

    # Call the function with the file path
    result = exerc.chatgpt_code_review(file_path)

    # Check the type of result and that it's not an error message
    assert isinstance(result, str), "Function should return a string"
    assert not result.startswith('File not found.'), "Function should find the file"
    assert not result.startswith('Exception'), "Function should not raise an exception"

    print("All tests passed.")

if __name__ == "__main__":
    test_chatgpt_code_review()