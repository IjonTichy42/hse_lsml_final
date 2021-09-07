from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
import io
import os
import numpy as np
import pandas as pd
import requests
import json
import pickle
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Mount to the scripts in static
# app.mount("/static", StaticFiles(directory="static"), name="static")
# Load the template from specified directory
# templates = Jinja2Templates(directory="templates")

# @app.get("/") # get the url,and call the function on that page
# async def root(request: Request):
#         return templates.TemplateResponse("index.html",
#                 {"request": request}) # Pass a dict for corresponding parameters

@app.post("/predict") # get the url,and call the function on that page
async def predict(request: Request):

    url = f'http://model:5000/invocations'

    body = await request.json()

    to_predict = pd.DataFrame(vectorizer.transform([body["text"]]).toarray().tolist())

    http_data = to_predict[:1].to_json(orient='split')

    response = requests.post(url=url, headers={'Content-Type': 'application/json'}, data=http_data)
    prod_pred = json.loads(response.text)
    return JSONResponse({
        "team": prod_pred[0]
    })
    # return templates.TemplateResponse("main.html",
    #     {"request": request, 'pred': prod_pred[0]})

# @app.get("/solve") # get the url,and call the function on that page
# async def solve(request: Request, pred: str):
#     return {'pred':pred}