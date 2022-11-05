from requests.auth import HTTPBasicAuth
from auth import User
import requests
from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_user, logout_user, current_user, login_required
from Database.users import add_user, get_user_by_credentials, email_available
from Database.saved_jobs import save_job, display_saved_jobs, save_applied_for_job
from api import get_from_api, search_result
from datetime import timedelta

views = Blueprint(__name__, "views")

# search engine


@views.get('/jobengine')
def job_engine():
    return render_template('jobengine.html')


@views.get('/jobsearch')
def jobsearch():
    return render_template("jobsearch.html")


@views.get('/jobs')
def job_results():
    job_list = get_from_api()
    return render_template("jobresults.html", job_list=job_list)


@views.get('/search-results')
def job_search_result():
    search_title = request.args.get('jobTitle')
    search_location = request.args.get('locationName')
    search_employer = request.args.get('employerName')
    search_salary = request.args.get('minimumSalary')
    search_deadline = request.args.get('expirationDate')
    job_list = search_result(search_title, search_location, search_employer, search_salary, search_deadline)
    return render_template("search-results.html", data=job_list)

# main page


@views.get('/')
def view_home():
    return render_template('home.html')

# user pages


@views.get('/login')
def view_login():
    return render_template('login.html', user=current_user)


@views.post('/login')
def submit_login():
    if not current_user.is_anonymous:
        return redirect('/profile')
    email = request.form.get('email')
    password = request.form.get('password')
    user = get_user_by_credentials(email, password)
    if user is None:
        flash('Invalid credentials', 'error')
    else:
        user = User(user)
        login_user(user, remember=True, duration=timedelta(hours=2))
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
    # email already exists
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
    return redirect('/login')


@views.get('/profile')
def view_profile():
    data = (display_saved_jobs())
    return render_template("profile.html", user=current_user, data=data)


# store and retrieve favourite jobs

@views.post('/saved_job')
def save_job_id():
    jobID = request.form.get('JobID')
    response = requests.get(f'https://www.reed.co.uk/api/1.0/jobs/{jobID}',
                               auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f', '')).json()

    user_id = current_user.id

    save_job(response['employerId'],
             response['employerName'],
             response['expirationDate'],
             response['jobDescription'],
             response['jobId'],
             response['jobTitle'],
             response['jobUrl'],
             response['locationName'],
             response['maximumSalary'],
             response['minimumSalary'],
             user_id
             )
    return redirect('/profile')


@views.post('/have_i_applied_for_this_job')
def have_i_applied_for_this_job():
    jobID = request.form.get('jobID')
    link = request.form.get('link')

    save_applied_for_job(jobID)

    return redirect(link)
