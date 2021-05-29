from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user": generate_password_hash("123456"),
    "admin": generate_password_hash("admin")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    page =  "Hello, {}!".format(auth.current_user())
    page += """<a href="/logout"> logout </a>"""
    return page

## a http 401 effectively logs a user out
@app.route('/logout')
def logout():
    return "Logout", 401

if __name__ == '__main__':
    app.run()
