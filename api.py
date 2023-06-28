import requests, befrest
import mysql.connector

previous_bitcoin_value = 5000000



def get_data(api):
        response = requests.get(api)
        if response.status_code == 200:
            print("sucessfully fetched the data")
            kooneJavadi = response.json()
            return kooneJavadi
        else:
            print(f"Dadash ridi, there's a {response.status_code} error with your request")

coins_link = "http://localhost:8000/api/data/"
coins_list = get_data(coins_link)
for coin_name in coins_list:
    if coin_name == "bitcoin":
        coin_detail = get_data(coins_link + coin_name)
        for key in coin_detail:
            if key == "value":
                if coin_detail[key] < previous_bitcoin_value:
                    befrest.send_message("khosiamir1@gmail.com", "Dadash nanat dare gaeede mishe!!!")
                print(previous_bitcoin_value)
                previous_bitcoin_value = coin_detail[key]
                print(previous_bitcoin_value)
