import time
import datetime


def main():
    # Get the current time
    current_time = time.time()

    # Convert to a human-readable format
    readable_time = datetime.datetime.fromtimestamp(current_time).strftime('%b %d %Y')

    # Print the results
    print(f"Seconds since January 1, 1970: {current_time:.4f} or {current_time:.2e} in scientific notation")
    print(readable_time)


if __name__ == '__main__':
    main()
