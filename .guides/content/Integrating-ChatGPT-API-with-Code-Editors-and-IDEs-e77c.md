Let's tackle how to integrate the ChatGPT API with popular code editors and Integrated Development Environments (IDEs) to provide AI-powered assistance directly within your preferred coding environment. We will go over how to do it with jupyter the concepts can be applied to other environments as well.

For our first example, we can tackle the integration using **Jupyter**. 

Before we get started, if for some reason Jupyter is not open on the left panel please refresh your page. 

**Jupyter** is an open-source web application that allows users to create and share documents containing live code, equations, visualizations, and narrative text. To integrate the ChatGPT API with Jupyter, follow these steps:

Before we get started, if for some reason Jupyter is not open on the left panel please refresh your page. 

Ensure that you have the required Python libraries installed (openai and ipywidgets). If not, you can install them using pip.  Run the following command in Jupyter:

```python
!pip3 install openai
!pip3 install --upgrade openai
!pip3 install openai ipywidgets
```
 after running the following command you can import the necessary libraries in the Jupyter notebook. 

```python
import openai
import ipywidgets as widgets
from IPython.display import display
```

Next we can set our API key.
```
openai.api_key = "your_api_key_here"
```
To retrieve your API key you can go click on `Codio ->preferences -> environmental variable.`

![codioTOkey](codioTOkey.gif)

After retrieving your key you can copy and paste it as the value for the `openai.api_key`.

Now that we have all the tools needed we can start interacting with the API inside Jupyter. 

Lets create a function to call the ChatGPT API:
```
def chatgpt_query(prompts):
    # example of generating a completion
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompts,
      max_tokens=60
)
    return(response['choices'][0]['text'].strip())
```


Create a simple interactive widget to interact with the ChatGPT API:

```python
input_widget = widgets.Textarea(placeholder="Enter your question or prompt here...")
output_widget = widgets.Label()
submit_button = widgets.Button(description="Submit")

def on_submit(_):
    prompt = input_widget.value
    response = chatgpt_query(prompt)
    output_widget.value = response

submit_button.on_click(on_submit)

display(input_widget)
display(submit_button)
display(output_widget)

```

you can access ChatGPT API assistance within Jupyter by typing a question or prompt into the input widget and pressing Enter. The AI-generated response will appear below the input widget. we've added a submit_button widget. The on_click method is used to bind the on_submit function to the button. When you click the "Submit" button, the ChatGPT API query will be executed, and the response will be displayed in the output_widget.


### Other IDEs
The concepts  being applied to other environments.

**Atom Integration:**
Atom is another widely used open-source code editor with a strong community and a rich ecosystem of packages. To integrate the ChatGPT API with Atom, follow these steps:

1. Install the "chatgpt-api-client" package from the Atom package manager.
2. Configure the package by providing your ChatGPT API key.
3. Set up key bindings or commands to access the ChatGPT API from within the editor.
After the integration is complete, you can access ChatGPT API assistance within Atom using the configured key bindings or commands.

**Sublime Text Integration:**
Sublime Text is a lightweight, fast, and customizable code editor popular among developers. To integrate the ChatGPT API with Sublime Text, follow these steps:

1. Install the "ChatGPT API Client" package using Package Control, the Sublime Text package manager.
2. Configure the package by providing your ChatGPT API key.
3. Set up key bindings or commands to access the ChatGPT API from within the editor.


{Check It!|assessment}(fill-in-the-blanks-688923000)
