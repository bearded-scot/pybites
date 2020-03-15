from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class UserDoesNotExist(Exception):
    pass

class UserAccessExpired(Exception):
    pass

class UserNoPermission(Exception):
    pass


def get_secret_token(username):
    user = [i for i in USERS if i.name == username]
    if len(user) == 0:
        raise UserDoesNotExist('user does not exist')
    user = user[0]
    if user.expired:
        raise UserAccessExpired('user\'s access token has expired')
    if user.role != ADMIN:
        raise UserNoPermission('user does not have permission')
    return SECRET

get_secret_token("PyBites")


