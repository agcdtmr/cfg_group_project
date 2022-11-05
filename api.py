from requests.auth import HTTPBasicAuth
import requests


def get_from_api():
    response = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=programmer,frontend%20developer,'
                            'backend%20developer,software%20engineer',
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

    response = requests.get(f'https://www.reed.co.uk/api/1.0/search?keywords=programmer,frontend%20developer,'
                            f'backend%20developer,software%20engineer,{jobTitle}&locationName='
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

