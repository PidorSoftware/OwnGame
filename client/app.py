import kivy
import json

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.label import Label
import inspect


background_color = (0.0, 0.02745098, 0.525490196, 1.0)

with open('questions.json') as file:
	data_json = json.loads(file.read())

	'''print(questions)
	for i in range(number_of_rounds - 1):			
		for j in range(themes[i]):
			for k in range(questions[i][j]):
				print(data_json['rounds']['round'][i]['themes']['theme'][j]['questions']['question'][k]['@price'])
				print()'''

def question(rounds, theme, question):
	return (str(data_json['rounds']['round'][rounds]['themes']['theme'][theme]['questions']['question'][question]['scenario']['atom']))

def price_of_question(rounds, theme, question):
	return (data_json['rounds']['round'][rounds]['themes']['theme'][theme]['questions']['question'][question]['@price'])

def number_of_rounds():
	return (len(data_json['rounds']['round']))

def number_of_themes(rounds):
	return (len(data_json['rounds']['round'][rounds]['themes']['theme']))

def theme(rounds,theme):
	return (data_json['rounds']['round'][rounds]['themes']['theme'][theme]['@name'])

def number_of_quetions(rounds, themes):
	return (len(data_json['rounds']['round'][rounds]['themes']['theme'][themes]['questions']['question']))

class MyApp(App):	

	def build(self):
		Window.clearcolor = background_color
		self.rounds = 0
		self.themes = number_of_themes(self.rounds)
		self.questions = number_of_quetions(self.rounds, self.themes - 1)
		self.gl = GridLayout(cols = self.questions + 1, rows = self.themes, padding = 100, spacing = 10)
		for i in range(self.themes):
			for j in range(self.questions + 1):
				if j != 0:
					btn = Button(text = str(price_of_question(self.rounds, i, j - 1)),
								background_color = (0.0, 0.0, 1.0, 1.0),
								on_press = self.show_question,
								background_disabled_down = '' )
					btn.id = [i,j]
					self.gl.add_widget(btn)
				else:
					label = Label(text=theme(self.rounds, i), text_size=(110,None), halign='center')
					self.gl.add_widget(label)
		return self.gl

	def dismiss_popup(self, dt):
		self.popup.dismiss()

	def show_question(self, instance):
		instance.disabled = True
		instance.opacity = 0
		label = Label(text=question(self.rounds, instance.id[0], instance.id[1]), text_size=(600,None), halign='center')
		label.texture_update()
		self.popup = Popup(title='Вопрос '+str((instance.id[0] * self.questions) + instance.id[1] + 1),
							content= label,
							auto_dismiss=False)
		self.popup.open()
		Clock.schedule_once(self.dismiss_popup, 5)			

if __name__ == '__main__':
	MyApp().run()
