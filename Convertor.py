from tkinter import *
import requests
import customtkinter

options = [
    "CAD",
    "GBP",
    "USD",
    "EUR"
]

label = " "
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        amount = amount / self.currencies[from_currency]

            # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 3)
        print(amount)
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
        self.totext = StringVar()
        self.v = StringVar()
        inputOutputFrame(self)
        inputOutputField(self)
        dropbox(self)
        customtkinter.CTkButton(text="Convert", width=380, height=20, bd=0, bg="#0000eb",
               cursor="hand2",
               command=lambda: perform(self)).pack(ipady=50)
        print(self.fromtext.get())

        def perform(self):
            global label
            amount = float(self.imported_Text.get())
            from_curr = self.fromtext.get()
            to_curr = self.totext.get()

            converted_amount= self.currency_converter.convert(from_curr,to_curr,amount)
            converted_amount = round(converted_amount, 2)
            Label(converted_amount)



def Label(entry):
    global label
    label = entry
    label_1 = customtkinter.CTkLabel(text_color="black")
    label_1.pack(pady=12, padx=10)
    label_1.set_text(label)
    print("Printing label ", label, "and entry ", entry)




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
    self.drop.configure(width=50, height=6, bd=2,font=('calibri',(15)),bg='grey', highlightbackground="#5e5c5c", highlightcolor="#5e5c5c")
    self.drop2.configure(width=50, height=6, bd=2,font=('calibri',(15)),bg='grey', highlightbackground="#5e5c5c", highlightcolor="#5e5c5c")
    self.drop.pack()
    self.drop2.pack()


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    app = App(converter)
    app.mainloop()



