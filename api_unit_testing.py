from unittest import TestCase
import requests
from requests.auth import HTTPBasicAuth


class TestAPI(TestCase):
    def test_get_from_api(self):
        response = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=tech'
                                , auth=('d71bf436-fc9f-47fb-9a1f-2035ae09c27f'
                                        , ''))
        result = 200
        self.assertTrue(response, result)

    def test_search_result(self):
        response = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=programmer,tech,frontend%20developer,'
                                'backend%20developer,devops,software%20engineer,junior,Junior%20Data%20Engineer&locationName='
                                'London&employerName=Anson%20McCade%20Ltd%20%20IT%20and%20Finance%20Recruitment&minimumSalary=45000&'
                                'expirationDate=09/12/2022',
                                auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f', ''))
        result = 200

        self.assertTrue(response, result)
