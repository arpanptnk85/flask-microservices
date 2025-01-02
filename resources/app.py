import socket
from flask import Flask
from flask import jsonify, render_template

app = Flask(__name__)

# Fucntion to get the host and ip
def getHostDetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

@app.route("/", methods=["GET"])
def hello():
    return "<p>Hello, World!</p>"

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="UP")

@app.route("/home", methods=["GET"])
def home():
    host_name, host_ip = getHostDetails()
    return render_template('index.html', host=host_name, ip=host_ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)