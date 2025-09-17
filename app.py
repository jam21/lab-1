from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DevOps! Connected to Postgres DB at host: " + os.getenv("DB_HOST", "unknown")

@app.route("/new_url")
def new_url():
    return "System response from url /new_url"

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
    "user": os.getenv("DB_USER", "user"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "dbname": os.getenv("DB_NAME", "mydb"),
}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
