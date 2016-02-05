

import click
from model.models import initdb
from controller import controller
from getpass import getpass

@click.command()
@click.option('--urwid', default='no', help='Urwid terminal GUI {yes | no}, default=no')
@click.option('--get-service', help='Get service')
@click.option('--add-service', help='Add service')
@click.option('--list', help='List all services')
def start(urwid, get_service, add_service, list):

    if initdb() is not True:
        user = raw_input('Username: ')
        password1 = getpass('Password: ')
        password2 = getpass('Password again: ')
        while password1 != password2:
            print('Passwords didnt match')
            password1 = getpass('Password: ')
            password2 = getpass('Password again: ')
        controller.create_admin(user, password1)

    if urwid in ['yes', 'YES']: pass

    print(urwid)
    print(get_service)
    print(add_service)
    print(list)


if __name__ == '__main__':
    start()