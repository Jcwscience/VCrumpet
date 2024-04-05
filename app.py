from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from helpers import Language

langs = Language()

supported_languages = langs.get_supported_languages_names()

class MainApp(App):

    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Dropdown Menu 1
        self.dropdown1 = DropDown()
        for language in supported_languages:
            btn = Button(text = language, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown1.select(btn.text))
            self.dropdown1.add_widget(btn)
        mainbutton1 = Button(text='Language 1')
        mainbutton1.bind(on_release=self.dropdown1.open)
        self.dropdown1.bind(on_select=lambda instance, x: setattr(mainbutton1, 'text', x))
        self.root.add_widget(mainbutton1)

        # Dropdown Menu 2
        self.dropdown2 = DropDown()
        for language in supported_languages:
            btn = Button(text = language, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown2.select(btn.text))
            self.dropdown2.add_widget(btn)
        mainbutton2 = Button(text='Language 2')
        mainbutton2.bind(on_release=self.dropdown2.open)
        self.dropdown2.bind(on_select=lambda instance, x: setattr(mainbutton2, 'text', x))
        self.root.add_widget(mainbutton2)

        # Start and Stop Recording Buttons
        start_button = Button(text="Start Recording")
        start_button.bind(on_press=self.start_recording)
        self.root.add_widget(start_button)

        stop_button = Button(text="Stop Recording")
        stop_button.bind(on_press=self.stop_recording)
        self.root.add_widget(stop_button)

        # Text Display Boxes
        self.text_display1 = TextInput(text='Recording status will be shown here.', readonly=True)
        self.root.add_widget(self.text_display1)

        self.text_display2 = TextInput(text='Additional info here.', readonly=True)
        self.root.add_widget(self.text_display2)
        return self.root

    def start_recording(self, instance):
        # Placeholder for start recording functionality
        self.text_display1.text = 'Recording started...'
        self.text_display2.text = 'Recording in progress...'

    def stop_recording(self, instance):
        # Placeholder for stop recording functionality
        self.text_display1.text = 'Recording stopped.'
        self.text_display2.text = 'Ready for new recording.'

if __name__ == '__main__':
    MainApp().run()
