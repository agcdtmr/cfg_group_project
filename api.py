from requests.auth import HTTPBasicAuth
from flask import jsonify
import requests
from pprint import pprint

#A. Mih

def get_from_api():
    # url = "https://xxxx"
    # API_KEY = "HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f"
    # params = {
    #     'token': API_KEY
    # }
    response = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=tech',
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


#API calls to follow:
########################
#1
# def filtered_search(filter, keyword):
#     res = requests.get(
#         'https://www.reed.co.uk/api/1.0/search?keywords=programmer,tech,frontend,data,backend,devops,junior&{}={}'.format(
#             filter, keyword),
#         auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f', ''))
#     for data in res.json()['results']:
#         pprint(data)
#
# filter= input('Filter by: ')
# keyword= input('You are searching for jobs with a {} of:'.format(filter))
#
# filtered_search(filter, keyword='tech')

########################
#2
# def get_unfiltered_data():
#     res = requests.get(
#         'https://www.reed.co.uk/api/1.0/search?keywords=programmer',
#         auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f', ''))
#     job_list=res.json()
#     for job in job_list['results']:
#       print(job['jobTitle'] + job['employerName'])
#         #print(job)


#############################
#3
# auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f','')
# res = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=programmer',auth=auth)
#
def get_job_by_title(jobTitle):

    response = requests.get(f'https://www.reed.co.uk/api/1.0/search?keywords={jobTitle}',
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

###############################


##############################################

if __name__=="__main__":
    print(get_from_api())
    #print(get_unfiltered_data())
    #print(filtered_search('junior','London'))
