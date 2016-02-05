
from model.models import User


def create_admin(username, password):
    user = User()
    user.name = username
    user.password = password
    user.admin = True
    if user.valid():
        user.create()
        return True
    else:
        return False

