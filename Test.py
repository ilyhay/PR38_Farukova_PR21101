# main.py
import random
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import pygame



class FireSafetyApp(App):
    questions = [
        {
            'question': "Что делать, если в квартире начал гореть телевизор?",
            'image': 'C:\\Users\\ilyha\\Downloads\\tv_fire.jpg',
            'answers': ['А. Попытаться потушить пожар самостоятельно', 'Б. Вызвать пожарную службу и эвакуироваться',
                        'В. Продолжать смотреть телевизор', 'Г. Открыть окно и дышать свежим воздухом'],
            'correct': 'Б'
        },
        {
            'question': "Как нужно действовать при задымлении в помещении?",
            'image': 'C:\\Users\\ilyha\\Downloads\\smoke_filling_room.jpg',
            'answers': ['А. Закрыть окна и двери, укрыть нос и рот влажным материалом',
                        'Б. Открыть окна и двери, чтобы проветрить помещение', 'В. Включить вентилятор и смирно ждать',
                        'Г. Выключить свет и не двигаться с места'],
            'correct': 'А'
        },
        {
            'question': "Что следует делать, если ваша одежда загорелась?",
            'image': 'C:\\Users\\ilyha\\Downloads\\clothes_fire.jpg',
            'answers': ['А. Быстро броситься в сторону и побежать', 'Б. Остаться на месте и кричать о помощи',
                        'В. Броситься на землю и попытаться потушить пламя', 'Г. Продолжить стоять на месте'],
            'correct': 'В'
        },
        {
            'question': "Какие предметы лучше всего гасить водой в случае возгорания?",
            'image': 'C:\\Users\\ilyha\\Downloads\\water_extinguishing.jpg',
            'answers': ['А. Масляные пятна', 'Б. Электрооборудование', 'В. Банка с краской', 'Г. Бумажные документы'],
            'correct': 'А'
        },
        {
            'question': "Почему важно обслуживать и проверять пожарные сигнализации вовремя?",
            'image': 'C:\\Users\\ilyha\\Downloads\\smoke_detector.jpg',
            'answers': ['А. Чтобы повеселить соседей', 'Б. Для экономии электроэнергии',
                        'В. Для раннего обнаружения пожара и своевременной эвакуации', 'Г. Чтобы слушать музыку'],
            'correct': 'В'
        },
        {
            'question': "Какой тип огнетушителя используется для гашения электрических пожаров?",
            'image': 'C:\\Users\\ilyha\\Downloads\\electrical_fire.jpeg',
            'answers': ['А. Пенный', 'Б. Порошковый', 'В. Углекислотный', 'Г. Водный'],
            'correct': 'Б'
        },
        {
            'question': "Какие меры безопасности нужно соблюдать при использовании свечей в домашних условиях?",
            'image': 'C:\\Users\\ilyha\\Downloads\\candle_safety.png',
            'answers': ['А. Оставлять свечи без присмотра', 'Б. Ставить свечи на воспламеняющиеся поверхности',
                        'В. Обеспечить надежную подставку и удалить горючие материалы',
                        'Г. Забывать дуть свечи перед выходом из дома'],
            'correct': 'В'
        },
        {
            'question': "Какие предметы лучше всего хранить вне дома для профилактики пожаров?",
            'image': 'C:\\Users\\ilyha\\Downloads\\fire_prevention.png',
            'answers': ['А. Зажигалки и спички', 'Б. Химические вещества', 'В. Топливо и газ', 'Г. Огнетушитель'],
            'correct': 'Г'
        },
        {
            'question': "Почему важно проводить пожарные тренировки и обучение для семьи?",
            'image': 'C:\\Users\\ilyha\\Downloads\\fire_drill.jpg',
            'answers': ['А. Для создания паники и страха', 'Б. Для развлечения детей',
                        'В. Для обучения действиям в случае пожара и укрепления навыков эвакуации',
                        'Г. Чтобы взрослые лучше понимали, как это страшно'],
            'correct': 'В'
        },
        {
            'question': "Какие меры предосторожности нужно принимать при использовании электрических удлинителей?",
            'image': 'C:\\Users\\ilyha\\Downloads\\power_strip.jpg',
            'answers': ['А. Перегружать удлинители проводами', 'Б. Подключать много устройств к одному выходу',
                        'В. Регулярно проверять состояние удлинителей и избегать перегрева',
                        'Г. Ходить босиком на участке с разводкой электричества'],
            'correct': 'В'
        }
    ]
    correct_answers = 0
    answer_widgets = []

    def build(self):
        self.layout = FloatLayout()
        with self.layout.canvas:
            Color(1, 0, 0, 1)
            Rectangle(pos=(0, 0), size=(Window.width, Window.height))

        self.question_label = Label(text="", pos_hint={'center_x': 0.5, 'top': 0.9}, size_hint=(0.9, 0.1),
                                    color=(0, 0, 0, 1))  # Черный текст
        self.question_image = Image(source="", pos_hint={'center_x': 0.5, 'top': 0.82},
                                    size_hint=(0.3, 0.3))  # Уменьшенный размер изображения
        self.answer_labels = []
        for i in range(4):
            label = Button(text="", pos_hint={'center_x': 0.5, 'top': 0.5 - i * 0.1}, size_hint=(0.8, 0.1))
            label.bind(on_press=self.check_answer)
            self.answer_labels.append(label)

        for label in self.answer_labels:
            self.layout.add_widget(label)

        self.layout.add_widget(self.question_label)
        self.layout.add_widget(self.question_image)

        self.next_question()

        return self.layout

    def next_question(self):
        self.current_question = random.choice(self.questions)
        self.question_label.text = self.current_question['question']
        self.question_image.source = self.current_question['image']
        self.correct_answer = self.current_question['correct']
        random.shuffle(self.current_question['answers'])
        for label, answer in zip(self.answer_labels, self.current_question['answers']):
            label.text = answer

    def check_answer(self, instance):
        selected_answer = instance.text.split('.')[0]
        if selected_answer == self.correct_answer:
            print("Correct!")
            pygame.mixer.init()
            pygame.mixer.music.load('C:\\Users\\ilyha\\Downloads\\good.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()  # Ждем окончания воспроизведения
            self.correct_answers += 1
        else:
            print("Incorrect!")
            pygame.mixer.init()
            pygame.mixer.music.load('C:\\Users\\ilyha\\Downloads\\bad.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()  # Ждем окончания воспроизведения

        if len(self.questions) > 1:
            self.questions.remove(self.current_question)
            self.next_question()
        else:
            self.show_results()

    def on_start(self):
        self.next_question()

    def show_results(self):
        result_images = {
            0: 'C:\\Users\\ilyha\\Downloads\\awful.jpg',
            1: 'C:\\Users\\ilyha\\Downloads\\awful.jpg',
            2: 'C:\\Users\\ilyha\\Downloads\\awful.jpg',
            3: 'C:\\Users\\ilyha\\Downloads\\bad.jpg',
            4: 'C:\\Users\\ilyha\\Downloads\\bad.jpg',
            5: 'C:\\Users\\ilyha\\Downloads\\bad.jpg',
            6: 'C:\\Users\\ilyha\\Downloads\\norm.jpg',
            7: 'C:\\Users\\ilyha\\Downloads\\norm.jpg',
            8: 'C:\\Users\\ilyha\\Downloads\\norm.jpg',
            9: 'C:\\Users\\ilyha\\Downloads\\good.jpg',
            10: 'C:\\Users\\ilyha\\Downloads\\good.jpg'
        }

        result_messages = {
            0: "Плохо! Вам стоит изучить правила безопасности при пожаре.",
            1: "Плохо! Вам стоит изучить правила безопасности при пожаре.",
            2: "Плохо! Вам стоит изучить правила безопасности при пожаре.",
            3: "Нехорошо! Вам следует повторить правила безопасности при пожаре.",
            4: "Нехорошо! Вам следует повторить правила безопасности при пожаре.",
            5: "Нехорошо! Вам следует повторить правила безопасности при пожаре.",
            6: "Хорошо! Но вам следует повторить правила безопасности при пожаре.",
            7: "Хорошо! Но вам следует повторить правила безопасности при пожаре.",
            8: "Хорошо! Но вам следует повторить правила безопасности при пожаре.",
            9: "Очень хорошо! Ваши знания правил безопасности при пожаре на высоте.",
            10: "Очень хорошо! Ваши знания правил безопасности при пожаре на высоте."
        }

        result_image = result_images[self.correct_answers]
        result_message = result_messages[self.correct_answers]

        for label in self.answer_labels:
            self.layout.remove_widget(label)

        # Отображение результата
        self.question_label.text = result_message
        self.question_image.source = result_image


if __name__ == '__main__':
    FireSafetyApp().run()