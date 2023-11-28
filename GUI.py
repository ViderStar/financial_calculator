import tkinter as tk
from tkinter import ttk

buttons_func = [
    {"name": "Plus"},
    {"name": "Minus"},
    {"name": "Divide"},
    {"name": "Multiply"}
]

roundings = [
    {"name": "No r."},
    {"name": "Math."},
    {"name": "Bank."},
    {"name": "Trunc."}
]


class Fields:
    def __init__(self, num, root) -> None:
        self.num = num
        self.fields = []
        self.radiobuttons = []
        self.operators = []
        self.rounding = tk.StringVar(value=roundings[0]["name"])

        # Создание основной рамки
        main_frame = ttk.LabelFrame(root)
        main_frame.pack(pady=20, padx=20)

        for i in range(num):

            # Рамка для поля ввода
            input_frame = ttk.Frame(main_frame)
            input_frame.pack(pady=10, padx=10)

            # Текстовое поле
            entry = ttk.Entry(input_frame)
            entry.pack(fill="x", padx=5, pady=5)
            self.fields.append(entry)

            # Радиокнопки для операторов
            if i < num - 1:

                operator_frame = ttk.Frame(main_frame)
                operator_frame.pack(pady=10, padx=10)

                self.operators.append(tk.StringVar(value=buttons_func[0]["name"]))

                for val in buttons_func:
                    rb = ttk.Radiobutton(operator_frame, value=val["name"],
                                         text=val["name"],
                                         variable=self.operators[i])
                    rb.pack(side=tk.LEFT, padx=5)
                    self.radiobuttons.append(rb)
            else:

                rounding_frame = ttk.Frame(main_frame)
                rounding_frame.pack(pady=10, padx=10)

                for val in roundings:
                    rb = ttk.Radiobutton(rounding_frame, value=val["name"],
                                         text=val["name"],
                                         variable=self.rounding)
                    rb.pack(side=tk.LEFT, padx=5)
                    self.radiobuttons.append(rb)

    def get_values(self):
        values = [str(i.get()) for i in self.fields]
        return values

    def get_operators(self):
        operators = [str(i.get()) for i in self.operators]
        return operators

    def get_roundings(self):
        return self.rounding.get()
