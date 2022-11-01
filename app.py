#creating the server for the job engine application

from flask import Flask, render_template, url_for
from views import views
from config import SECRET_KEY


app= Flask(__name__)
app.register_blueprint(views, url_prefix='/')
app.secret_key = SECRET_KEY

if __name__=="__main__":
    app.run(debug=True)


