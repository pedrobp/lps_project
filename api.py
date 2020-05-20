from github_webhook import Webhook
from flask import Flask
from webhook_processor import processor

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    db = Processor() # fix later
    db.save_push(data)

if __name__ == "__main__":
    app.run(host="192.168.15.4", port=5000)