
### Build a Basic Code Review Assistant with the ChatGPT API

Create a function named `chatgpt_code_review` with the following specifications:

* The function should take one argument: a file path.

* This function should use the ChatGPT API to review the code in the file.

* The function should return a string of feedback on the code.

Here is some python that can help with reading a file outline of the function:

```python
# Path to your python file
file_path = code

with open(file_path, 'r') as file:
code = file.read()

```
A `temp.py` file is in the same directory as you `exerc.py` file. Feel free to use it to test your code.
```python
print(chatgpt_code_review("temp.py"))
```
{Try it!}(python3 exerc.py)

**Before submitting, your code remove your print statement.** The submit button will be running your code, we don't want to run it twice which might cause delays and lead to a  `timeout error`.

{Check It!|assessment}(code-output-compare-254856085)