import tkinter as tk
from tkinter import messagebox
import math


# -----------------------------
# Calculator Logic
# -----------------------------
def safe_eval(expression):
    allowed_names = {
        name: obj
        for name, obj in math.__dict__.items()
        if not name.startswith("__")
    }

    allowed_names.update(
        {
            "abs": abs,
            "round": round,
            "pow": pow,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "factorial": math.factorial,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
        }
    )

    return eval(expression, {"__builtins__": None}, allowed_names)


# -----------------------------
# GUI
# -----------------------------
class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("420x600")
        self.root.resizable(False, False)

        # Dark Theme Colors
        BG = "#121212"
        BTN = "#2D2D2D"
        HOVER = "#3A3A3A"
        TEXT = "#FFFFFF"
        ACCENT = "#00C896"
        ENTRY = "#1F1F1F"

        self.root.configure(bg=BG)

        self.expression = tk.StringVar()

        title = tk.Label(
            root,
            text="Advanced Calculator",
            font=("Segoe UI", 20, "bold"),
            bg=BG,
            fg=ACCENT
        )
        title.pack(pady=15)

        self.entry = tk.Entry(
            root,
            textvariable=self.expression,
            font=("Consolas", 22),
            justify="right",
            bg=ENTRY,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            bd=10
        )
        self.entry.pack(fill="x", padx=15, pady=10)

        button_frame = tk.Frame(root, bg=BG)
        button_frame.pack(pady=10)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["(", ")", "C", "⌫"]
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = tk.Button(
                    button_frame,
                    text=text,
                    width=8,
                    height=2,
                    font=("Segoe UI", 11, "bold"),
                    bg=BTN,
                    fg=TEXT,
                    activebackground=HOVER,
                    activeforeground=TEXT,
                    relief="flat",
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=r, column=c, padx=4, pady=4)

        # Functions
        func_frame = tk.LabelFrame(
            root,
            text="Functions",
            bg=BG,
            fg=ACCENT,
            font=("Segoe UI", 11, "bold")
        )
        func_frame.pack(fill="x", padx=15, pady=15)

        functions = [
            "sin(",
            "cos(",
            "tan(",
            "sqrt(",
            "log(",
            "factorial("
        ]

        for i, func in enumerate(functions):
            btn = tk.Button(
                func_frame,
                text=func[:-1],
                width=10,
                bg=BTN,
                fg=TEXT,
                activebackground=HOVER,
                activeforeground=TEXT,
                relief="flat",
                command=lambda f=func: self.add_function(f)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)

    def add_function(self, func):
        self.expression.set(
            self.expression.get() + func
        )

    def button_click(self, value):
        if value == "=":
            self.calculate()

        elif value == "C":
            self.expression.set("")

        elif value == "⌫":
            self.expression.set(
                self.expression.get()[:-1]
            )

        else:
            self.expression.set(
                self.expression.get() + value
            )

    def calculate(self):
        try:
            result = safe_eval(
                self.expression.get()
            )

            self.expression.set(str(result))

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )


if __name__ == "__main__":
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()