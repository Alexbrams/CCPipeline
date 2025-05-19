import unittest
from calculate import *
import pandas as pd

class CheckFiles(unittest.TestCase):

    csv_df = pd.read_csv('profiles1.csv')
    json_df = pd.read_json('data.json')
    
    def test_csv_columns(self):

        # Assert CSV column count to a variable.
        columncount = self.csv_df.shape[1]

        # Check if it is accepted.
        t = correctColumnCount(columncount)

        # If the check wasn't accepted, Fail the test. 
        self.assertTrue(t, f"CSV column count {columncount} is incorrect")

    def test_csv_rows(self):

        # Assert CSV row count to a variable.
        rowcount = self.csv_df.shape[0]
        
        # Check if it is accepted.
        t = correctRowCount(rowcount)
        
        self.assertTrue(t, f"CSV row count {rowcount} is incorrect.")

    def test_json_properties(self):
        
        missing = [col for col in properties if col not in self.json_df.columns]

        t = correctProperties(missing)

        self.assertTrue(t, f"Properties: {missing} is missing.")
        
    def test_json_rows(self):

        # Assert JSON row count to a variable.
        rowcount = self.json_df.shape[0]

        # Check if it is accepted.
        t = correctRowCount(rowcount)

        self.assertTrue(t, f"JSON row count {rowcount} is incorrect.")
        
    def test_alwaysFail(self):
        
        # Assert 1 to number
        number = 1

        # Check if it is accepted.
        t = failTest(number)

        self.assertFalse(t, "Extreme fail")

if __name__ == '__main__':
    unittest.main()       