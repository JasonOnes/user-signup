""" simple sign-up page with password confirmation and email with feedback """
import re
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def sign_up():
    """ renders sign up form view"""
    return render_template("index.html")

@app.route("/form_inputs", methods=['POST'])
def print_form_values():
    """just a check to see form keys"""
    resp = " "
    for field in request.form.keys():
        resp += "<br>{key}</br>: {value}</br>".format(key=field, value=request.form[field])
    return resp

@app.route("/confirm", methods=['POST'])
def confirm():
    """checks to see if inputs valid if so return confirmation view"""
    name = request.form['username']
    psw = request.form['passw']
    con_psw = request.form['conf_pass']
    email = request.form['email']
    match = re.compile(r"[^\s-]{3,21}")
    match_name = match.fullmatch(name)
    match_psw = match.fullmatch(psw)
    if not match_name:
        error = "no spaces allowed and must be between 3 and 20 chars"
        return render_template("index.html", email=email, error1=error)
    elif not match_psw:
         error = "no spaces allowed and must be between 3 and 20 chars"
         return render_template("index.html", username=name, email=email, error2=error)
    elif psw != con_psw:
        error = "Passwords didn't match!!"
        return render_template("index.html", username=name, email=email, error3=error)
    elif email:
        match_pat = re.compile(r"[^@]+@[^@]+\.[^@]+") 
        match = match_pat.match(email)
        error = "Not a valid email address!"
        msg = render_template("index.html", username=name, error4=error)
        if not match or len(email) not in range(3, 21):
            return msg
        else:
            return render_template("confirm.html", name=name)
    else:
        return render_template("confirm.html", name=name)

app.run()
