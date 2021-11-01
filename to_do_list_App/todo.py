from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar
from kivy.core.window import Window
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.textfield import MDTextField
from kivy.uix.scrollview import ScrollView


Window.size =(320, 600)
tareas_registradas = []
#mensajelist = []
class main(MDApp):
    #aqui nesecito ayuda 
    def on_start(self):
        self.elementoList.clear_widgets()
        p=0
        for i in tareas_registradas:
            z = i
            mensajelist = OneLineAvatarIconListItem(text=f"{i}-{p}")
            eliminar = IconLeftWidget(
                icon='trash-can',
                on_press=lambda a:self.eliminarTarea('que pongo aqui?')
                #on_press = self.elementoList.remove_widget(mensajelist[p])
            )

            terminar = IconRightWidget(icon='check-bold')
            mensajelist.add_widget(eliminar)
            mensajelist.add_widget(terminar)
            self.elementoList.add_widget(
                mensajelist
            )
            p+=1
    def eliminarTarea(self, *args):
        print(str(args))
     #hasta aqui es mi problema
    def agregarTarea(self, *args):
        tareas_registradas.append(str(self.tarea.text))
        print(tareas_registradas)
        self.on_start()

    def onPress1(self, *args):
        self.changeScreen(2)
    def onPress2(self, *args):
        self.changeScreen(3)
    def changeScreen(self, payload):
        self.menu.set_state('close')
        if payload == 2:
            self.gestorVentanas.current = 'ven1'
            print('esto funciona')
        else:
            print('tambien funciona')
            self.gestorVentanas.current = 'ven2'

    def openMenu(self):
        self.menu.set_state('toggle')
    def build(self):
        screen = MDScreen()
        self.toolbar = MDToolbar(title = 'To do List ')
        self.toolbar.pos_hint = {'top':1}

        #editamos los colores
        self.theme_cls.primary_palette = 'Gray'
        #agregamos el toolbar ala ventana
        self.toolbar.left_action_items = [['menu', lambda x: self.openMenu()]]
        screen.add_widget(self.toolbar)
        #menu
        self.menu = MDNavigationDrawer()
        #screen.add_widget(self.menu)
        #menu Opciones
        self.configButton = MDFlatButton(
            text = 'Configuracion',
            font_size = 16,
            pos_hint = {'center_x':0.5},
            on_press = self.onPress1
        )

        self.exitButton = MDFlatButton(
            text='Salir',
            font_size=16,
            pos_hint={'center_x': 0.5},
            on_press= self.onPress2
        )
        self.menuContent = MDBoxLayout()
        self.menuContent.orientation = 'vertical'
        self.menuContent.adaptive_height = True
        self.menuContent.pos_hint = {'top':1}
        self.menuContent.add_widget(self.exitButton,0)
        self.menuContent.add_widget(self.configButton, 1)
        #agregamos finalmente el conjunto de botones al menu
        self.menu.add_widget(self.menuContent)

        #gestion de ventanas
        self.ventana1 = MDScreen()

        self.ventana2 = MDScreen()
        #etiquetas
        self.texto1 = MDLabel(
            text = 'hola',
            halign="center"
                              )
        self.texto2 = MDLabel(
            text='chao',
            halign= "center"
        )
        self.tareas = MDBoxLayout()
        self.tareas.padding = [20,0,0,10]
        self.tareas.md_bg_color = [0,1,1,0]
        self.tarea = MDTextField(
            hint_text="Escribe una tarea",
            halign="left",
            size_hint = (0.8,1),
            font_size = 22,
        )


        self.agregar = MDIconButton(
            icon='plus',
            on_press = self.agregarTarea
        )


        self.tareas.add_widget(self.tarea)
        self.tareas.add_widget(self.agregar)
        self.ventana1.name = 'ven1'


        #lista de tareas
        self.listaTasks = ScrollView()
        self.elementoList = MDList()

        self.listaTasks.pos_hint = {'top':0.89}
        self.listaTasks.size_hint_max_y = 400
        self.listaTasks.add_widget(self.elementoList)
        self.container = MDBoxLayout()
        self.container.orientation = 'vertical'
        self.container.line_color = [0, 1, 1, 1]
        self.ventana1.add_widget(self.listaTasks, 1)
        self.ventana1.add_widget(self.tareas, 0)

        #self.ventana1.add_widget(self.container)
        self.ventana2.add_widget(self.texto2)
        self.ventana2.name = 'ven2'
        self.contentMain = MDNavigationLayout()

        self.gestorVentanas = ScreenManager()
        self.gestorVentanas.add_widget(self.ventana1)
        self.gestorVentanas.add_widget(self.ventana2)
        self.contentMain.add_widget(self.gestorVentanas)
        self.contentMain.add_widget(self.menu)
        screen.add_widget(self.contentMain)


        return screen

if __name__ == '__main__':
    main().run()
