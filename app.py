from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/ping")
def ping():
    ip = request.args.get('ip')
    result = subprocess.check_output(["ping", "-c 2", "www.google.com"])
    return result

@app.route("/very-secret")
def very_secret():
    secret_key = bcc286bbbe4353e6a97ae169729ed4a5
    return """
    The key is: %s
    """.format(secret_key)


if __name__ == '__main__':
    app.run(host='0.0.0.0') 
