# Cashapp Payment Tracker Sellix
Tracks all the cashapp payments in a sellix shop using webhooks.
Commands:
- /balance: Check the current balance.
- /reset: Reset the current balance.

How to setup webhook?
- Download ngrok and authorise your account by following the steps on their website.
- Run the command `ngrok http 6969` to open the 6969 port.
- Copy the `Forwarding` URL.
- Go to https://dashboard.sellix.io/developer/webhooks/all. Click on `Add Webhooks Endpoint`.
- Type: `Sellix`, Webhook URL: `The URL you copied/cashapp`, Event: `Order:Paid`.
- Click on `Add Webhook Endpoint`

How to start the bot?
- Install python, open the terminal and type `pip install -r requirements.txt`
- Then type `python main.py`

OR

- Go to `releases` and download the compiled version.
- Run `main.exe`

P.S:
- Please leave a star for my efforts of explaining to so well :)
- log.py is just print because I don't want the logs with skids
- I know the code is bad but I made it in 20 minutes.
- This is the best I can explain, please do not DM me for help.
