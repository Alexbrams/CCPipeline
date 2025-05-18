import pandas as pd

def convert_csv():
    df = pd.read_csv('profiles1.csv')
    df.to_json('data.json', orient='records', indent=4)
