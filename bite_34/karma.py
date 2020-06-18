from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    def __init__(self, name: str):
    	self.name = name
    	self._transactions = []

    @property
    def karma(self):
    	return sum(self.points)
    
    @property
    def fans(self) -> int:
    	return len(set([t.giver for t in self._transactions]))

    @property
    def points(self):
    	return [t.points for t in self._transactions]

    def __add__(self, other):
    	self._transactions.append(other)
    	self.points.append(other.points)

    def __repr__(self):
    	if self.fans > 1:
    	    return f'{self.name} has a karma of {self.karma} and {self.fans} fans'
    	else:
    		return f'{self.name} has a karma of {self.karma} and {self.fans} fan'

