# from flask import Flask, redirect, url_for
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# @app.route('/<name>')
# def user(name):
#     return f"hello{name}!"
#
#
# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))
#
#
# if __name__ == '__main__':
#     app.run()

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
