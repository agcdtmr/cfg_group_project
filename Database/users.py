import hashlib
from cfg_group_project.Database.connection import get_database_connection


def add_user(first_name: str, surname: str, username: str, email: str, password: str):
    """
    Adds a new user to the database
    Raises an error is the email already exists in the database
    """
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            # converting password to bytes
            password_bytes = password.encode()
            # hashing the password
            password = hashlib.sha256(password_bytes).hexdigest()
            # adding to the database
            cursor.execute("""INSERT
                                INTO users
                                   (first_name, surname, username, email, password) 
                              VALUES (%s, %s, %s, %s, %s)""", [first_name, surname, username, email, password])
            connection.commit()


def email_available(email):
    """Checks whether an email is available or if it's already in the database"""
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.user_ID, u.first_name, u.surname, u.email, u.password
                                FROM users AS u
                              WHERE u.email = %s""", [email])
            user = cursor.fetchone()
            return True if user is None else False


def get_user_by_credentials(email, password):
    """Retrieves the user with the given credentials, if present.
    If there is no matching user, returns None"""
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            password_bytes = password.encode()
            password = hashlib.sha256(password_bytes).hexdigest()
            cursor.execute("""SELECT *
                                FROM users as u
                                WHERE u.email = %s""", [email])
            user = cursor.fetchone()
            # checking password
            if user is not None and password == user.get('password'):
                return user


def get_user_by_id(user_id):
    """Retrieves the users with the given id"""
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.user_ID, u.first_name, u.surname, u.email
                                FROM users AS u
                              WHERE u.user_id = %s""", [user_id])
            user = cursor.fetchone()
            if user is not None:
                return user
