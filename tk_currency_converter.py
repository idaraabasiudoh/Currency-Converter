import requests
import os
import json
from tkinter import Tk, Label,ttk
from currency_dic import *
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def can_be_converted(value, target_type):
    try:
        target_type(value)
        return True
    except ValueError:
        return False

def verify_input(from_currency, to_currency, amount_to_convert):
    check = False
    all_currencies = get_currencies()

    if can_be_converted(amount_to_convert, float) and from_currency in all_currencies and to_currency in all_currencies:
        check = True

    return check

def currency_phaser(new_currency, old_currency):
    key = os.getenv("API_KEY")
    url = f"https://openexchangerates.org/api/latest.json?app_id={key}&base={old_currency}&prettyprint=true&show_alternative=true"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        exchange_rate = data["rates"][new_currency]
        print(f"\n\nExchange rate = {exchange_rate}\n\n")
        return exchange_rate
    else:
        print(f"Error: {response.status_code}")
        return None

def currency_converter(rate, amount):
    new_value = rate * amount
    return new_value

def convert_currency():
    current_time = datetime.now()
    current_time = current_time.strftime("%I:%M %p")

    from_currency = old_currency_input.get().upper()
    amount_to_convert = amount_input.get()
    to_currency = new_currency_input.get().upper()

    if not verify_input(from_currency, to_currency, amount_to_convert):
        result_label.config(text=f"Invalid Entry!\nPlease read instructions again and enter data\nCurrent Time: {current_time}\n")
        style.configure("Rounded.TFrame", background="red", relief="groove")
        return None

    amount_to_convert = float(amount_to_convert)
    rate = currency_phaser(to_currency.upper(), from_currency.upper())

    if rate is not None:
        converted_amount = currency_converter(rate, amount_to_convert)
        all_currency = get_currencies()
        currency_1 = all_currency[f'{to_currency}']
        currency_2 = all_currency[f'{from_currency}']

        result_text = f"{currency_2} to {currency_1}\nExchange rate:  ~{to_currency} {rate:.2f} per {from_currency.upper()}\n\n{from_currency.upper()} {amount_to_convert:.2f}  ≈  {to_currency.upper()} {converted_amount:.2f}\nCurrent Time:  {current_time}\n"
        result_label.config(text=result_text)
        style.configure("Rounded.TFrame", background="green", relief="groove")
    else:
        result_label.config(text=f"Conversion failed!\nRetry\nCurrent Time: {current_time}\n\n")
        style.configure("Rounded.TFrame", background="red", relief="groove")

    old_currency_input.delete(0, 'end')
    amount_input.delete(0, 'end')
    new_currency_input.delete(0, 'end')

root = Tk()
root.title("Currency Converter")
root.configure(bg="#1d1e1f")

old_currency_label = Label(root, text="Enter original currency symbol (Ex. USD, CAD, EUR, BTC)", bg="#1d1e1f", font=('FixedSys', 12))
old_currency_input = ttk.Entry(root, style="Rounded.TEntry")
amount_label = Label(root, text="\nEnter amount to convert", bg="#1d1e1f", font=('FixedSys', 12))
amount_input = ttk.Entry(root, style="Rounded.TEntry")
new_currency_label = Label(root, text="\nEnter target currency symbol (Ex. USD, CAD, EUR, BTC)", bg="#1d1e1f", font=('FixedSys', 12))
new_currency_input = ttk.Entry(root, style="Rounded.TEntry")
result_label_frame_1 = ttk.Frame(root, style="Rounded.TFrame")
result_label_frame_2 = ttk.Frame(result_label_frame_1, style="Rounded.TFrame")
result_label = Label(result_label_frame_2, text="\n\n Enter excahnge currencies and amount,\nthen select convert\n\n", bg="#131313", fg="white", wraplength=400, font=('FixedSys', 12))
convert_button = ttk.Button(root, text="Convert", command=convert_currency, style="TButton")
exit_button = ttk.Button(root, text="Exit", command=root.destroy,style="TButton" )

result_label_frame_1.pack(pady=10)
result_label_frame_2.pack(pady=5, padx=5)
result_label.pack()
old_currency_label.pack()
old_currency_input.pack()
amount_label.pack()
amount_input.pack()
new_currency_label.pack()
new_currency_input.pack()
convert_button.pack(anchor="s")
exit_button.pack(anchor="s")

style = ttk.Style()
style.configure("Rounded.TEntry", borderwidth=0, bordercolor="blue", relief="flat", background="blue", padding=(5, 5), width=200)
style.configure("Rounded.TFrame", background="blue", relief="groove")
style.configure("TButton", font=('FixedSys', 12), foreground='white', width=7, height=4)


root.mainloop()
