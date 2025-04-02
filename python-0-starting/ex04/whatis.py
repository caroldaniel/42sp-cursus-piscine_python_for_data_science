import sys


def check_odd_even(num):
    """
    Returns a string indicating whether the number is even or odd.
    """
    return "I'm Even." if num % 2 == 0 else "I'm Odd."


def main():
    args_len = len(sys.argv)

    # No arguments provided
    if args_len < 2:
        return

    # More than one argument provided
    if args_len > 2:
        raise AssertionError("more than one argument is provided")

    # Try converting argument to integer
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    print(check_odd_even(num))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
