from requests.auth import HTTPBasicAuth
from flask import jsonify
import requests
from pprint import pprint

def get_from_api():
    # url = "https://xxxx"
    # API_KEY = "HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f"
    # params = {
    #     'token': API_KEY
    # }
    response = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=tech',
               auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f', '')).json()
    for job in response['results']:

        city = job['locationName']
        job_title = job['jobTitle']
        jobId = job['jobId']
        employer_name = job['employerName']
        link = job['jobUrl']
        description = job['jobDescription']
        exp_date = job['expirationDate']
        data = {
            "city": city,
            "job_title": job_title,
             "jobId ": jobId,
             "employer_name": employer_name,
             "link": link,
             "description": description,
             "exp_date": exp_date
                 }
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
# filtered_search(filter, keyword)



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
# def get_job_by_title(jobTitle):
#     response = requests.get(f'https://www.reed.co.uk/api/1.0/search?keywords={jobTitle}',auth=auth)
#     jobs = response.json()
#     for job in response.json()['results']:
#         #for title in response.json()['results']:
#             print(job['jobTitle'])

###############################


##############################################

#if __name__=="__main__":
    print(get_from_api())
    #print(get_unfiltered_data())
    #print(filtered_search('junior','London'))
