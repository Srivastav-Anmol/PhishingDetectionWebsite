import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from API import get_prediction

app = FastAPI()

class URLInput(BaseModel):
    url: str

# Load the LightGBM classifier using pickle
print("Loading the model...")
with open('lightgbm_classifier.pkl', 'rb') as file:
    clf = pickle.load(file)

@app.post("/predict")
def predict(data: URLInput):
    url = data.url
    prediction = get_prediction(url, clf)
    return {"prediction": prediction}
