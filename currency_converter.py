# Import necessary libraries and modules
import requests
import os
import json
from currency_dic import *
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from dotenv import load_dotenv

# Load environment variables from a file named ".env"
load_dotenv()

# Define the style for a RoundedButton using Kivy's KV language
Builder.load_string('''
<RoundedButton@Button>:
    background_color: 0, 0, 0, 0  # Make the background transparent
    canvas.before:
        Color:
            rgba: (0.4, 0.4, 0.4, 1) if self.state == 'normal' else (0, 0.7, 0.7, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [60]
''')

# Create a class for the RoundedButton
class RoundedButton(Button):
    pass

# Main application class inheriting from Kivy's App class
class CurrencyConverterApp(App):
    # Method to build the UI
    def build(self):
        # Define UI elements
        self.old_currency_input = TextInput(hint_text="Enter original currency symbol (Ex. USD, CAD, EUR, BTC)", multiline=False)
        self.amount_input = TextInput(hint_text="Enter amount to convert", multiline=False)
        self.new_currency_input = TextInput(hint_text="Enter target currency symbol (Ex. USD, CAD, EUR, BTC)", multiline=False)
        self.result_label = Label(text="")
        self.convert_button = RoundedButton(text="Convert", on_press=self.convert_currency)  # Instantiate directly
        self.exit_button = RoundedButton(text="Exit", on_press=self.stop)  # Instantiate directly

        # Create a layout for UI elements
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        layout.add_widget(self.old_currency_input)
        layout.add_widget(self.amount_input)
        layout.add_widget(self.new_currency_input)
        layout.add_widget(self.convert_button)
        layout.add_widget(self.result_label)
        layout.add_widget(self.exit_button)

        return layout

    # Helper method to check if a value can be converted to a target type
    def can_be_converted(self, value, target_type):
        try:
            target_type(value)
            return True
        except ValueError:
            return False

    # Helper method to verify user input
    def verify_input(self, from_currency, to_currency, amount_to_convert):
        check = False
        all_currencies = get_currencies()

        # Check if the amount can be converted to float and currencies are valid
        if self.can_be_converted(amount_to_convert, float) and from_currency in all_currencies and to_currency in all_currencies:
            check = True

        return check

    # Method to convert currency
    def convert_currency(self, instance):
        # Get current time
        current_time = datetime.now()
        current_time = current_time.strftime("%I:%M %p")

        # Get user inputs
        from_currency = self.old_currency_input.text.upper()
        amount_to_convert = self.amount_input.text
        to_currency = self.new_currency_input.text.upper()

        # Validate user input
        if not self.verify_input(from_currency, to_currency, amount_to_convert):
            self.result_label.text = f"Invalid Entry!\nPlease read instructions again and enter data\nCurrent Time: {current_time}\n\n"
            return None

        # Convert amount to float
        amount_to_convert = float(amount_to_convert)

        # Get exchange rate
        rate = self.currency_phaser(to_currency.upper(), from_currency.upper())

        # Check if the conversion was successful
        if rate is not None:
            # Perform currency conversion
            converted_amount = self.currency_converter(rate, amount_to_convert)
            all_currency = get_currencies()

            currency_1 = all_currency[f'{to_currency}']
            currency_2 = all_currency[f'{from_currency}']

            # Display the result
            result_text = f"\n\n{currency_2} to {currency_1}\nExchange rate:  ~{to_currency} {rate:.2f} per {from_currency.upper()}\n\n{from_currency.upper()} {amount_to_convert:.2f}  ≈  {to_currency.upper()} {converted_amount:.2f}\nCurrent Time:  {current_time}\n\n"
            self.result_label.text = result_text
        else:
            # Display an error message if the conversion fails
            self.result_label.text = f"Conversion failed!\nRetry\nCurrent Time: {current_time}\n\n"

        # Clear input fields after conversion
        self.old_currency_input.text = ""
        self.amount_input.text = ""
        self.new_currency_input.text = ""

    # Method to retrieve exchange rate from an API
    def currency_phaser(self, new_currency, old_currency):
        key = os.getenv("API_KEY")
        url = f"https://openexchangerates.org/api/latest.json?app_id={key}&base={old_currency}&prettyprint=true&show_alternative=true"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)

        # Check if the API request was successful
        if response.status_code == 200:
            data = json.loads(response.text)
            exchange_rate = data["rates"][new_currency]
            print(f"\n\nExchange rate = {exchange_rate}\n\n")
            return exchange_rate
        else:
            # Display an error message if the API request fails
            print(f"Error: {response.status_code}")
            return None

    # Method to perform currency conversion
    def currency_converter(self, rate, amount):
        new_value = rate * amount
        return new_value

# Entry point for the application
if __name__ == "__main__":
    # Run the CurrencyConverterApp
    CurrencyConverterApp().run()
