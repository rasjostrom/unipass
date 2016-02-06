

import click
from model.models import initdb
from controller import controller
from getpass import getpass


@click.command()
@click.option('--urwid', is_flag=True, help='Urwid terminal GUI {yes | no}, default=no')
@click.option('--add', is_flag=True, help='Add service interactivly')
@click.option('--get', help='Get service interactivly')
@click.option('--list', is_flag=True, help='List all services')
def start(urwid, add, get, list):

    if initdb() is not True:
        create_user()

    if urwid: pass  # Start urwid view

    if get is not None:
        username = raw_input('User:')
        password = getpass('Pass: ')
        if controller.login(username, password):
            result = controller.find_by_service(get)
            if result is not None:
                print('Service: {}'.format(result.service))
                print('User: {}'.format(result.name))
                print('Note: {}'.format(result.note))
                print('Password: {}'.format(result.password))                
            else:
                print('could not find service')
        else:
            print('wrong cridentials')

    if add:
        service = raw_input('Service: ')
        username = raw_input('Username: ')
        password = raw_input('Password: ')
        note = raw_input('Note: ')
        if controller.add_service(service, username, password, note):
            print('{} saved.'.format(service))
        else:
            print('Something when wrong, sorry')

    if list:
        for service in controller.list_all_services():
            print(service[0]+' | '+service[1])


def create_user():
    """
    Create a user
    """
    print('No database found!\nCreate a user!')
    user = raw_input('Username: ')
    password1 = getpass('Password: ')
    password2 = getpass('Password again: ')
    while password1 != password2:
        print('Passwords didnt match')
        password1 = getpass('Password: ')
        password2 = getpass('Password again: ')
    controller.create_user(user, password1)


if __name__ == '__main__':
    start()
