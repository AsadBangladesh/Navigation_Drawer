from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (360, 640)

from kivymd.app import MDApp

KV = '''
<ContentNavigationDrawer>:
    ScrollView:
        MDList:
            OneLineListItem:
                text: "Screen Title One"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen Title Two"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
                    
            OneLineListItem:
                text: "Screen Title Three"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"

            OneLineListItem:
                text: "Screen Title Four"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4"

            OneLineListItem:
                text: "Screen Title Five"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 5"

            OneLineListItem:
                text: "Screen Title Six"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 6"



Screen:

    MDTopAppBar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            Screen:
                name: "scr 1"
                MDLabel:
                    text: "Screen Page One"
                    halign: "center"

            Screen:
                name: "scr 2"
                MDLabel:
                    text: "Screen Page Two"
                    halign: "center"  
            Screen:
                name: "scr 3"
                MDLabel:
                    text: "Screen Page Three"
                    halign: "center"
            Screen:
                name: "scr 4"
                MDLabel:
                    text: "Screen Page Four"
                    halign: "center"
            Screen:
                name: "scr 5"
                MDLabel:
                    text: "Screen Page Five"
                    halign: "center"
            Screen:
                name: "scr 6"
                MDLabel:
                    text: "Screen Page Six"
                    halign: "center"


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)


TestNavigationDrawer().run()