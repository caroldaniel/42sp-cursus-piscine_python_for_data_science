import sys

def check_odd_even(num):
    if num % 2 == 0:
        return "I'm Even"
    else:
        return "I'm Odd"
    

def main():
    # Check whether the number of arguments is correct
    if len(sys.argv) < 2:
        return
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    
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