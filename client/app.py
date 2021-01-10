import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.label import Label


background_color = (0.0, 0.02745098, 0.525490196, 1.0)

string = """Блять, да мне похуй на тебя, блять, слушай, какая у тебя там тачка, блять, плюсы, джавы там блять, 
си, всё, мне похуй, хоть там "Руби", хоть блять нахуй "Котлин", хоть "Шарпы", хоть "Делфи" блять, 
хоть стометровый баш, мне на это насрать, понимаешь?"""

class MyApp(App):	

	def build(self):
		Window.clearcolor = background_color
		self.gl = GridLayout(cols = 5, rows = 5, padding = 100, spacing = 10)
		for i in range(25):
			self.gl.add_widget( Button(text = str(((i % 5) + 1) * 100),
									background_color = (0.0, 0.0, 1.0, 1.0),
									on_press = self.show_question,
									background_disabled_down = '' ) )
		return self.gl

	def dismiss_popup(self, dt):
		self.popup.dismiss()

	def show_question(self, instance):
		instance.disabled = True
		instance.opacity = 0
		self.popup = Popup(title='question', content=Label(text=string), auto_dismiss=False)
		self.popup.open()
		Clock.schedule_once(self.dismiss_popup, 1)			

if __name__ == '__main__':
	MyApp().run()
