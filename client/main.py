from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class MainLayout(Widget):
    pass


class OwnGameApp(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    OwnGameApp().run()