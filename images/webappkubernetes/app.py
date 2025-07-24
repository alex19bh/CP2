from flask import Flask, request, jsonify, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json

app = Flask(__name__, template_folder='templates')
auth = HTTPBasicAuth()

# Diccionario de usuarios permitidos
users = {
    "alex": generate_password_hash("alex123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

DATA_FILE = '/data/db.json'

@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
@auth.login_required
def data():
    if request.method == 'POST':
        data = request.json
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f)
        return jsonify({"status": "saved"})
    else:
        if not os.path.exists(DATA_FILE):
            return jsonify({})
        with open(DATA_FILE) as f:
            return jsonify(json.load(f))

if __name__ == '__main__':
    context = ('certs/clave_publica.crt', 'certs/clave_privada.key')
    app.run(host='0.0.0.0', port=443, ssl_context=context)
