import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",   # change this
        database="hospital_coverage"
    )
    return conn