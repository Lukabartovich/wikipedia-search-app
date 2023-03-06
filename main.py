from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder


import os


from SpeechRecognitionCover import Cover


from DataBase_class import DataBase
from scrap import getting_data

from Getting_Images import getWikiImage, shutil_getting



Window.size = (500, 600)
Builder.load_file('layout.kv')


class Start(Screen):
    def start(self):
        self.manager.current = 'log_in'

class LogIn(Screen):

    def log_in(self):
        self.name = str(self.ids.name.text)
        self.password = str(self.ids.password.text)
        self.db = DataBase()

        if self.name == 'name' or self.password == 'password' or self.name \
                == '' or self.password == '':
            pass
        else:
            right = self.db.check_for_account(self.name, self.password)
            self.ids.name.text = ''
            self.ids.password.text = ''
            print(right)
            if right == True:
                self.manager.current = 'home'
                with open('files/name.txt', 'w+') as file:
                    file.truncate(0)
                    file.write(self.name)

    def create_account(self):
        self.name = str(self.ids.name.text)
        self.password = str(self.ids.password.text)
        self.db = DataBase()

        if self.name == 'name' or self.password == 'password' or self.name \
                == '' or self.password == '':
            pass
        else:
            self.db.new_account(self.name, self.password)

            self.ids.name.text = ''
            self.ids.password.text = ''


class Home(Screen):

    def glass(self):
        print('glass')
        self.text = self.ids.input.text

        if len(self.text) != 0:
            print(self.text)
            self.ids.input.text = ''

            self.result_text = list(getting_data(self.text, 70))[1]

            with open('files/name.txt', 'r+') as file:
                name = file.read()

            db = DataBase()
            db.update_number(self.text, str(name))

            self.manager.current = 'result'
            self.manager.current_screen.ids.result.text = self.result_text

    def mic(self):
        c = Cover('en')
        print('talk')
        output = c.recognize(time=5)

        self.ids.input.text = output

        self.result_text = getting_data(output, 70)[1]

        with open('files/name.txt', 'r+') as file:
            name = file.read()


        db = DataBase()
        db.update_number(output, str(name))

        self.manager.current = 'result'
        self.manager.current_screen.ids.result.text = self.result_text

    def dots(self):
        print('dots')

        self.manager.current = 'dots'


class Result(Screen):
    def back(self):
        self.manager.current = 'home'

    def images(self):
        if str(self.ids.result.text) != 'None':
            with open('files/name.txt', 'r+') as file:
                name = file.read()

            db = DataBase()

            self.result_input = db.get_number('1', name)
            print(self.result_input)

            path = str(getWikiImage(self.result_input))
            print(path)

            os.chdir('C:\\Users\\Calva\\PycharmProjects\\facts\\images')

            real_image_pat = shutil_getting(path)
            os.chdir('C:\\Users\\Calva\\PycharmProjects\\facts')

            if real_image_pat != None:
                real_image_path = 'images/' + real_image_pat

                try:
                    self.manager.current = 'images'
                    self.manager.current_screen.ids.img.source = str(real_image_path)
                except:
                    self.manager.current = 'images'
                    self.manager.current_screen.ids.img.source = 'files/no_image.png'
            else:
                self.manager.current = 'home'


class Dots(Screen):
    def back(self):
        self.manager.current = 'home'

    def history(self):
        db = DataBase()
        with open('files/name.txt', 'r+') as file:
            name = file.read()

        self.manager.current = 'history'
        if db.get_number(1, name) != 'None':
            self.manager.current_screen.ids.b1.text = db.get_number(1, name)
        else:
            self.manager.current_screen.ids.b1.text = ''
        if db.get_number(2, name) != 'None':
            self.manager.current_screen.ids.b2.text = db.get_number(2, name)
        else:
            self.manager.current_screen.ids.b2.text = ''
        if db.get_number(3, name) != 'None':
            self.manager.current_screen.ids.b3.text = db.get_number(3, name)
        else:
            self.manager.current_screen.ids.b3.text = ''
        if db.get_number(4, name) != 'None':
            self.manager.current_screen.ids.b4.text = db.get_number(4, name)
        else:
            self.manager.current_screen.ids.b4.text = ''
        if db.get_number(5, name) != 'None':
            self.manager.current_screen.ids.b5.text = db.get_number(5, name)
        else:
            self.manager.current_screen.ids.b5.text = ''


class History(Screen):

    def b1_press(self):
        self.text = self.ids.b1.text

        print(self.text)

        self.result_text = getting_data(self.text, 70)[1]

        with open('files/name.txt', 'r+') as file:
            name = file.read()

        db = DataBase()
        db.update_number(self.text, str(name))

        self.manager.current = 'result'
        self.manager.current_screen.ids.result.text = self.result_text

    def b2_press(self):
        self.text = self.ids.b2.text

        print(self.text)

        self.result_text = getting_data(self.text, 70)[1]

        with open('files/name.txt', 'r+') as file:
            name = file.read()

        db = DataBase()
        db.update_number(self.text, str(name))

        self.manager.current = 'result'
        self.manager.current_screen.ids.result.text = self.result_text

    def b3_press(self):
        self.text = self.ids.b3.text

        print(self.text)

        self.result_text = getting_data(self.text, 70)[1]

        with open('files/name.txt', 'r+') as file:
            name = file.read()

        db = DataBase()
        db.update_number(self.text, str(name))

        self.manager.current = 'result'
        self.manager.current_screen.ids.result.text = self.result_text

    def b4_press(self):
        self.text = self.ids.b4.text

        print(self.text)

        self.result_text = getting_data(self.text, 70)[1]

        with open('files/name.txt', 'r+') as file:
            name = file.read()

        db = DataBase()
        db.update_number(self.text, str(name))

        self.manager.current = 'result'
        self.manager.current_screen.ids.result.text = self.result_text

    def b5_press(self):
        self.text = self.ids.b5.text

        print(self.text)

        self.result_text = getting_data(self.text, 70)[1]

        with open('files/name.txt', 'r+') as file:
            name = file.read()

        db = DataBase()
        db.update_number(self.text, str(name))

        self.manager.current = 'result'
        self.manager.current_screen.ids.result.text = self.result_text

    def back(self):
        self.manager.current = 'home'

    def clear(self):
        db = DataBase()

        with open('files/name.txt', 'r+') as file:
            name = file.read()

        for i in range(5):
            db.update_number('None', str(name))

        self.manager.current = 'home'


class Images(Screen):
    def back(self):
        self.manager.current = 'home'

class Root(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return Root()


MainApp().run()