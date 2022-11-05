<p align="center"><img width=40% src="https://github.com/agcdtmr/cfg_group_project/blob/main/Templates/static/cookie__4_-removebg-preview.png"></p>

# Cookie Jobs 

## Table of content
- [Description](#Description)
- [Our Why's](#Our-Why's)
- [Requirements](#Requirements)
- [Built With](#Built-With)
- [Getting Started](#Getting-Started)
- [Project Files Description](#Project-Files-Description)
- [Authors](#Authors)
- [License](#License)
- [Project Status](#Project-Status)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Description
Entering the tech job search can be daunting and overwhelming.
Based on data from [reed.co.uk](https://www.reed.co.uk/api),
**CookieJobs** is an open source tool built for [Code First Girls](https://codefirstgirls.com/)
graduates and alumni, career switchers and tech newbies.


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Our Why's
**We wanted a tool that would:**
1. Allow users to search junior-level tech jobs
2. Help the CFG graduates and alumni find jobs in tech

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Requirements
1. Application is developed in Python 3.9
2. You can install the packages using the `requirements.txt` file.
```
pip install -r requirements.txt
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Built With
This section lists all the major frameworks or libraries used to put this project together.
- [MySQL](https://www.mysql.com/products/connector/)
- [sys](https://docs.python.org/3/library/sys.html)
- [hashlib](https://docs.python.org/3/library/hashlib.html)
- [macros](https://explore-flask.readthedocs.io/en/latest/templates.html)
- [requests](https://pypi.org/project/requests/)
- [flask](https://flask.palletsprojects.com/en/2.2.x/)
- [bootstrap](https://getbootstrap.com/)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Getting Started
1. Go to our GitHub [repo](https://github.com/agcdtmr/cfg_group_project).
2. Fork or clone our project to your local directory.
3. Install the python libraries below if necessary:
- Flask
```
pip install Flask
```

- requests
```
pip install requests
```

- sys
```
pip install os-sys
```

- hashlib
```
pip install hashlib
```

4. Open the repo using pycharm, go to **app.py** and run.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Project Files Description
- api.py - Where we call our api.
- app.py - The main file that runs our website.
- auth.py - Stores the user id as a cookie
- config.py - Database connection information and secret Key for Flask session
- views.py - Creating the views for the webpage
- connection.py - Where we connect our sql database to our python server.
- users.py - Where we retrieve data from our users.
- saved_jobs.py - Functions to save and retrieve saved jobs from the database.

**Other supporting files**
- jobengine.html - Where user may choose to find all jobs or filtered jobs
- jobresults.html - Shows the list of all jobs
- jobsearch.html - Displays our form for filtering jobs
- search-results.html - Shows the list of filtered jobs
- login.html - Displays our form for logging in
- main.html - The main file for our html head and body and where we connect our css styling
- profile.html - Shows the profile page of the users once logged in
- signup.html - Displays our form for signing up

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Authors:
[Amelie Legault](https://www.linkedin.com/in/amelie-legault/), [Angeline Calleja](https://www.linkedin.com/in/anjcalleja/), Crina Pentiuc, Helen Shortland, and [Ruth Osoba](https://www.linkedin.com/in/ruth-osoba/)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## License
This project is open source and all ownership rights are attributed to the authors.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Acknowledgments
- Thank you very much to [Code First Girls](https://codefirstgirls.com/).
- Thank you to Nada, Fola, Jack and all the people behind this community.
- Congratulations to all our fellow students for this achievement, we wish you all the best in your journey to tech

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Project Status
This website is created as a final project for Autumn 2022 Software Engineering CFG Degree.
The development has stopped completely as we have submitted and presented this project.
