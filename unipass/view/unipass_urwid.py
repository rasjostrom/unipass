
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
             ]+[self.button('Back', self.back)]
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

    def exit_program(self, button):
        raise urwid.ExitMainLoop()
        

def start():
    urwid.MainLoop(UniPassUrwid(), palette=[('reversed', 'standout', '')]).run()        

    

