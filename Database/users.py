import hashlib
import bcrypt

from Database.connection import get_database_connection


def add_user(first_name: str, surname:str, email:str, password: str):
    """
    Adds a new user to the database
    Raises an error is the email already exists in the database
    """
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            # converting password to bytes
            password_bytes = password.encode()
            #adding to the database
            cursor.execute("""INSERT
                                INTO users
                                   (first_name, surname, email, password) 
                              VALUES (%s, %s, %s, %s)""", [first_name, surname, email, hashlib.sha256(password_bytes).hexdigest()])
            connection.commit()

#to be implemented once "username" column is added to the users table
def get_user_by_credentials(username, password):
    """Retrieves the user with the given credentials, if present.
    If there is no matching user, returns None"""
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            password_bytes = password.encode()
            cursor.execute("""SELECT l.username, l.password
                                FROM users AS l                     
                              WHERE u.username = %s""", [username])  ###a new column username is needed in table users
            user = cursor.fetchone()
            #checking password
            if user and bcrypt.checkpw(password_bytes, user.get('password')):
                return user

def email_available(email):
    """Checks whether an email is available or if it's already in the database"""
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.id, u.first_name, u.email
                                FROM users AS u
                              WHERE u.email = %s""", [email])
            user = cursor.fetchone()
            return True if user is None else False