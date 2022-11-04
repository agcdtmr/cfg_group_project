import mysql.connector
import sys
sys.path.append('..')
from config import HOST, USER, DATABASE, PASSWORD

def get_database_connection():
    return mysql.connector.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password"
    )