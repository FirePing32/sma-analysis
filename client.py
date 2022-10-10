import csv
from insert import insert_rows
from get_rows import get_all_rows
from grapher import sma
# file = open('data.csv')
# reader = csv.reader(file)

# insert_rows(reader)

all_data = get_all_rows()

raw_data = [{'date': r[0], 'open': r[1], 'high': r[2], 'low': r[3], 'close': r[4], 'volume': r[5]} for r in all_data]

sma(raw_data, 20, 50)
sma(raw_data, 30, 50)
