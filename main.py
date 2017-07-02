# simple sign-up page with password confirmation and email with feedback

from flask import Flask, redirect, render_template, request
#import cgi


app = Flask(__name__)
app.config['DEBUG']= True

@app.route("/", methods=['GET','POST'])
def sign_up():
    return render_template("index.html")

@app.route("/confirm", methods=['GET','POST'])
def confirm():
    name = request.form['username']
    psw = request.form['passw']
    #con_psw = request.form['conf_pass']
    con_psw = request.form.get('conf_pass')
    email = request.form['email']
    if len(name) not in range(3, 21):
        error = "Username must be at least 3 characters and no more than 20."
        #print(error)
        return render_template("index.html", error=error)
        #return render_template("index.html", username=error)
    # elif len(psw) not in range(3, 21):
    #     error = "Passwords must be at least 3 chars and no more than 20."
    #     return render_template("index.html", passw=error)
    # elif " " in name:
    #     error = "spaces not allowed"
    #     return render_template("index.html", username=error)
    # elif " " in psw:
    #     error = "no spaces allowed in password"
    #     return render_template("index.html", passw=error)
    # elif psw != con_psw:
    #     error = "Passwords must match."
    #     return render_template("index.html", conf_pass=error)
    # elif email:
    #     error = "Not a valid email address!"
    #     if "@" not in email:
    #         return render_template("index.html", email=error)
    #         #more criteria here, use regex?        
    else:
        return render_template("confirm.html", name=name)


app.run()