import os
import wavio
import uvicorn
from io import BytesIO
from models.tts import TTSModel
from fastapi import FastAPI, Response, HTTPException


app = FastAPI()

female_model_path = "models/female"
male_model_path = "models/male"

female = TTSModel(
    os.path.join(female_model_path, "tts.saved_model"),
    os.path.join(female_model_path, "vocoder.saved_model")
)

male = TTSModel(
    os.path.join(male_model_path, "tts.saved_model"),
    os.path.join(male_model_path, "vocoder.saved_model")
)

def generate_audio(tts):
    audio = BytesIO()
    wavio.write(audio, tts, 22050, sampwidth=3)
    audio.seek(0)
    return audio.read()

@app.get("/predict/")
async def inference(text: str, voice: str, speed: float = 1.0):
    if text:
        if voice.lower() == "female":
            tts = female(text, speed=speed)
            audio = generate_audio(tts)
        elif voice.lower() == "male":
            tts = male(text, speed=speed)
            audio = generate_audio(tts)
        else:
            raise HTTPException(status_code=400, detail="Bad Request")
    else:
        raise HTTPException(status_code=400, detail="Bad Request")

    return Response(audio, media_type="audio/wav")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)