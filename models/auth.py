
class User:
    def __init__(self, username, password, token):
        self.username = username
        self.password = password
        self.token = token

    def __repr__(self):
        return '<User {}>'.format(self.username)