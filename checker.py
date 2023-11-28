from calculator import Calculator
from GUI import Fields
import re
import tkinter
import tkinter as tk
from tkinter import ttk


class Checker:
    def __init__(self, num, root) -> None:
        self.inputs = Fields(num, root)
        self.result_display = ttk.Entry(root, state=tk.DISABLED, text='Output')

        self.result_display.pack(pady=10)
        self.calcul = Calculator(num)

    def check(self, inputs):
        checked = []
        for num_str in inputs:
            num_str = str(num_str.replace(",", "."))
            if self.is_valid_number(num_str):
                number = str(num_str.replace(" ", ""))
                checked.append(str(number))
            else:
                print(num_str)
                return []
        return checked

    def is_valid_number(self, num_str):
        pattern = r"^-?\d+(?:\.\d+)?$|^-?\d{1,3}(?: \d{3})*(?:\.\d+)?$"
        return bool(re.match(pattern, num_str))

    def change_output(self, result):
        self.result_display.config(state=tkinter.NORMAL)
        self.result_display.delete(0, tkinter.END)
        self.result_display.insert(0, result)
        self.result_display.config(state=tkinter.DISABLED)

    def calculate_callback(self):
        nums = self.check(self.inputs.get_values())
        if len(nums) == 0:
            self.change_output("Something wrong!")
        else:
            try:
                self.calcul.change_rounding(self.inputs.get_roundings())
                operators = self.inputs.get_operators()
                result = self.operator_to_func(operators[1], nums[1], nums[2])
                if (operators[2] == 'Multiply' or operators[2] == 'Divide') and (
                        operators[0] == 'Plus' or operators[0] == 'Minus'):
                    result = self.operator_to_func(operators[2], result, nums[3])
                    result = self.operator_to_func(operators[0], nums[0], result)
                else:
                    result = self.operator_to_func(operators[0], nums[0], result)
                    result = self.operator_to_func(operators[2], result, nums[3])
                result = self.calcul.format(result)
                print(result.find('.'))
                if result.find('.') > len('1 000 000 000 000'):
                    self.change_output("Something wrong!")
                elif result.find('.') == -1 and len(result) > len('1 000 000 000 000'):
                    self.change_output("Something wrong!")
                else:
                    self.change_output(result)
            except Exception as error:
                print(error)
                self.change_output("Something wrong!")

    def operator_to_func(self, operator, a, b):
        if operator == 'Plus':
            return self.calcul.plus(a, b)
        elif operator == 'Minus':
            return self.calcul.minus(a, b)
        elif operator == 'Multiply':
            return self.calcul.mupytiply(a, b)
        elif operator == 'Divide':
            return self.calcul.divide(a, b)
