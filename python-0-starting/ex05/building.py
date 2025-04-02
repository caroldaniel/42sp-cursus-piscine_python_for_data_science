import sys
import string


def analyze_text(text: str) -> dict:
    """
    Analyze the text and return counts of character types.

    Parameters:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with counts for total characters, upper letters,
              lower letters, punctuation marks, spaces, and digits.
    """
    return {
        "characters": len(text),
        "upper": sum(1 for c in text if c.isupper()),
        "lower": sum(1 for c in text if c.islower()),
        "punctuation": sum(1 for c in text if c in string.punctuation),
        "spaces": sum(1 for c in text if c.isspace()),
        "digits": sum(1 for c in text if c.isdigit()),
    }


def prompt_input(prompt: str) -> str:
    """
    Read characters one-by-one until Enter is pressed, handling both
    \n and \r\n.
    """
    print(prompt, flush=True)
    result = []
    while True:
        char = sys.stdin.read(1)
        if not char:  # End-of-file reached
            break
        if char == '\n':
            # Newline encountered; check if it's part of \r\n
            last_char = result[-1] if result else None
            if not last_char or last_char != '\r':
                result.append('\r')
            break
        result.append(char)
    return ''.join(result)


def text_analyzer(text: str) -> None:
    """
    Analyze the input text and print counts of different character types.

    Parameters:
        text (str): The text to analyze.
    """
    counts = analyze_text(text)
    print(f"The text contains {counts['characters']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main() -> None:
    """
    Entry point of the program. Handles CLI arguments and input.
    Reads from sys.stdin until EOF if no CLI argument is provided.
    """
    try:
        args = sys.argv[1:]
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")

        text = ""

        if len(args) == 1:
            text = args[0]
        elif len(args) == 0:
            text = prompt_input("What is the text to count?")
        else:
            raise AssertionError("too many arguments provided.")

        text_analyzer(text)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
