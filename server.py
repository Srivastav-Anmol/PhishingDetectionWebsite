# server.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import API  # Import the function from api.py

app = FastAPI()

class URLInput(BaseModel):
    url:str

@app.post("/classify")
def classify_url(url_input):
    try:
        result = API.get_prediction(url_input.url, model)  # Call the function from ap
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
