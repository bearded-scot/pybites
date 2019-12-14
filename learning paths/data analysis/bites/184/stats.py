from csv import DictReader
from os import path
from urllib.request import urlretrieve
from collections import Counter

DATA = path.join('/tmp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)



class BiteStats:

    def _load_data(self, data) -> list:
        return list(DictReader(open(data)))

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        unique_bites = set([row['bite'] for row in self.rows])
        return len(unique_bites)
            
    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        solved = set([row['bite'] for row in self.rows if row['completed']=='True'])
        return len(solved)

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        unique_user = set([row['user'] for row in self.rows])
        return len(unique_user)
    
    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        unique_user_solved = set([row['user'] for row in self.rows if row['completed'] == 'True'])
        return len(unique_user_solved)

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        clicks_per_bite = Counter([row['bite'] for row in self.rows])
        return max(clicks_per_bite, key = clicks_per_bite.get)

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        count_user_solved = Counter([row['user'] for row in self.rows if row['completed'] == 'True'])
        return max(count_user_solved, key = count_user_solved.get)
