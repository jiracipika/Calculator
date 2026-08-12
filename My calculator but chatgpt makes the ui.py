import tkinter as tk
from tkinter import ttk

from calculator_core import CalculationError, calculate, format_result


OPERATIONS = {
    "Add (+)": "+",
    "Subtract (-)": "-",
    "Multiply (×)": "*",
    "Divide (÷)": "/",
    "Remainder (%)": "%",
    "Square root (√)": "^",
}


def create_app() -> tk.Tk:
    window = tk.Tk()
    window.title("Calculator")
    window.minsize(360, 250)

    frame = ttk.Frame(window, padding=16)
    frame.grid(sticky="nsew")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    ttk.Label(frame, text="First number:").grid(row=0, column=0, sticky="w", pady=5)
    first_entry = ttk.Entry(frame)
    first_entry.grid(row=0, column=1, sticky="ew", pady=5)

    second_label = ttk.Label(frame, text="Second number:")
    second_label.grid(row=1, column=0, sticky="w", pady=5)
    second_entry = ttk.Entry(frame)
    second_entry.grid(row=1, column=1, sticky="ew", pady=5)

    ttk.Label(frame, text="Operation:").grid(row=2, column=0, sticky="w", pady=5)
    operation = tk.StringVar(value="Add (+)")
    operation_menu = ttk.Combobox(
        frame,
        textvariable=operation,
        values=list(OPERATIONS),
        state="readonly",
    )
    operation_menu.grid(row=2, column=1, sticky="ew", pady=5)

    result = tk.StringVar(value="Enter numbers and choose an operation.")
    result_label = ttk.Label(
        frame,
        textvariable=result,
        anchor="center",
        justify="center",
        wraplength=320,
    )
    result_label.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(16, 0))

    def update_operand_state(*_args: object) -> None:
        square_root = OPERATIONS[operation.get()] == "^"
        second_entry.configure(state="disabled" if square_root else "normal")
        second_label.configure(text="Second number (not needed):" if square_root else "Second number:")

    def run_calculation(*_args: object) -> None:
        try:
            value = calculate(
                OPERATIONS[operation.get()],
                first_entry.get(),
                second_entry.get(),
            )
        except CalculationError as error:
            result.set(f"Error: {error}")
            window.bell()
            return
        result.set(f"Result: {format_result(value)}")

    calculate_button = ttk.Button(frame, text="Calculate", command=run_calculation)
    calculate_button.grid(row=3, column=0, columnspan=2, pady=(12, 0))

    operation.trace_add("write", update_operand_state)
    window.bind("<Return>", run_calculation)
    window.bind("<KP_Enter>", run_calculation)
    window.bind("<Escape>", lambda _event: window.destroy())
    first_entry.focus_set()
    return window


if __name__ == "__main__":
    create_app().mainloop()
