import tkinter as tk
from tkinter import ttk


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call("source", "Azure-ttk-theme/azure.tcl")
        self.tk.call("set_theme", "light")

        self.title('Калькулятор Лебедевича')
        # self.iconbitmap(r".ico")

        self.geometry("1000x500")

        self.fio_label = ttk.Label(self, text="ФИО студента: Лебедевич Артем Владимирович", font=("Arial", 12))
        self.fio_label.pack()

        self.course_label = ttk.Label(self, text="Курс: 3 курс", font=("Arial", 12))
        self.course_label.pack()

        self.group_label = ttk.Label(self, text="Группа: 12 группа", font=("Arial", 12))
        self.group_label.pack()

        self.year_label = ttk.Label(self, text="Год: 2023", font=("Arial", 12))
        self.year_label.pack()

        self.num1_label = ttk.Label(self, text="Число 1:", font=("Arial", 12))
        self.num1_label.pack()

        self.num1_entry = ttk.Entry(self, font=("Arial", 12))
        self.num1_entry.pack()

        self.num2_label = ttk.Label(self, text="Число 2:", font=("Arial", 12))
        self.num2_label.pack()

        self.num2_entry = ttk.Entry(self, font=("Arial", 12))
        self.num2_entry.pack()

        self.operation_label = ttk.Label(self, text="Операция:", font=("Arial", 12))
        self.operation_label.pack()

        self.operation_var = tk.StringVar(self)
        self.operation_var.set("+")

        self.operation_optionmenu = ttk.OptionMenu(self, self.operation_var, "+", "-")
        self.operation_optionmenu.pack()

        self.calculate_button = ttk.Button(self, text="Вычислить", style="Accent.TButton", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.result_label.pack()

        self.bind("<Control-c>", self.copy)
        self.bind("<Control-v>", self.paste)

        self.clipboard = ""

    # def set_style(self):
    #     # style = AzureStyle()
    #     # style.set_theme("Blue")
    #     # self.style = style
    #
    #     self.style.configure("TLabel", font=("Arial", 12))
    #     self.style.configure("TButton", font=("Arial", 12))
    #     self.style.configure("AccentButton.TButton", font=("Arial", 12), foreground="white", background="#0078D7")
    #     self.style.configure("TEntry", font=("Arial", 12), padding=5)

    def calculate(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        operation = self.operation_var.get()

        try:
            num1 = self.parse_number(num1)
            num2 = self.parse_number(num2)

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2

            self.result_label.config(text="Результат: {}".format(result))
        except ValueError:
            self.result_label.config(text="Ошибка: неверный формат чисел")
        except OverflowError:
            self.result_label.config(text="Ошибка: переполнение")

    def parse_number(self, number):
        number = number.replace(",", ".")  # Замена запятой на точку
        if "e" in number:
            raise ValueError("Число в экспоненциальной нотации")
        return float(number)

    def copy(self, event):
        if self.focus_get() in (self.num1_entry, self.num2_entry):
            self.clipboard = self.focus_get().get()

    def paste(self, event):
        if self.focus_get() in (self.num1_entry, self.num2_entry):
            self.focus_get().insert("insert", self.clipboard)


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()