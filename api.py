from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import uvicorn
from fastapi.responses import HTMLResponse
import requests
import mysql.connector

previous_bitcoin_value = 5000000



app = FastAPI()
mycursor = mydb.cursor()
mydb.commit()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def file_upload(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})  

# Endpoint to get all alert subscriptions
@app.post("/price")
async def get_price_history(request: Request, coin_name: str = Form(...)):
    mycursor.execute(f"select coin_price from price where coin_name = '{coin_name}'")
    myresult = mycursor.fetchall()
    for res in myresult:
        print(res)
    return {"message": f"{coin_name} price history = {myresult}"}

# Endpoint to create a new alert subscription
@app.post("/Subscribe")
async def subscribe_coin(request: Request, email: str = Form(...), coin_name: str = Form(...), price_change: str = Form(...)):
    # subscriptions.append(subscription) 
    print(email)
    print(coin_name)
    print(price_change)

    mycursor.execute(f"insert into alert_subscriptions values ('{email}', '{coin_name}', {price_change})")
    mydb.commit()
    return {"message": f"{email} + {coin_name} + {price_change} subscriptions"}

# root page where html homepage file is loaded for uploading files(upload_file.html)


if __name__ == "__main__":
    uvicorn.run(app="api:app", host="127.0.0.1", port=8200, reload=True)