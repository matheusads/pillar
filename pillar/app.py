from fastapi import FastAPI
from .models import RequestModel, Order

app = FastAPI()


@app.get("/")
def get_status():
    return {"status": "ok"}


@app.post("/vowel_count/")
def vowel_count(request: RequestModel):
    return {word: len([char for char in word if char in "aeiouAEIOU"]) for word in request.words}
