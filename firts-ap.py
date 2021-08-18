from kivy.app import App  #istid3a a  tatbik
from kivy.lang import Builder # intid3a a milaf kharigiy
from kivy.core.window import Window #tahakom fi size + color
from kivy.uix.screenmanager import ScreenManager, Screen

Window.clearcolor=(100/255.0,0,1,1) # "red, green, blue,a" hada kod litandif nafida mina al alwan 0=>255
Window.size=(400,630)  # "width, height" tahakom fi hagm nafida

class Error(Screen):
    pass
class Maintree(ScreenManager):
    pass
class Mainone(Screen):
    pass
class Maintow(Screen):
    pass

nano = Builder.load_file("my.kv")

class My_app(App):
    def build(self):
        self.title="mama" # ta4yira 3onwan app
        return nano
    



if __name__ =="__main__":
    My_app().run()


