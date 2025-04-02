import subprocess
import re


def test_format_ft_time_output():
    # Run the script and capture output
    result = subprocess.run(
        ["python3", "format_ft_time.py"], capture_output=True, text=True
    )
    output = result.stdout.strip().split('\n')

    # Check we got exactly 2 lines
    assert len(output) == 2, "Expected exactly 2 lines of output"

    line1 = output[0]
    line2 = output[1]

    # Check line 1 format using regex
    pattern1 = (
        r"^Seconds since January 1, 1970: ([\d,]+\.\d{4}) or "
        r"(\d\.\d{2}e\+\d{2}) in scientific notation$"
    )
    assert re.match(pattern1, line1), f"Line 1 format incorrect: {line1}"

    # Check line 2 format (e.g., Oct 21 2022)
    pattern2 = r"^[A-Z][a-z]{2} \d{2} \d{4}$"
    assert re.match(pattern2, line2), f"Line 2 format incorrect: {line2}"
