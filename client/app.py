import kivy
import random
import time

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
used_questions = []

def my_callback():
    pass


class MyApp(App):	

	def build(self):
		Window.clearcolor = (0, 0.02745098, 0.525490196, 1)
		self.gl = GridLayout(cols = 5, rows = 5, padding = 100, spacing = 10, )
		for i in range(5):
			for j in range(5):
				if([i,j] not in used_questions):
					self.gl.add_widget( Button(text = str((j + 1) * 100),
										background_color = (0, 0, 1, 1),
										on_press = self.show_question,
										background_disabled_down = '' ) )
		'''else:
					self.gl.add_widget( Button(background_color = (0, 0.02745098, 0.525490196, 1),
										background_normal = '') )'''
		return self.gl

	def show_question(self, instance):
		if instance.text:
			instance.text = ''
			instance.background_color = (1, 1, 1, 0)
			popup = Popup(title='Test popup', content=Label(text='Hello world'),
			              auto_dismiss=0.0000001)
			popup.open()

if __name__ == '__main__':
	MyApp().run()