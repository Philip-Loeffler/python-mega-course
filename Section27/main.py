from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('design.kv')

# inherit from screen object
class LoginScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    #  this class takes in the App, which is an import from kivy
    # then we can use the build object, which is a part of the import
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()