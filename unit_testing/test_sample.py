from unittest import TestCase
import requests



class TestAPI(TestCase):
    def test_api(self):
        response = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=tech'
                                , auth=('d71bf436-fc9f-47fb-9a1f-2035ae09c27f'
                                        , ''))
        result = 200
        self.assertTrue(response, result)


