from unittest import TestCase
import hashlib
from app import app


class TestAPI(TestCase):
    def test_api(self):
        response = requests.get('https://www.reed.co.uk/api/1.0/search?keywords=tech'
                                , auth=('d71bf436-fc9f-47fb-9a1f-2035ae09c27f'
                                        , ''))
        result = 200
        self.assertTrue(response, result)

class HashedPassword(TestCase):
    def test_hash_password(self):
        normal_password = "12345"
        password_bytes=normal_password.encode()
        hashed_password=hashlib.sha256(password_bytes).hexdigest()
        self.assertEqual(hashed_password, "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5")


class TestJobEngineRegistration(TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def tearDown(self):
        self.app = None
        self.client = None

    def test_registration_form(self):
        response = self.client.get('/signup')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        # make sure all the fields are included
        assert 'name="username"' in html
        assert 'name="email"' in html
        assert 'name="first_name"' in html
        assert 'name="surname"' in html

    def test_signup_new_user(self):
        response=self.client.post('/signup', data={
            "first_name": "anna",
            "surname": "smith",
            "username":"anny",
            "email":"anny@gmail.com",
            "password":"12345",
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_login_with_correct_credentials(self):
        response = self.client.post('/login', data={
            'email': 'anny@gmail.com',
            'password': '12345',
        }, follow_redirects=True)
        assert response.status_code == 200