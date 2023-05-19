import flask, json, requests, threading, datetime
from colorama import Fore, Style
from flask import request
from log import *

app = flask.Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)




def update_json(balance):
    
    json_object = json.dumps(balance, indent=4)
    with open("balance.json", "w") as outfile:
        outfile.write(json_object)



@app.route("/cashapp", methods=["GET", "POST"])
def add_to_bal():
    
    data = request.json
    
    if data['data']['gateway'] == "CASH_APP":
        balance = json.load(open("balance.json", encoding="utf-8"))
        amount = data['data']['total']
        balance['current_balance'] = balance['current_balance'] + amount
        update_json(balance)
        info(f"[+]", f"Added ${amount} to balance")
        open("logs.txt", "a").write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}|[+] Added ${amount} to balance\n")
        
    return '{"status": "received"}', 200 

def run():  
    app.run(host="0.0.0.0", port="6969")
    
def keep_alive():
    t = threading.Thread(target=run)
    t.start()

