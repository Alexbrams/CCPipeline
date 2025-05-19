import unittest
from calculate import *
import pandas as pd

class CheckFiles(unittest.TestCase):

    csv_df = pd.read_csv('profiles1.csv')
    json_df = pd.read_json('data.json')
    
    def csv_columns(self):

        # Assert CSV column count to a variable.
        columncount = self.csv_df.shape[1]

        # Check if it is accepted.
        t = correctColumnCount(columncount)

        # If the check wasn't accepted, Fail the test. 
        if t == False:
            self.fail

    def csv_rows(self):

        # Assert CSV row count to a variable.
        rowcount = self.csv_df.shape[0]
        
        # Check if it is accepted.
        t = correctRowCount(rowcount)
        
        # If the check wasn't accepted, Fail the test. 
        if t == False:
            self.fail

    def json_properties(self):
        
        missing = [column for column in correctProperties.expected if column not in self.json_df.columns]

        t = correctProperties(missing)

        if t == False:
            self.fail
        
    def json_rows(self):

        # Assert JSON row count to a variable.
        rowcount = self.json_df.shape[0]

        # Check if it is accepted.
        t = correctRowCount(rowcount)

        # If the check wasn't accepted, Fail the test. 
        if t == False:
         self.fail
        
    def alwaysFail(self):
        
        # Assert 1 to number
        number = 1

        # Check if it is accepted.
        t = failTest(number)

        # If the check wasn't accepted, Fail the test. (Always)
        if t == False:
            self.fail

if __name__ == '__main__':
    unittest.main()        