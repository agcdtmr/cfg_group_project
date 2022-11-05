from flask_login import UserMixin
# stores the user ide as a cookie


class User(UserMixin):

    def __init__(self, user_details):
        self.id = user_details.get('user_ID')
        self.first_name = user_details.get('first_name')
        self.surname = user_details.get('surname')
        self.email = user_details.get('email')
