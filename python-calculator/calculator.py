
import tkinter as tk
import ast
import operator

# Window setup
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x490")
root.resizable(False, False)
root.configure(bg="#171923")

expression = tk.StringVar(value="")

# Safe arithmetic operations
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.Mod: operator.mod,
}

def calculate_node(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in operators:
        left = calculate_node(node.left)
        right = calculate_node(node.right)

        if isinstance(node.op, ast.Div) and right == 0:
            raise ZeroDivisionError

        return operators[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in operators:
        return operators[type(node.op)](calculate_node(node.operand))

    raise ValueError("Invalid expression")

def press(value):
    current = expression.get()

    if value == "C":
        expression.set("")
    elif value == "DEL":
        expression.set(current[:-1])
    elif value == "=":
        try:
            tree = ast.parse(current, mode="eval")
            result = calculate_node(tree.body)
            expression.set(str(result))
        except ZeroDivisionError:
            expression.set("Cannot divide by zero")
        except (ValueError, SyntaxError, TypeError, OverflowError):
            expression.set("Invalid expression")
    else:
        if current in ("Cannot divide by zero", "Invalid expression"):
            current = ""
        expression.set(current + value)

def keyboard_input(event):
    if event.char in "0123456789.+-%":
        press(event.char)
    elif event.char in "*/":
        press(event.char)
    elif event.char == "-":
        press("-")
    elif event.keysym in ("Return", "KP_Enter"):
        press("=")
    elif event.keysym == "BackSpace":
        press("DEL")
    elif event.keysym == "Escape":
        press("C")

# Display
display = tk.Entry(
    root,
    textvariable=expression,
    font=("Arial", 25),
    bg="#222536",
    fg="#FFFFFF",
    insertbackground="white",
    justify="right",
    bd=0,
    state="normal"
)
display.pack(fill="x", padx=18, pady=(25, 20), ipady=18)

# Button layout
buttons = [
    ["C", "DEL", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="],
]

button_frame = tk.Frame(root, bg="#171923")
button_frame.pack(expand=True, fill="both", padx=12, pady=(0, 15))

for r, row in enumerate(buttons):
    for c, value in enumerate(row):
        if value == "=":
            color = "#6C63FF"
        elif value in ("C", "DEL"):
            color = "#E76F51"
        elif value in ("%", "/", "*", "-", "+"):
            color = "#30364D"
        else:
            color = "#24283B"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 15, "bold"),
            bg=color,
            fg="white",
            activebackground="#8580FF",
            activeforeground="white",
            bd=0,
            relief="flat",
            command=lambda v=value: press(v),
            cursor="hand2"
        )
        button.grid(
            row=r,
            column=c,
            sticky="nsew",
            padx=4,
            pady=4
        )

for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

root.bind("<Key>", keyboard_input)

root.mainloop()
