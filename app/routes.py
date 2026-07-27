from flask import render_template

def resiter_routes(app):
    @app.route("/")
    def home():
        return render_template("Home.html")
    
    @app.route("/signup", methods = ['GET','POST'])
    def signup():
        return render_template("signup.html")
    
    @app.route("/login", methods = ['GET','POST'])
    def login():
        return render_template("login.html")