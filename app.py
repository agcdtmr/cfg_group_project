from flask import Flask, render_template, redirect, request, flash
from flask_login import LoginManager, current_user, UserMixin, login_user, logout_user, login_required
from Database.users import add_user, email_available, get_user_by_credentials, get_user_by_id
from config import SECRET_KEY
from api import get_from_api

app = Flask(__name__)

app.secret_key= SECRET_KEY

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


#stores the user ID as a cookie

class User(UserMixin):

    def __init__(self, user_details):
        self.id=user_details.get('id') # needs to match the id stored in the cookie
        self.first_name = user_details.get('first_name')
        self.surname = user_details.get('surname')
        self.email=user_details.get('email')

#retrieving the user based on the User ID from the cookie & decripts it
@login_manager.user_loader
def user_loader(user_id):
    user_details = get_user_by_id(user_id)
    if user_details is None:
        return None
    user = User(user_details) # create a user and return it
    return user

@app.get('/')
def view_home():
    return render_template('home.html')

@app.get('/login')
def view_login():
    return render_template('login.html', user=current_user)


@app.post('/login')
def submit_login():
    if not current_user.is_anonymous:
        return redirect('/profile')
    email = request.form.get('email')
    password=request.form.get('password')
    user=get_user_by_credentials(email,password)
    if user is None:
        flash('Invalid credentials', 'error')
    else:
        user = User(user)
        login_user(user)
        return redirect('/profile')
    #in case something has gone wrong
    return redirect('/login')


@app.get('/signup')
def view_signup():
    if not current_user.is_anonymous:
        return redirect('/profile')
    else:
        return render_template('signup.html', user=current_user)

@app.post('/signup')
def submit_signup():
    if not current_user.is_anonymous:
       return redirect('/profile')
    first_name = request.form.get('first_name')
    surname = request.form.get('surname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    if len(password) < 5:
        flash('Passwords should be at least 5 characters long', 'error')
    # email already exists ~THIS DOESN'T FLASH
    elif not email_available(email):
        flash('An account with that email already exists', 'error')
    # they're signed up and they ready to login
    else:
        add_user(first_name, surname,username, email, password)
        flash('New account created.', 'info')
        return redirect('/login')
    # otherwise have try again signing up
    return redirect('/signup')


@app.post('/logout')
@login_required
def submit_logout():
    logout_user()
    return redirect ('/login')

@app.get('/profile')
def view_profile():
    #must add again login_required
    return render_template("profile.html", user=current_user)

######################################

#jobengine - full list button
@app.get('/jobengine')
def job_engine():
    return render_template('jobengine.html')

@app.get('/filter-jobs')
def job_search():
    return render_template('jobsearch.html')


#@views.route('/jobs',methods = ['GET'])
@app.get('/jobs')
def job_results():
    job_list = get_from_api()
    return render_template("jobresults.html", job_list=job_list)


if __name__ == '__main__':
    app.run(debug=True, port=5007)

