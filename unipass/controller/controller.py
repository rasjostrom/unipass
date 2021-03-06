
import random
import json
import string

from unipass.model.models import Service, initdb


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
    for serv in Service.getall():
        if serv.service == service:
            return serv
    return None


def list_all_services():
    return [(serv.service, serv.name, serv.uuid) for serv in Service.getall()]


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

def delete_service(uuid):
    serv = Service.getbyuuid(uuid)
    serv.delete()
    return True
    
def get_service_by_uuid(uuid):
    return Service.getbyuuid(uuid)


def export_data(path='unipass_export.json'):
    try:
        with open(path, 'w') as outfile:
            json.dump([s.__dict__ for s in Service.getall()], outfile, indent=4)
        return True
    except:
        return False


def import_data(path='unipass_export.json'):
    initdb()  # If db not exists, create one
    with open(path, 'r') as fp:
        try:
            for s in json.load(fp):
                service = Service(**s)
                if service.valid():
                    service.create()
            return True
        except ValueError:
            return False


def generate_password(lowercase, uppercase, numbers, special, length):
    pwd = ''
    chars = ''
    special_chars = '%#'
    if lowercase:
        chars += string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if special:
        chars += special_chars

    for i in range(length):
        pwd += chars[random.randint(0, len(chars)-1)]

    return pwd

