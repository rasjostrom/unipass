
import urwid
from unipass.controller import controller
from unipass.settings import settings
import pyperclip


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
                self.button('Add entry', self.service_add),                
                #self.button('Search entry', None),
                self.button('Generate password', self.generate_password),
                self.button('Export to file', self.export_to_file),
                self.button('Import from file', self.import_from_file),
                urwid.Text('\n'),
                self.button('Quit', self.exit_program) ]))

    def service_add(self, btn):
        service = urwid.Edit(caption='Service: ', edit_text="")
        name = urwid.Edit(caption='Username: ', edit_text="")
        password = urwid.Edit(caption='Password: ', edit_text="")
        note = urwid.Edit(caption='Note: ', edit_text="")
        status = urwid.Text('\n', align='center')

        def paste_password(btn):
            password.set_edit_text(pyperclip.paste())

        def save(btn):
            if controller.add_service(
                    service.get_edit_text(),
                    name.get_edit_text(),
                    password.get_edit_text(),
                    note.get_edit_text()
            ):
                status.set_text('\nCreated success!')
            else:
                status.set_text('\nSomethings wrong!')
        
        self.open_box(
            self.menu('Add entry', [
                status,
                service,
                name,
                password,
                note,
                urwid.Text('\n'),
                self.button('Paster from clipboard', paste_password),
                self.button('Save', save),
                urwid.Text('\n'),
                self.button('Back', self.back) ]))
        
    def service_list(self, btn):

        self.open_box(
            self.menu('Services', [
                self.button(user[0], self.service_detail, user[2])
                for user in controller.list_all_services()
            ]+[
                urwid.Text('\n\n'),
                self.button('Back', self.back)
            ]
        ))

    def service_detail(self, btn, data):
        
        entry = controller.get_service_by_uuid(data)
        
        def password_to_clipboard(btn):
            pyperclip.copy(entry.password)

        def delete_service_confirm(btn, data):

            def delete_service(btn, uuid):
                controller.delete_service(uuid)
                self.back(None)
                self.back(None)
                self.back(None)
                
            self.open_box(
                self.menu('Delete!', [
                    urwid.Text('Are you sure that you wanna delete:', align='center'),
                    urwid.Text(entry.service, align='center'),
                    urwid.Text('\n'),
                    self.button('No', self.back),
                    self.button('Yes', delete_service, entry.uuid) ]))

        self.open_box(
            self.menu(entry.service,
                [urwid.Text('Username: {}'.format(entry.name)),
                 urwid.Text('Password: {}'.format(entry.password)),
                 urwid.Text('Note: {}'.format(entry.note)),
                 urwid.Text('\n'),
                 self.button('Copy password', password_to_clipboard),
                 self.button('Edit', self.service_edit, entry),
                 self.button('Back', self.back),
                 urwid.Text('\n'),
                 self.button('Delete', delete_service_confirm, entry) ]))

    def service_edit(self, btn, data):

        service = urwid.Edit(caption='Service: ', edit_text=data.service)
        name = urwid.Edit(caption='Username: ', edit_text=data.name)
        password = urwid.Edit(caption='Password: ', edit_text=data.password)
        note = urwid.Edit(caption='Note: ', edit_text=data.note)
        status = urwid.Text('\n', align='center')

        def paste_password(btn):
            password.set_edit_text(pyperclip.paste())
        
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
            self.menu('Edit: {}'.format(data.service), [
                status,
                service,
                name,
                password,
                note,
                urwid.Text('\n'),
                self.button('Save', save),
                self.button('Paste password from clipbord', paste_password),
                urwid.Text('\n'),
                self.button('Back', self.back) ]))

    def export_to_file(self, btn):

        path = urwid.Edit(caption='Export path: ',
                          edit_text=settings.HOME_DIR+'/unipass_export.json')
        status = urwid.Text('\n', align='center')

        def save(btn):
            controller.export_data(path.get_edit_text())
            status.set_text('\nUpdated success!')

        self.open_box(
            self.menu('Export UniPass database', [
                status,
                path,
                urwid.Text('\n'),
                self.button('Export', save),
                urwid.Text('\n'),
                self.button('Back', self.back) ]))

    def import_from_file(self, btn):

        path = urwid.Edit(caption='File location: ',
                          edit_text=settings.HOME_DIR+'/unipass_export.json')
        status = urwid.Text('\n', align='center')

        def save(btn):
            controller.import_data(path.get_edit_text())
            status.set_text('\nImport success!')

        self.open_box(
            self.menu('Import from file', [
                status,
                path,
                urwid.Text('\n'),
                self.button('Start import', save),
                urwid.Text('\n'),
                self.button('Back', self.back) ]))

    def generate_password(self, btn):
        
        def password_to_clipboard(btn):
            pyperclip.copy(password.get_text()[0])

        def generate(btn):
            pwd = controller.generate_password(
                lower_case.get_state(),
                upper_case.get_state(),
                numbers.get_state(),
                special.get_state(),
                int(length.get_edit_text()))

            password.set_text(pwd)

        password = urwid.Text("Password: ", align='center')
        lower_case = urwid.CheckBox(label='Lower case', state=True)
        upper_case = urwid.CheckBox(label='Upper case', state=True)
        numbers = urwid.CheckBox(label='Numbers', state=True)
        special = urwid.CheckBox(label='Special', state=False)
        length = urwid.Edit('Length:', '16')
        
        self.open_box(
            self.menu('Genereate Password', [
                password,
                urwid.Text('\n'),
                lower_case,
                upper_case,
                numbers,
                special,
                length,
                urwid.Text('\n'),
                self.button('Generate pwd', generate),
                self.button('Copy', password_to_clipboard),
                urwid.Text('\n'),
                self.button('Back', self.back) ]))

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

    def back(self, btn):
        self.original_widget = self.original_widget[0]
        self.box_level -= 1

    def keypress(self, size, key):
        if key == 'esc' and self.box_level > 1:
            self.back(None)
        elif key == 'esc' and self.box_level == 1:
            self.exit_program(None)
        else:
            return super(UniPassUrwid, self).keypress(size, key)

    def exit_program(self, btn):
        raise urwid.ExitMainLoop()
        

def start():
    urwid.MainLoop(UniPassUrwid(), palette=[('reversed', 'standout', '')]).run()        

    

