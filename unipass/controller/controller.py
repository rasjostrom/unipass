
from unipass.model.models import Service


def login(username, password):
    for user in Service.getall():
        if (user.name == username and user.password == password) and user.admin:
            return True
    return False


def create_user(username, password):
    user = Service()
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
    for user in Service.getall():
        if user.service == service:
            return user
    return None


def list_all_services():
    return [(user.service, user.name, user.uuid) for user in Service.getall()]


def add_service(service, name, password, note):
    serv = Service()
    serv.service = service
    serv.name = name
    serv.password = password
    serv.note = note
    if serv.valid():
        serv.create()
        return True
    else:
        return False


def update_service(uuid, service, name, password, note):
    serv = Service.getbyuuid(uuid)
    serv.service = service
    serv.name = name
    serv.password = password
    serv.note = note
    if serv.valid():
        serv.update()
        return True
    else:
        return False


def get_service_by_uuid(uuid):
    return Service.getbyuuid(uuid)



