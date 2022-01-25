from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('design.kv')

# inherit from screen object, when you see this, that class will be able to use those object
class LoginScreen(Screen):
    def sign_up(self):
        # self is referring to the current class and the login screen object
        # self is what has been instantiated from this class
        # and manager is a prop of Screen
        self.manager.current = "sign_up_screen"


# inherit from ScreenManager object, when you see this, that class will be able to use those object
class RootWidget(ScreenManager):
    def add_user(self)
        pass
class SignUpScreen(Screen, uname, pword):
    pass


class MainApp(App):
    #  this class takes in the App, which is an import from kivy
    # then we can use the build object, which is a part of the import
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()