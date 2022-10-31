from flask import Flask
from flask_login import LoginManager
from views import views
from auth import User
from Database.users import get_user_by_id
from config import SECRET_KEY

app = Flask(__name__)

app.secret_key= SECRET_KEY

app.register_blueprint(views, url_prefix='/')

#set up
login_manager=LoginManager()
#link it to our app
login_manager.init_app(app)
#redirecting if user tries to access something they're not allowed
login_manager.login_view = "/login"
#what message to show after redirecting
login_manager.login_message='Please login to view this page'
#if error
login_manager.login_message_category='error'


#retrieving the user based on the User ID from the cookie & decripts it
@login_manager.user_loader
def user_loader(user_id):
    user_details = get_user_by_id(user_id)
    if user_details is None:
        return None
    user = User(user_details) # create a user and return it
    return user


if __name__ == '__main__':
    app.run(debug=True, port=5009)

