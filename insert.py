import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    database=os.environ['DB'], user=os.environ['DBUSER'], password=os.environ['PASSWORD'], host=os.environ['HOST'], port=os.environ['PORT']
)
cursor = conn.cursor()

def insert_rows(reader) -> None:
    for row in reader:
        print(row)
        cursor.execute(f"""INSERT INTO stock(datestamp, open, high, low, close, volume)
   VALUES ('{row[0]}', {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]})""")

    conn.commit()
    conn.close()
    