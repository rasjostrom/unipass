
try:
    input = raw_input
except NameError:
    pass


import click
import pyperclip
from getpass import getpass

from unipass.model.models import initdb
from unipass.controller import controller
from unipass.view import unipass_urwid


@click.command()
@click.option('--urwid', is_flag=True, help='Urwid terminal GUI')
@click.option('--add', is_flag=True, help='Add service interactivly')
@click.option('--get', help='Get service interactivly')
@click.option('--export-data', help='Export data, {path}')
@click.option('--import-data', help='Import data, {path}')
@click.option('--list', is_flag=True, help='List all services')
def start(urwid, add, get, list, export_data, import_data):

    if import_data is not None:
        if controller.import_data(import_data):
            print('Import successful')
        else:
            print('Somethings wrong!')

    if export_data is not None:
        if controller.export_data(export_data):
            print('Export successful!')
        else:
            print('Somethings wrong!')

    if initdb() is not True:
        create_user()
        print('User created!')

    if urwid:
        print('Login!')
        username = str(input('User: '))
        password = getpass('Pass: ')
        if controller.login(username, password):
            unipass_urwid.start()

    if get is not None:
        username = str(input('User:'))
        password = getpass('Pass: ')
        if controller.login(username, password):
            result = controller.find_by_service(get)
            if result is not None:
                print('Service: {}'.format(result.service))
                print('User: {}'.format(result.name))
                print('Password: {}'.format(result.password))
                print('Note: {}'.format(result.note))
            else:
                print('could not find service')
        else:
            print('wrong cridentials')

    if add:
        service = str(input('Service: '))
        username = str(input('Username: '))
        password = str(input('Password: '))
        note = str(input('Note: '))
        if controller.add_service(service, username, password, note):
            print('{} saved.'.format(service))
        else:
            print('Something when wrong, sorry')

    if list:
        print('|'+'-'*55+'|')        
        print('| {:>25} | {:25} |'.format('Service', 'Username'))
        print('|'+'-'*55+'|')
        for service in controller.list_all_services():
            print('| {:>25} | {:25} |'.format(service[0], service[1]))
        print('|'+'-'*55+'|')        
    
def create_user():
    """
    Create a user
    """
    print('No database found!\nCreate a user!')
    user = str(input('Username: '))
    password1 = getpass('Password: ')
    password2 = getpass('Password again: ')
    while password1 != password2:
        print('Passwords didnt match')
        password1 = getpass('Password: ')
        password2 = getpass('Password again: ')
    controller.create_user(user, password1)


if __name__ == '__main__':
    start()
