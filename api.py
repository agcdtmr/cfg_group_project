from requests.auth import HTTPBasicAuth
from flask import jsonify
import requests

def get_from_api():
    # url = "https://xxxx"
    # API_KEY = "HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f"
    # params = {
    #     'token': API_KEY
    # }
    response = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=programmer,tech,frontend%20developer,'
                            'backend%20developer,devops,software%20engineer,junior',
               auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f', '')).json()
    for job in response['results']:
        data = [{
            "city": entry['locationName'],
            "job_title": entry['jobTitle'],
            "jobId": entry['jobId'],
            "employer_name": entry['employerName'],
            "link": entry['jobUrl'],
            "description": entry['jobDescription'],
            "exp_date": entry['expirationDate']
    } for entry in response['results']]

    return data

def search_result(jobTitle, locationName, employerName, minimumSalary, expirationDate):

    response = requests.get(f'https://www.reed.co.uk/api/1.0/search?keywords=programmer,tech,frontend%20developer,'
                            f'backend%20developer,devops,software%20engineer,junior,{jobTitle}&locationName='
                            f'{locationName}&employerName={employerName}&minimumSalary={minimumSalary}&'
                            f'expirationDate={expirationDate}',
                            auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f', '')).json()

    data = [{
        "city": entry['locationName'],
        "job_title": entry['jobTitle'],
        "jobId": entry['jobId'],
        "employer_name": entry['employerName'],
        "link": entry['jobUrl'],
        "description": entry['jobDescription'],
        "exp_date": entry['expirationDate']
    } for entry in response['results']]

    return data

##############################################

#if __name__=="__main__":
    print(get_from_api())
