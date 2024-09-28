import sys
from ft_filter import ft_filter


def check_string(s: str) -> bool:
    """
check_string(s) --> bool

Return True if the string s contains only letters, False otherwise.
"""
    # split the string into words
    words = s.split()

    # check if the words have any punctuation or invisible characters
    for word in words:
        if not word.isalpha():
            return False

    return True


def check_int(n: str) -> bool:
    """
check_int(n) --> bool

Return True if n is a positive integer, False otherwise.
"""
    try:
        n = int(n)
        if n > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    args = sys.argv[1:]

    assert len(args) == 2, 'the arguments are bad'

    assert check_string(args[0]), 'the arguments are bad'
    assert check_int(args[1]), 'the arguments are bad'

    words = args[0].split()
    length = int(args[1])

    print([word for word in ft_filter(lambda x: len(x) > length, words)])


if __name__ == '__main__':
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
