from cfg_group_project.config import HOST, USER, DATABASE, PASSWORD
import mysql.connector
import sys
sys.path.append('..')


def get_database_connection():
    return mysql.connector.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password"
    )