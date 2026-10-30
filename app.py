import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")
APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello from the Python API!")
FEATURE_STATUS = os.getenv("FEATURE_STATUS", "enabled").lower()

@app.get("/")
def home():
    return jsonify({
        "application": "Docker Environment Configuration Demo",
        "status": "running",
        "environment": APP_ENV
    })

@app.get("/config")
def config():
    return jsonify({
        "environment": APP_ENV,
        "message": APP_MESSAGE,
        "feature_status": FEATURE_STATUS
    })

@app.get("/hello")
def hello():
    if FEATURE_STATUS != "enabled":
        return jsonify({
            "environment": APP_ENV,
            "error": "The hello feature is disabled"
        }), 403
    return jsonify({"environment": APP_ENV, "message": APP_MESSAGE})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
