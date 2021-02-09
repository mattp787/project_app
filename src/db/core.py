import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("MYSQL_HOST")
PORT = os.environ.get("MYSQL_PORT")
USER = os.environ.get("MYSQL_USER")
DB = os.environ.get("MYSQL_DB")
PASSWORD = os.environ.get("MYSQL_PASSWORD")

connection = pymysql.connect(
    host=HOST,
    user=USER,
    port=PORT,
    password=PASSWORD,
    db=DB
)
