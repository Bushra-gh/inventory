from flask import Flask, render_template, redirect, request
from flask import current_app as app
from .models import *

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form.get("pwd")
        this_user = User.query.filter_by(username=username).first()
        if this_user:
            if this_user.password == pwd:
                if this_user.type == "manager":
                    return redirect("/manager")
                else:
                    return render_template("user_dashboard.html", this_user=this_user)
            else:
                return render_template("incorrect_p.html")
        else:
            return render_template("not_exist.html")
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    return render_template("register.html")