from flask import render_template

def resiter_routes(app):
    @app.route("/")
    def home():
        return render_template("Home.html")
