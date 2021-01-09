import kivy
import random
from time import sleep

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import Label as CoreLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.clock import Clock
import inspect



string = """Блять, да мне похуй на тебя, блять, слушай, какая у тебя там тачка, блять, плюсы, джавы там блять, 
си, всё, мне похуй, хоть там "Руби", хоть блять нахуй "Котлин", хоть "Шарпы", хоть "Делфи" блять, 
хоть стометровый баш, мне на это насрать, понимаешь?"""


class MyApp(App):	

	def my_callback(self, dt):
	    pass

	def build(self):
		parser = Button()
		print(inspect.getmembers(parser, predicate=inspect.ismethod))
		Window.clearcolor = (0, 0.02745098, 0.525490196, 1)
		self.gl = GridLayout(cols = 5, rows = 5, padding = 100, spacing = 10, )
		for i in range(5):
			for j in range(5):
				self.gl.add_widget( Button(text = str((j + 1) * 100),
										background_color = (0, 0, 1, 1),
										on_press = self.show_question,
										background_disabled_down = '' ), index = i)
		return self.gl

	def dismiss_popup(self, dt):
		self.popup.dismiss()

	def show_question(self, instance):
		if instance.text:
			self.popup = Popup(title='question', content=Label(text=string),
			              auto_dismiss=False)
			self.popup.open()
			instance.text = ''
			instance.background_color = (1, 1, 1, 0)
			Clock.schedule_once(self.dismiss_popup, 5)
			

if __name__ == '__main__':
	MyApp().run()