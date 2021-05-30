import os

from flask import Flask, redirect, render_template, request, flash
from flask_login import login_required, LoginManager, logout_user, login_user

from user import User
from form import LoginForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

## for CSRF tokens
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
    #return 1


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():

        user = load_user(form.username.data)
        if not user:
            return redirect('/login')

        if not user.verify_password(form.password.data):
            return redirect('/login')

        login_user(user)
        flash("Logged in successfully.")

        # this can be a nice vuln open redirect
        #next = flask.request.args.get('next')
        #if not is_safe_url(next):
        #    return flask.abort(400)
        #return flask.redirect(next)

        next = "/protected"
        return redirect(next)

    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/')
def index():
    return """Hello. <a href="/login"> login </a>  or  <a href="/protected"> Go to protected </a>"""

@app.route('/protected')
@login_required
def protected():
    return """<h2>logged in!</h2>  <a href="/logout"> logout </a>"""

if __name__ == "__main__":
    #app.run(ssl_context="adhoc")
    app.run()
