import time
import sys
import shutil


def ft_tqdm(lst: range) -> None:  # type: ignore
    total = len(lst)
    start_time = time.time()

    # Get terminal width for dynamic bar size
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    bar_width = max(10, terminal_width - 40)

    for i, item in enumerate(lst, 1):
        percent_complete = i / total

        # Calculate the time remaining
        elapsed_time = time.time() - start_time
        rate = i / elapsed_time if elapsed_time > 0 else 0
        remaining_time = (total - i) / rate if rate > 0 else 0

        # Build the progress bar
        filled_length = int(bar_width * percent_complete)
        bar = '█' * filled_length + '-' * (bar_width - filled_length)

        # Convert elapsed_time and remaining_time to mm:ss format
        elapsed_minutes, elapsed_seconds = divmod(elapsed_time, 60)
        remaining_minutes, remaining_seconds = divmod(remaining_time, 60)

        # Print the progress bar
        sys.stdout.write(
            f'\r{percent_complete:>4.0%}|{bar}| {i}/{total} '
            f'[{int(elapsed_minutes):02}:{int(elapsed_seconds):02}<'
            f'{int(remaining_minutes):02}:{int(remaining_seconds):02}, '
            f'{rate:.2f}it/s]'
        )
        sys.stdout.flush()  # Force print the progress

        # Yield the item to the caller
        yield item

    # Final newline after completion
    sys.stdout.write('\n')
