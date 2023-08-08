We will explore how to integrate the ChatGPT API with **GitHub** to improve collaboration and streamline workflows. GitHub, a popular platform for version control and project management, can benefit from ChatGPT's capabilities to enhance various aspects of project management and development. This integration can provide intelligent suggestions for code, help with documentation, and assist in code review processes. In this tutorial, we will demonstrate how to use the ChatGPT API within a GitHub Actions workflow to automate some of these tasks.


**Step 1**: Create a New Repository
Create a new directory on your local machine and initialize it as a Git repository:

Use the terminal for the following: 
```bash
mkdir my_project
cd my_project
git init
```

**Step 2**: Create the GitHub Actions Workflow
1. In your local Git repository, create a directory for GitHub Actions:
```
mkdir -p .github/workflows
```

2. Create a new YAML file for the ChatGPT integration workflow:
```bash
touch .github/workflows/chatgpt_integration.yml
```
For this page as you run the `touch` command to run your code, it will create a new file. You can access those file by clicking on the file button ->open file then you type in the file name you want to open. In the following case it should be `chatgpt_integration.yml`.

Once Open paste the following inside the text area:
```YAML
name: ChatGPT Integration

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  chatgpt_integration:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install openai

    - name: Run ChatGPT API integration
      run: python chatgpt_integration.py
      env:
        OPENAI_KEY: "${{ secrets.OPENAI_KEY }}"
```


**Step 3**: Create the ChatGPT API Integration Script
1. In your local Git repository, create a new Python file:
```python
touch chatgpt_integration.py
```


1. Open the `chatgpt_integration.py` file and add the following content:
```python
import openai
import os

# Initialize the OpenAI API
openai.api_key = os.getenv('OPENAI_KEY')

def chatgpt_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return (response['choices'][0]['message']['content'].strip())
    #assistant_message = [msg for msg in response['choices'][0]['messages'] if msg['role'] == 'assistant']
    #return assistant_message[0]['content']

# Example: Get a code suggestion from ChatGPT
code_suggestion_prompt = "Write a Python function to calculate the factorial of a number using recursion."
code_suggestion = chatgpt_prompt(code_suggestion_prompt)
print("Code Suggestion:")
print(code_suggestion)
```
**Step 4:** Commit Changes and  Push to GitHub
1. Stage the files for commit:
```
git add .
```
2.Commit changes
```
git commit -m "Initial commit with ChatGPT integration."
```

3. Create a new repository on GitHub. You can do this by visiting https://github.com/new and following the instructions. Do not initialize the new repository with a README, .gitignore, or License. This empty repository will receive the contents of your local repository.

4. Once your new GitHub repository is created, you'll be shown a repository URL. It will look like this: https://github.com/<username>/<repository>.git. Copy this URL, replace <username> and <repository> with your GitHub username and repository name, and run the following commands:
```
git remote add origin git@github.com:<username>/<repository>.git
git branch -M main
git push -u origin main
```

You now have a new GitHub repository with a GitHub Actions workflow that integrates with the ChatGPT API! Please remember to add your OpenAI API key to the GitHub repository secrets. You can do this by going to your GitHub repository, clicking on **"Settings" -> "Secrets" -> "New repository secret"**, then adding "OPENAI_KEY" as the name and your actual OpenAI API key as the value.

Please note that to use SSH with GitHub, you must have an SSH key set up on your GitHub account. You can find out how to do this in the GitHub Docs [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).


{Check It!|assessment}(multiple-choice-1003522885)
