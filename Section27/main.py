from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

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
    pass
class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        print(users)

        # when the new object is created in json there will be user1, user2, then 
        # whatever is put into uname, will be the name of the third object. 
        # so if we put in u1 it would look like
        # user1: {}, user2: {}, u1: {}
        users[uname] = {'username': uname, 'password': pword, 'created': datetime.now()}

        with open("users.json", 'w') as file:
            json.dump(users, file)

class MainApp(App):
    #  this class takes in the App, which is an import from kivy
    # then we can use the build object, which is a part of the import
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()