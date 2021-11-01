from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar

class main(MDApp):
    def build(self):
        screen = MDScreen()

        return screen

if __name__ == '__main__':
    main().run()