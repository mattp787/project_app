import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("MYSQL_HOST")
PORT = os.environ.get("MYSQL_PORT")
USER = os.environ.get("MYSQL_USER")
DB = os.environ.get("MYSQL_DB")
PASSWORD = os.environ.get("MYSQL_PASSWORD")

# connection = pymysql.connect(
#     host=HOST,
#     user=USER,
#     port=PORT,
#     password=PASSWORD,
#     db=DB
# )

def connection():
    return pymysql.connect(host=HOST, user=USER, port=int(PORT), password=PASSWORD, db=DB, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

def query(conn, sql):
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

def update(conn, sql):
    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()
    # return conn.commit()