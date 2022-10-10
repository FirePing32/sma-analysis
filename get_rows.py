import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    database=os.environ['DB'], user=os.environ['DBUSER'], password=os.environ['PASSWORD'], host=os.environ['HOST'], port=os.environ['PORT']
)
cursor = conn.cursor()

def get_all_rows():
    cursor.execute("SELECT * FROM stock")
    return cursor.fetchall()