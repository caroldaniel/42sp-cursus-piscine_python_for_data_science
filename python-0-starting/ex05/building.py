import sys
import string


def count_text(text: str) -> None:
    """
Count the number of uppercase, lowercase, digits, punctuation marks and
spaces in the given text.

Parameters:
    text (str): The text to count.

Returns:
    None

Example:
>>> count_text("Hello, World!")
The text contains 13 characters:
2 upper letters
8 lower letters
2 punctuation marks
1 spaces
0 digits
"""

    # Initialize the counters
    uppercase = 0
    lowercase = 0
    punctuation = 0
    digits = 0
    spaces = 0

    # Iterate over each character in the text
    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        elif char in string.punctuation:
            punctuation += 1
        else:
            pass

    # Print the results
    print(f"""The text contains {len(text)} characters:
{uppercase} upper letters
{lowercase} lower letters
{punctuation} punctuation marks
{spaces} spaces
{digits} digits""")
    return


def main() -> None:
    """
Main entry point for the program.

It raises an AssertionError if more than one argument is provided, and it
prompts the user to provide a text if no arguments are provided.

This function will parse the command-line arguments and call the count_text
function for the provided text.
"""

    args = sys.argv[1:]

    # If no arguments are provided, prompt the user to provide a string
    if not args:
        # ask for user's input
        text = input("What is the text to count?\n")
    else:
        text = args[0]

    assert len(args) <= 1, "only one argument is allowed"

    # Count the number of characters in the text
    count_text(text)
    return


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
