"""covert miles to km program"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesToKMConverterAPP(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_number_change(self, text, change):
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * FACTOR_MILES_TO_KM)


MilesToKMConverterAPP().run()

