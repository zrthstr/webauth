from flask import Flask, jsonify, render_template

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
#from flask_jwt_extended import unset_jwt_cookies
#from flask_jwt_extended import set_access_cookies

app = Flask(__name__)

app.config["JWT_TOKEN_LOCATION"] = ["headers"]
app.config["JWT_SECRET_KEY"]="INSECURE_IF_NOT_CHANGED_AND_SECRET"

jwt = JWTManager(app)


@app.route("/login_with_headers", methods=["POST"])
def login_with_headers():
    access_token = create_access_token(identity="some_id")
    return jsonify(access_token=access_token)


@app.route("/protected", methods=["GET", "POST"])
@jwt_required()
def protected():
    return jsonify(something="somethingelse")


#@app.route("/")
#def index():
#    return """<a href="/protected"> protected </a> <br> <a href="/login"> login </a>"""


@app.route("/")
def login():
    #return render_tempalte("login.html", form=form)
    return render_template("login.html")


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
