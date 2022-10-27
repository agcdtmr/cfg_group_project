from requests.auth import HTTPBasicAuth
import requests
from pprint import pprint


def filtered_search(filter, keyword):
    res = requests.get(
        'https://www.reed.co.uk/api/1.0/search?keywords=programmer,tech,frontend,data,backend,devops,junior&{}={}'.format(
            filter, keyword),
        auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f', ''))
    for data in res.json()['results']:
        pprint(data)


filter= input('Filter by: ')
keyword= input('You are searching for jobs with a {} of:'.format(filter))

filtered_search(filter, keyword)

