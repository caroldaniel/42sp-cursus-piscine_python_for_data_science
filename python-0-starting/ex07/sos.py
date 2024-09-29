import sys


NESTED_MORSE = {
    'A': '.- ',
    'B': '-... ',
    'C': '-.-. ',
    'D': '-.. ',
    'E': '. ',
    'F': '..-. ',
    'G': '--. ',
    'H': '.... ',
    'I': '.. ',
    'J': '.--- ',
    'K': '-.- ',
    'L': '.-.. ',
    'M': '-- ',
    'N': '-. ',
    'O': '--- ',
    'P': '.--. ',
    'Q': '--.- ',
    'R': '.-. ',
    'S': '... ',
    'T': '- ',
    'U': '..- ',
    'V': '...- ',
    'W': '.-- ',
    'X': '-..- ',
    'Y': '-.-- ',
    'Z': '--.. ',
    '0': '----- ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '----. ',
    ' ': '/ '
}


def morse(s: str) -> str:
    """
morse(s) --> str

Return the morse code of the string s.
"""
    return ''.join([NESTED_MORSE.get(c, '') for c in s.upper()])


def main():
    """
Main entry point for the program.

Print the morse code of a string passed as an argument. The string must contain
only letters and numbers, otherwise an AssertionError is raised.
"""

    args = sys.argv[1:]

    assert len(args) == 1, 'the arguments are bad'

    for c in args[0]:
        if not c.isalnum() and c != ' ':
            raise AssertionError('the arguments are bad')

    print(morse(args[0]).strip())


if __name__ == '__main__':
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
