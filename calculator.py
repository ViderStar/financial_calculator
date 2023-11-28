from decimal import *


class Calculator:
    def __init__(self, num) -> None:
        self.num = num
        self.method = "No r."

    def change_rounding(self, rounding):
        self.method = rounding

    def apply_rounding(self, value):
        value = Decimal(value)
        if self.method == "No r.":
            return round(value, 6)
        elif self.method == "Math.":
            return value.quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
        elif self.method == "Bank.":
            return value.quantize(Decimal('1.'), rounding=ROUND_HALF_EVEN)
        elif self.method == "Trunc.":
            return value.to_integral_value(rounding=ROUND_DOWN)

    def output(self, digit):
        return round(Decimal(digit), 6)

    def format(self, digit):
        number = self.apply_rounding(digit)
        int_part = int(number)
        frac_part = number - int_part
        formatted_int_part = '{:,}'.format(int_part).replace(',', ' ')
        if frac_part:
            if str(frac_part)[0] == '-':
                formatted_frac_part = str(frac_part)[3:].rstrip('0')
            else:
                formatted_frac_part = str(frac_part)[2:].rstrip('0')
            return f"{formatted_int_part}.{formatted_frac_part}"
        else:
            return formatted_int_part

    def plus(self, a, b):
        try:
            result = str(self.output(a) + self.output(b))
            return str(self.output(result))
        except:
            return "Something wrong!"

    def mupytiply(self, a, b):
        try:
            result = str(self.output(a) * self.output(b))
            return str(self.output(result))
        except:
            return str("Something wrong!")

    def minus(self, a, b):
        try:
            result = str(self.output(a) - self.output(b))
            return str(self.output(result))
        except:
            return str("Something wrong!")

    def divide(self, a, b):
        try:
            result = str(self.output(a) / self.output(b))
            return str(self.output(result))
        except:
            return str("Something wrong!")
