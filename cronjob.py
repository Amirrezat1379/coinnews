import requests, befrest
import mysql.connector

previous_bitcoin_value = 5000000



mycursor = mydb.cursor()
mydb.commit()
price_insert_sql = "INSERT INTO price (coin_name, time_stamp, coin_price) VALUES (%s, %s, %s)"
alert_insert_sql = "INSERT INTO alert_subscriptions (email, coin_name, differencepercentage) VALUES (%s, %s, %s)"
alert_select_sql = "SELECT * FROM alert_subscriptions WHERE differencepercentage < 0"

def get_data(api):
        response = requests.get(api)
        if response.status_code == 200:
            salap = response.json()
            return salap
        else:
            print(f"Dadash ridi, there's a {response.status_code} error with your request")

coins_link = "http://localhost:8000/api/data/"
coins_list = get_data(coins_link)
for coin_name in coins_list:
    coin_detail = get_data(coins_link + coin_name)
    mycursor.execute(price_insert_sql, (coin_name, coin_detail["updated_at"][:-1], coin_detail["value"]))
    mydb.commit()
    mycursor.execute(alert_insert_sql, ("khosiamir1@gmail.com", coin_name, str(float(coin_detail["roc"]) * 100)))
    mydb.commit()
    
mycursor.execute(alert_select_sql)
myresult = mycursor.fetchall()
for result in myresult:
    befrest.send_message(result[0], f"{result[1]}et be chokh raft!")
    print(myresult)

