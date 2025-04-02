import time
from datetime import datetime


def format_time_float(current_time):
    """Format the current time as a float."""
    return f"{current_time:,.4f}"


def format_time_scientific(current_time):
    """Format the current time in scientific notation."""
    return f"{current_time:.2e}"


def format_time_human_readable(datetime_now):
    """Convert the current time to a human-readable format."""
    return datetime_now.strftime('%b %d %Y')


def main():
    # Get the current time
    current_time = time.time()

    # Print timestamp in float and scientific notation
    print(
        f"Seconds since January 1, 1970: "
        f"{format_time_float(current_time)} "
        f"or {format_time_scientific(current_time)} in scientific notation"
    )

    # Print in a human-readable format
    datetime_now = datetime.now()
    print(format_time_human_readable(datetime_now))


if __name__ == '__main__':
    main()
