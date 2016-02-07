
from model.models import User


def login(username, password):
    for user in User.getall():
        if (user.name == username and user.password == password) and user.admin:
            return True
    return False


def create_user(username, password):
    user = User()
    user.name = username
    user.password = password
    user.service = 'UniPass'
    user.note = 'Entry for UniPass'
    user.admin = True
    if user.valid():
        user.create()
        return True
    else:
        return False

def find_by_service(service):
    for user in User.getall():
        if user.service == service:
            return user
    return None


def list_all_services():
    return [(user.service, user.name, user.uuid) for user in User.getall()]


def add_service(service, name, password, note):
    serv = User()
    serv.service = service
    serv.name = name
    serv.password = password
    serv.note = note
    if serv.valid():
        serv.create()
        return True
    else:
        return False


def update_service(uuid, **kwargs):
    serv = User.getbyuuid(uuid)
    serv.service = kwargs['service']
    serv.name = kwargs['name']
    serv.password = kwargs['password']
    serv.note = kwargs['note']
    if serv.valid():
        serv.update()
        return True
    else:
        return False


def get_service(uuid):
    return User.getbyuuid(uuid)



