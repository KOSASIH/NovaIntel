import pandas as pd
import datetime

class TemporalDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = pd.DataFrame(columns=['timestamp', 'data'])

    def insert(self, data):
        self.db = self.db.append({'timestamp': datetime.datetime.now(), 'data': data}, ignore_index=True)

    def query(self, timestamp):
        return self.db[self.db['timestamp'] == timestamp]
