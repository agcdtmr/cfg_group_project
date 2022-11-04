from unittest import TestCase
import requests
from cfg_group_project.api import get_from_api, search_result


class TestAPI(TestCase):
    def Test_get_from_api(self):
        response = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=tech'
                                , auth=('d71bf436-fc9f-47fb-9a1f-2035ae09c27f'
                                        , ''))
        result = 200
        self.assertTrue(response, result)


    def Test_search_result(self):
        response = requests.get(f'https://www.reed.co.uk/api/1.0/search?keywords=programmer,tech,frontend%20developer,'
                                f'backend%20developer,devops,software%20engineer,junior,{jobTitle}&locationName='
                                f'{locationName}&employerName={employerName}&minimumSalary={minimumSalary}&'
                                f'expirationDate={expirationDate}',
                                auth=HTTPBasicAuth('d71bf436-fc9f-47fb-9a1f-2035ae09c27f', ''))
        result = 200

        self.assertTrue(response, result)
