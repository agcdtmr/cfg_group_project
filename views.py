#creating the views for the webpage

from flask import Blueprint, render_template,jsonify,request,flash, redirect, url_for
from Database.users import add_user, get_user_by_credentials,email_available
from config import SECRET_KEY
from api import get_from_api


views = Blueprint(__name__, "view")

# home page
@views.get('/')
def view_home():
    return render_template('home.html')

#jobengine - full list button
@views.get('/jobengine')
def job_engine():
    return render_template('jobengine.html')

@views.get('/filter-jobs')
def job_search():
    return render_template('jobsearch.html')


#@views.route('/jobs',methods = ['GET'])
@views.get('/jobs')
def job_results():
    job_list = get_from_api()
    return render_template("jobresults.html", job_list=job_list)

#Possible API call:
###################
# @views.get('/<jobTitle>')
# def job_full_list(jobTitle):
#    job_list=get_job_by_title('tech')
#    return render_template("jobresults.html", job_list=job_list)

#return ','.join([job['title'] for job in job_list]).title()
####################

#jobengine - filter button

@views.post('/jobs-title')
def job_search_by_title():
    pass

@views.get('/jobs-title')
def job_result_by_title():
    pass

@views.post('/jobs-location')
def job_search_by_location():
    pass

@views.get('/jobs-location')
def job_result_by_location():
    pass

#registering#login#logout
@views.get('/login')
def view_login():
    return render_template('login.html')

@views.post('/login')
def submit_login():
    password=request.form.get('password')
    username=request.form.get('username')
    user=get_user_by_credentials(username,password)
    if user is None:
        flash ("Invalid credentials", 'error')
        return redirect('/profile')

@views.get('/signup')
def view_signup():
    return render_template('signup.html')


@views.post('/signup')
def submit_signup():
    #these are taken from the html
    first_name = request.form.get('first_name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    password = request.form.get('password')
    #To be implemented:
    # if len(password)<8:
    #     flash ("Password should be at least 8 characters long", 'error')
    # elif not email_available(email):
    #     flash("an account with that email already exists", "error")
    if not email_available(email):
        flash("an account with that email already exists", "error")
    else:
        add_user(first_name, surname, email, password)
        flash("New account created", 'info')
        #return redirect ('/login')
    return redirect ('/profile')

@views.post('/logout')
def submit_logout():
    return redirect('/')

@views.get('/profile')
def view_profile():
    return render_template("profile.html")
