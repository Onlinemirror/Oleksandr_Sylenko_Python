#Sylenko_Oleksandr, Python
def main():
    # Part 1: Number Check
    try:
        number = float(input("Enter a number: "))
        if number <= 7:
            print("Number is less than or equal to 7. Exiting program.")
            exit()  # Terminate program if number is <= 7
        print("Hello")
    except ValueError:
        print("Invalid number input. Exiting program.")
        exit()

    # Part 2: Name Check
    name = input("Enter a name: ")
    if name != "John":
        print("There is no such name. Exiting program.")
        exit()  # Terminate program if name is not "John"
    print("Hello, John")

    # Part 3: Array Processing
    print("\nArray Processing:")
    try:
        array_input = input("Enter a numeric array (comma-separated): ")
        array = [int(x) for x in array_input.split(",")]
        multiples_of_three = [x for x in array if x % 3 == 0]
        print("Elements that are multiples of 3:", multiples_of_three)
    except ValueError:
        print("Invalid array input. Exiting program.")
        exit()

    # Part 4: Bracket Sequence Analysis
    sequence = input("\nEnter a bracket sequence, for example [((())()(())]]: ")  # User enters the sequence
    if is_correct_bracket_sequence(sequence):
        print(f"The bracket sequence '{sequence}' is correct.")
    else:
        print(f"The bracket sequence '{sequence}' is incorrect.")
        corrected_sequence = fix_bracket_sequence(sequence)
        print(f"Corrected sequence: {corrected_sequence}")


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
        elif char == "]":  
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


if __name__ == "__main__":
    main()