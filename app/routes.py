from flask import render_template, request

def resiter_routes(app):
    @app.route("/")
    def home():
        return render_template("Home.html")
    
    @app.route("/signup", methods = ['GET','POST'])
    def signup():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            
            
        return render_template("signup.html")
    
    @app.route("/login", methods = ['GET','POST'])
    def login():
        return render_template("login.html")