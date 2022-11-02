from flask import Blueprint, render_template, redirect, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from Database.users import add_user, email_available, get_user_by_credentials
from api import get_from_api, get_job_by_title
from auth import User


views = Blueprint(__name__, "views")


@views.get('/')
def view_home():
    return render_template('home.html')

@views.get('/login')
def view_login():
    return render_template('login.html', user=current_user)


@views.post('/login')
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


@views.get('/signup')
def view_signup():
    if not current_user.is_anonymous:
        return redirect('/profile')
    else:
        return render_template('signup.html', user=current_user)

@views.post('/signup')
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


@views.post('/logout')
@login_required
def submit_logout():
    logout_user()
    return redirect ('/login')

@views.get('/profile')
def view_profile():
    #must add again login_required
    return render_template("profile.html", user=current_user)

######################################

#jobengine - full list button
@views.get('/jobengine')
def job_engine():
    return render_template('jobengine.html')

@views.get('/filter-jobs')
def job_search():
    return render_template('jobsearch.html')


# #@views.route('/jobs',methods = ['GET'])
@views.get('/jobs')
def job_results():
    job_list = get_from_api()
    return render_template("jobresults.html", job_list=job_list)

@views.get('/jobs-title-search')
def job_search_by_title():
    return render_template("jobs-title-search.html")

@views.get('/jobs-title-results')
def job_result_by_title():
    search_input = request.args.get('job')  # 'job' is from input name attribute from jobs-title-search.html
    job_list = get_job_by_title(search_input) # a function from api.py
    return render_template("jobs-title-results.html", data=job_list)

