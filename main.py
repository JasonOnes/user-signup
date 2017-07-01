# simple sign-up page with password confirmation and email with feedback

from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config['DEBUG']= True

@app.route("/", methods=['GET','POST'])
def sign_up():
    return render_template("index.html")

@app.route("/confirm", methods=['POST'])
def confirm():
    name = request.form.get('username')
    psw = request.form.get('passw')
    con_psw = request.form.get('conf_pass')
    if psw == con_psw:
        return render_template("confirm.html", name=name)
    else:
        # error = "Passwords do not match!"
        #return redirect("/", username=name, passw=psw, conf_pass="")
        return render_template("index.html", username=name)#, 'username'=name, passw=psw, conf_pass = '' ) #+ error 



app.run()