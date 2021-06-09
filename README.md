# DhivehiTTS-http
Simple FastAPI app to server Dhivehi.ai pretrained TTS models.

## Setup
1. ```git clone https://github.com/ashraq1455/DhivehiTTS-http.git```
2. Download [dhivehi.ai](https://dhivehi.ai/) pre-trained models from [here](https://github.com/DhivehiAI/TTS-Demos)
3. Extract and copy the models to ```models/female/``` and ```models/male/``` directory
4. ```pip install -r requirements.txt```
5. ```python main.py``` to run development server


## Directory Structure
```
|- models/
    |- female/
      |- tts.saved_model
      |- vocoder.saved_model
    |- male/ 
      |- tts.saved_model
      |- vocoder.saved_model
    |- __init__.py
    |- tts.py
|- main.py
```

## How to use
Send a ```GET``` request to ```http://localhost:8000/predict/?text=ހެލޯ ދިވެހި&voice=female&speed=0.9``` 
