import tkinter as tk
from tkinter import messagebox

def check_number():
    """Check the entered number."""
    try:
        number = float(entry_number.get())
        if number <= 7:
            messagebox.showinfo("Result", "Number is less than or equal to 7. Exiting.")
            window.quit()  # Close the program
        else:
            messagebox.showinfo("Result", "Hello")
    except ValueError:
        messagebox.showerror("Error", "Invalid number input. Exiting.")
        window.quit()  # Close the program

def check_name():
    """Check the entered name."""
    name = entry_name.get()
    if name != "John":
        messagebox.showinfo("Result", "There is no such name. Exiting.")
        window.quit()  # Close the program
    else:
        messagebox.showinfo("Result", "Hello, John")

def process_array():
    """Process the entered numeric array."""
    try:
        array_input = entry_array.get()
        array = [int(x) for x in array_input.split(",")]
        multiples_of_three = [x for x in array if x % 3 == 0]
        messagebox.showinfo("Result", f"Elements that are multiples of 3: {multiples_of_three}")
    except ValueError:
        messagebox.showerror("Error", "Invalid array input. Exiting.")
        window.quit()  # Close the program

def analyze_bracket_sequence():
    """Analyze and correct the bracket sequence."""
    sequence = entry_sequence.get()
    if is_correct_bracket_sequence(sequence):
        messagebox.showinfo("Result", f"The bracket sequence '{sequence}' is correct.")
    else:
        corrected_sequence = fix_bracket_sequence(sequence)
        messagebox.showinfo("Result", f"The bracket sequence '{sequence}' is incorrect.\nCorrected sequence: {corrected_sequence}")

def is_correct_bracket_sequence(sequence):
    """Check if the given bracket sequence is correct."""
    stack = []
    for char in sequence:
        if char in "([":  # Opening brackets
            stack.append(char)
        elif char == ")":  # Closing parenthesis
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif char == "]":  # Closing square bracket
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
    return not stack  # If the stack is empty, it's correct

def fix_bracket_sequence(sequence):
    """Fix the given bracket sequence to make it correct."""
    stack = []
    corrections = []
    for char in sequence:
        if char in "([":  # Opening brackets
            stack.append(char)
            corrections.append(char)
        elif char == ")":  # Closing parenthesis
            if stack and stack[-1] == "(":
                stack.pop()
                corrections.append(char)
            else:
                corrections.append("(")  # Fix: Add matching opening bracket
                corrections.append(char)
        elif char == "]":  # Closing square bracket
            if stack and stack[-1] == "[":
                stack.pop()
                corrections.append(char)
            else:
                corrections.append("[")  # Fix: Add matching opening bracket
                corrections.append(char)
    # Add missing closing brackets for unclosed opening brackets
    while stack:
        corrections.append(")" if stack.pop() == "(" else "]")
    return "".join(corrections)

# Create the main window
window = tk.Tk()
window.title("Interactive Program")

# Create widgets
tk.Label(window, text="Enter a number:").grid(row=0, column=0)
entry_number = tk.Entry(window)
entry_number.grid(row=0, column=1)

tk.Button(window, text="Check Number", command=check_number).grid(row=0, column=2)

tk.Label(window, text="Enter a name:").grid(row=1, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=1, column=1)

tk.Button(window, text="Check Name", command=check_name).grid(row=1, column=2)

tk.Label(window, text="Enter a numeric array (comma-separated):").grid(row=2, column=0)
entry_array = tk.Entry(window)
entry_array.grid(row=2, column=1)

tk.Button(window, text="Process Array", command=process_array).grid(row=2, column=2)

tk.Label(window, text="Enter a bracket sequence:").grid(row=3, column=0)
entry_sequence = tk.Entry(window)
entry_sequence.grid(row=3, column=1)

tk.Button(window, text="Analyze Brackets", command=analyze_bracket_sequence).grid(row=3, column=2)

# Run the application
window.mainloop()
