# GenAI Stack UI 

This package is for the chat interface of the LLM stack. 

# Installation steps

1. Clone the repository

```
git clone https://github.com/aiplanethub/genai-stack.git
```

2. Create a new virtualenv and activate it.
```
python -m venv ./genai-stack-ui
source ./genai-stack-ui/bin/activate
```

3. Install the requirements 
```
pip install -r ui/requirements.txt
```

4. Run the streamlit app
```
streamlit run ui/app/main.py
```