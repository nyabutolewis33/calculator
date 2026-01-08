from functools import reduce
import tkinter as tk
from tkinter import ttk, messagebox
import re

def apply_operation(nums, op):
    if op in ('+', 'add'):
        return sum(nums)
    if op in ('*', 'x', 'multiply'):
        return reduce(lambda x, y: x * y, nums)
    if op in ('-', 'subtract'):
        return reduce(lambda x, y: x - y, nums)
    if op in ('/', 'divide'):
        return reduce(lambda x, y: x / y, nums)
    if op in ('%', 'mod', 'modulus'):
        return reduce(lambda x, y: x % y, nums)
    if op in ('//', 'floordiv'):
        return reduce(lambda x, y: x // y, nums)
    if op in ('**', '^', 'exp'):
        # left-associative exponent: ((a**b)**c)...
        return reduce(lambda x, y: x ** y, nums)
    raise ValueError(f"Unsupported operation: {op}")

def calculate():
    nums_str = entry_nums.get().strip()
    if not nums_str:
        messagebox.showerror("Error", "No numbers entered.")
        return

    parts = [p for p in re.split(r'[,\s]+', nums_str) if p]
    try:
        nums = [float(p) for p in parts]
    except ValueError:
        messagebox.showerror("Error", "Invalid number entered. Please enter numeric values.")
        return

    op = combo_op.get()
    try:
        result = apply_operation(nums, op)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero")
        return
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    label_result.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x250")

tk.Label(root, text="Enter numbers (space or comma separated):").pack(pady=5)
entry_nums = tk.Entry(root, width=50)
entry_nums.pack(pady=5)

tk.Label(root, text="Operation:").pack(pady=5)
combo_op = ttk.Combobox(root, values=['+', '-', '*', '/', '%', '//', '**'], state='readonly')
combo_op.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=5)

root.mainloop()
