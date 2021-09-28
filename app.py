from flask import Flask
from flask import request
import subprocess
from secrets_manager import get_secret

app = Flask(__name__)

api_key = get_secret()


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/ping")
def ping():
    ip = request.args.get('ip')
    result = subprocess.check_output(["ping", "-c 2", ip])
    return result

@app.route("/very-secret")
def very_secret():
    secret_key = "bcc286bbbe4353e6a97ae169729ed4a5"
    return f"""
    The key is: {secret_key}
    """

@app.route("/best-secret")
def best_secret():
    return api_key


if __name__ == '__main__':
    app.run(host='0.0.0.0') 
