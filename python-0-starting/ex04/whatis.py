import sys


def check_odd_even(num):
    if num % 2 == 0:
        return "I'm Even"
    else:
        return "I'm Odd"


def main():
    args_len = len(sys.argv)

    # Check if no arguments are provided
    if args_len < 2:
        return

    # Check whether the number of arguments is correct
    assert args_len == 2, "more than one argument is provided"

    # Check if the argument is an integer
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    # Check if it's odd or even
    print(check_odd_even(num))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
