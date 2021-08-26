import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super (MyGridLayout,self).__init__(**kwargs)

        self.cols=2
        self.add_widget(Label(text="Your Name:  "))
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)


        self.add_widget(Label(text="Favorite Car:  "))
        self.car=TextInput(multiline=False)
        self.add_widget(self.car)

        self.add_widget(Label(text="Favorite Language:  "))
        self.lang=TextInput(multiline=False)
        self.add_widget(self.lang)

        #creating a button
        self.submit=Button(text="submit  ", font_size=30)
        #bind the button
        self.submit.bind(on_press=self.press)
        
        self.add_widget(self.submit)
    def press(self,instance):
        name=self.name.text
        car=self.car.text
        language=self.lang.text
        #print (f"hello--{name}-so your favorite car is {car}- your favorite language is {language}")

        self.add_widget(Label(text=f"hello--{name}-so your favorite car is {car}- your favorite language is {language}"))
       #clear screen 
        self.name.text=""
        self.car.text=""
        self.lang.text=""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__=='__main__':
    MyApp().run()