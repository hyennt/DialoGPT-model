# SETTING UP PROJECT


## Install Pytorch
```
pip3 install torch torchvision torchaudio
```

## Install Transformers Hugging_Face 
### Starting create new env in project directory 
```
python -m venv .env
```
### Activate Virtual environment on MACOS
```
source .env/bin/activate
```
### Activate Virtual environment on Windows
```
.env/Scripts/activate
```
### Install Transformers
```
pip install transformers
```

### References : 
https://www.thepythoncode.com/article/conversational-ai-chatbot-with-huggingface-transformers-in-python

## Summary:

- Introduction to HuggingFace Transformer + how to setup environment
- Import `AutoTokenizer, AutoModelForCausalLM` and `torch` library from huggingface transformers.
    
    ```python
    # model_name = "microsoft/DialoGPT-large"
    model_name = "microsoft/DialoGPT-medium"
    # model_name = "microsoft/DialoGPT-small"
    ```
    
    - There are 3 versions of **DialoGPT**  including small, medium, large ( In this project , I will train medium models instead of 5GB large models, using PyCharm IDE )

## Report Details 
https://wiry-maxilla-d9c.notion.site/Conversional-AI-ChatBot-8726b0deaa614cddb151167aecb5feb5

## Link video for demo:
https://drive.google.com/drive/folders/1N7oamXvjzXTJmeIL9wGEQDza1cAHFB_9
