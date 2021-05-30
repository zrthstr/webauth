
from flask_login import UserMixin

from form import LoginForm

pseudodb = [
            ["somename","some_pass"],
            ["admin","secure"]]

class User(UserMixin):

    def __init__(self, id_, password):
        self.id = id_
        self.password = password

    """ theoretical todo: hash & salt """
    def verify_password(self, password):
        if self.password == password:
            return True
        return False

    @staticmethod
    def get(name):
        index = 0
        for n, p in pseudodb:
            if name == n:
                user = User(
                    n, p
                )
                return user
            index += 1
        return None

