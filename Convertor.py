from cgitb import text
from string import digits
from tkinter import *
import requests
import customtkinter

options = [
    "CAD/Canada Dollar",
    "GBP/Great Britain",
    "USD/Dollar",
    "EUR/Euro",
    "BGN/Bulgaria",
    "JPY/Japanese Yen",
    "AUD/Australian Dollar",
    "CHF/Swiss franch",
    "NZD/New Zealand Dollar",
    "HKD/Hong Kong Dollar",
    "TRY/Turkish lira",
    "RUB/Russian ruble"
]

label = " "
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        amount = amount / self.currencies[from_currency]

        # 3 decimal places
        amount = round(amount * self.currencies[to_currency], 3)
        return amount


class App(customtkinter.CTk):
    def __init__(self, converter):
        super().__init__()
        self.title('Currency Converter')
        self.currency_converter = converter
        self.configure(background="white")
        self.resizable(0, 0)
        self.geometry("380x510")
        self.imported_Text = StringVar()
        self.fromtext = StringVar()
        self.fromtext.set("EUR/Euro")
        self.totext = StringVar()
        self.totext.set("USD/Dollar")
        inputOutputFrame(self)
        inputOutputField(self)
        dropbox(self)
        customtkinter.CTkButton(text="Convert", width=380, height=20, bd=0, bg="#0000eb",
                                cursor="hand2",
                                command=lambda: execute(self)).pack(ipady=50)
        add_label()

        def execute(self):
            global label
            amount = self.imported_Text.get()
            amount = float(''.join(c for c in amount if c in digits))
            from_curr = self.fromtext.get()
            to_curr = self.totext.get()
            converted_amount = self.currency_converter.convert(
                from_curr[0: 3], to_curr[0: 3], amount)
            converted_amount = round(converted_amount, 2)
            update_label(str(converted_amount), amount, from_curr, to_curr)


def add_label():
    global label
    label = Label(fg="blue", font="Times 14 italic")
    label.pack(ipady=10)


def update_label(entry, amount, fromcurre, currency):
    global label
    finallabel = str(amount) + " " + \
        fromcurre[0:3] + " = " + entry + " " + currency[0:3]
    label["text"] = str(finallabel)


def inputOutputFrame(self):
    self.input_Output_Field_Frame = customtkinter.CTkFrame(bd=0, highlightbackground="white", highlightcolor="blue",
                                                           highlightthickness=2)
    self.input_Output_Field_Frame.pack()


def inputOutputField(self):
    self.input_Output_Field = customtkinter.CTkEntry(self.input_Output_Field_Frame,
                                                     textvariable=self.imported_Text, width=380,
                                                     bg="#ebeded", justify=LEFT)
    self.input_Output_Field.pack(ipady=10)


def dropbox(self):
    self.drop = OptionMenu(self, self.fromtext, *options,)
    self.drop2 = OptionMenu(self, self.totext, *options)
    self.drop.configure(width=50, height=6, bd=2, font=(
        'calibri', (15)), bg='grey', highlightbackground="#5e5c5c", highlightcolor="#5e5c5c")
    self.drop2.configure(width=50, height=6, bd=2, font=(
        'calibri', (15)), bg='grey', highlightbackground="#5e5c5c", highlightcolor="#5e5c5c")
    self.drop.pack()
    self.drop2.pack()


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    app = App(converter)
    app.mainloop()
