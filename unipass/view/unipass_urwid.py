
import urwid
from controller import controller


class UniPassUrwid(urwid.WidgetPlaceholder):
    max_box_levels = 7

    def __init__(self):
        super(UniPassUrwid, self).__init__(urwid.SolidFill(u' '))        
        self.box_level = 0
        self.menu_list()
        
    def menu_list(self):    
        self.open_box(
            self.menu(u'UniPass', [
                self.button('List entries', self.service_list),
                self.button('Search entry', None),
                self.button('Generate password', self.generate_password),
                urwid.Text('\n'),
                self.button('Quit', self.exit_program),
            ])
        )

    def service_list(self, services):
        self.open_box(
            self.menu('Services',
                      [
                          self.button(user[0], self.service_detail, user[2]) for user in controller.list_all_services()
                      ]+
                      [
                          urwid.Text('\n\n')
                      ]+
                      [
                          self.button('Back', self.back)
                      ]
        ))

    def service_detail(self, service, data):
        entry = controller.get_service(data)
        self.open_box(
            self.menu(entry.service,
                [urwid.Text('Username: '), urwid.Text(entry.name), urwid.Text('\n'),
                 urwid.Text('Password: '), urwid.Text(entry.password), urwid.Text('\n'),
                 urwid.Text('Note: '), urwid.Text(entry.note), urwid.Text('\n\n'),
             ]+[self.button('Edit', self.service_edit, entry), urwid.Text('\n'), self.button('Back', self.back)]
            )
        )

    def service_edit(self, service, data):

        service = urwid.Edit(caption='Service: ', edit_text=data.service)
        name = urwid.Edit(caption='Username: ', edit_text=data.name)
        password = urwid.Edit(caption='Password: ', edit_text=data.password)
        note = urwid.Edit(caption='Note: ', edit_text=data.note)
        status = urwid.Text('\n', align='center')
        
        def save(btn):
            if controller.update_service(
                    data.uuid,
                    service.get_edit_text(),
                    name.get_edit_text(),
                    password.get_edit_text(),
                    note.get_edit_text()
            ):
                status.set_text('\nUpdated success!')
            else:
                status.set_text('\Somethings wrong!')
        
        self.open_box(
            self.menu('Edit: {}'.format(data.service), [status, service, name, password, note]+[urwid.Text('\n'), self.button('Save', save), urwid.Text('\n'), self.button('Back', self.back)])
        )

    def generate_password(self, something):
        self.open_box(
            self.menu(
                'Genereate Password',
                [self.button('Back', self.back)]
            )
        )

    def button(self, caption, callback, data=None):
        button = urwid.Button(caption)
        urwid.connect_signal(button, 'click', callback, data)
        return urwid.AttrMap(button, None, focus_map='reversed')

    def open_box(self, box):
        self.original_widget = urwid.Overlay(urwid.LineBox(box),
            self.original_widget,
            align='center', width=('relative', 80),
            valign='middle', height=('relative', 80),
            min_width=24, min_height=8,
            #left=self.box_level * 3,
        )
        #     right=(self.max_box_levels - self.box_level - 1) * 3,
        #     top=self.box_level * 2,
        #     bottom=(self.max_box_levels - self.box_level - 1) * 2)
        self.box_level += 1
        
    def menu(self, title, choices):
        body = [urwid.Text(title, align='center'), urwid.Divider()]
        body.extend(choices)
        return urwid.ListBox(urwid.SimpleFocusListWalker(body))

    def back(self, something):
        self.original_widget = self.original_widget[0]
        self.box_level -= 1

    def keypress(self, size, key):
        if key == 'esc' and self.box_level > 1:
            self.back(None)
        elif key == 'esc' and self.box_level == 1:
            self.exit_program(None)
        else:
            return super(UniPassUrwid, self).keypress(size, key)
    

    def exit_program(self, button):
        raise urwid.ExitMainLoop()
        

def start():
    urwid.MainLoop(UniPassUrwid(), palette=[('reversed', 'standout', '')]).run()        

    

