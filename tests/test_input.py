import unittest
import csv
import datetime

class TestValidInput(unittest.TestCase):
    def test_data(self):
        raw_data = open('data.csv')
        reader = csv.reader(raw_data)
        for line in reader:
            self.assertEqual(type(datetime.datetime.strptime(
                line[0], '%Y-%m-%d %H:%M:%S')), datetime.datetime)
            self.assertEqual(type(float(line[1])), float)
            self.assertEqual(type(float(line[2])), float)
            self.assertEqual(type(float(line[3])), float)
            self.assertEqual(type(float(line[4])), float)
            self.assertEqual(type(int(line[5])), int)
