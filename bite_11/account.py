from functools import total_ordering

@total_ordering
class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below

    def __len__(self):
        return len(self._transactions)

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __getitem__(self, index):
        return self._transactions[index]

    def __iter__(self):
        return iter(self._transactions)

    def __add__(self, other):
        if type(other) in (int, float):
            self._transactions.append(other)
        else:
            raise ValueError()


    def __sub__(self, other):
        if type(other) in (int, float):
            self._transactions.append(other*-1)
        else:
            raise ValueError()

    def __repr__(self):
        return f'{self.name} account - balance: {self.balance}'




