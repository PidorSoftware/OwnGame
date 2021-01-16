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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage
import inspect


background_color = (0.0, 0.02745098, 0.525490196, 1.0)

with open('questions.json') as file:
    data_json = json.loads(file.read())

def right_answer(rounds, theme, question):
    return(str(data_json['rounds']['round'][rounds]['themes']['theme'][theme]['questions']['question'][question]['right']['answer']))

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
        Window.fullscreen = True
        Window.clearcolor = background_color
        self.number_of_players = 5
        self.players = [0] * self.number_of_players
        self.names = [0] * self.number_of_players
        self.images = [0] * self.number_of_players
        self.scores = [[0] * 3 for i in range(self.number_of_players)]
        print(self.images)
        for i in range(self.number_of_players):
            self.names[i] = BoxLayout(size_hint=[1, 0.15])
            self.images[i] = BoxLayout(size_hint =[1, 0.7], padding=10)
            self.scores[i][0] = BoxLayout(size_hint=[1, 0.15])
            self.images[i].add_widget(Image(source='player2.jpg'))
            self.names[i].add_widget(Label(text='Игрок '+str(i + 1)))
            self.scores[i][2] = Label(text=str(self.scores[i][1]))
            self.scores[i][0].add_widget(self.scores[i][2])
        self.rounds = 0
        self.themes = number_of_themes(self.rounds)
        self.questions = number_of_quetions(self.rounds, self.themes - 1)
        self.main_box = BoxLayout(orientation='vertical', padding=50)

        for i in range(self.themes):
            themes_box = BoxLayout(orientation='horizontal')
            for j in range(self.questions + 1):
                if j != 0:
                    btn = Button(text = str(price_of_question(self.rounds, i, j - 1)),
                                background_color = (0.0, 0.0, 1.0, 1.0),
                                on_press = self.show_question,
                                background_disabled_down = '' )
                    btn.id = [i,j]
                    themes_box.add_widget(btn)
                else:
                    label = Label(text=theme(self.rounds, i), text_size=(110,None), halign='center')
                    themes_box.add_widget(label)
            self.main_box.add_widget(themes_box)

        self.panel = BoxLayout(orientation='horizontal',size_hint=[1, 1.5])

        for i in range(self.number_of_players):
            self.players[i] = BoxLayout(orientation='vertical')
            self.players[i].add_widget(self.images[i])
            self.players[i].add_widget(self.names[i])
            self.players[i].add_widget(self.scores[i][0])
            self.panel.add_widget(self.players[i])

        self.main_box.add_widget(self.panel)

        return self.main_box

    def dismiss_popup(self, instance):
        if(self.answer.text == right_answer(self.rounds, self.current_theme, self.current_question - 1)):
            self.scores[0][1] += int(price_of_question(self.rounds, self.current_theme, self.current_question - 1))
        else:
            self.scores[0][1] -= int(price_of_question(self.rounds, self.current_theme, self.current_question - 1))
        self.popup.dismiss()
        self.scores[0][2].text = str(self.scores[0][1])

    def show_question(self, instance):
        instance.disabled = True
        instance.opacity = 0
        label = Label(text=question(self.rounds, instance.id[0], instance.id[1]-1), text_size=(600,None), halign='center')
        self.current_theme = instance.id[0]
        self.current_question = instance.id[1]
        general_box = BoxLayout(orientation='vertical')
        box_with_question = BoxLayout(orientation='vertical', size_hint=[1, 0.7])
        box_with_question.add_widget(label)
        box_with_input = BoxLayout(orientation='vertical', size_hint=[1, 0.2])
        self.answer = TextInput()
        box_with_input.add_widget(self.answer)
        box_with_input.add_widget(Button(text='Ответить', on_press=self.dismiss_popup))
        general_box.add_widget(box_with_question)
        general_box.add_widget(box_with_input)


        self.popup = Popup(title='Вопрос '+str((instance.id[0] * self.questions) + instance.id[1] + 1),
                            content=general_box,
                            auto_dismiss=False)
        self.popup.open()    

if __name__ == '__main__':
    MyApp().run()
