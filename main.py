import tkinter as tk
from tkinter import ttk

from checker import Checker



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("600x720")
    root.title("Artsem's Calculator")
    root.iconbitmap(r"img.ico")
    root.tk.call("source", "Azure-ttk-theme/azure.tcl")
    root.tk.call("set_theme", "light")

    num = 4
    name_label = ttk.Label(text="Artsem Lebiadzevich\n3 course, 12 group")
    name_label.pack(anchor=tk.N, pady=(20, 0))

    cntrl = Checker(num, root)

    calculate_button = ttk.Button(text="Calculate", style="Accent.TButton", command=cntrl.calculate_callback)
    calculate_button.pack(anchor=tk.S, pady=10)

    cntrl.result_display.pack(anchor=tk.S, pady=10)

    year_label = ttk.Label(text="2023")
    year_label.pack(anchor=tk.N)
    root.resizable(False, False)
    root.mainloop()
