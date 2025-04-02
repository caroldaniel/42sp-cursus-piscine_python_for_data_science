import subprocess
import sys


def run_script_with_args(*args):
    """
    Helper to run building.py with CLI arguments.
    Returns stdout, stderr, exit_code.
    """
    result = subprocess.run(
        [sys.executable, "building.py", *args],
        capture_output=True,
        text=True,
        timeout=3
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def run_script_without_args(user_input: str):
    """
    Helper to run building.py without CLI arguments, using prompt input.
    Simulates Enter (with `\n`) or Ctrl+D (with empty string).
    """
    result = subprocess.run(
        [sys.executable, "building.py"],
        input=user_input,
        capture_output=True,
        text=True,
        timeout=3
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


# ✅ Core Functional Tests
def test_given_paragraph_from_subject():
    """
    Test case based on the exact example from the subject PDF.
    """
    text = (
        "Python 3.0, released in 2008, was a major revision that is not "
        "completely backward-compatible with earlier versions. Python 2 "
        "was discontinued with version 2.7.18 in 2020."
    )

    expected = [
        "The text contains 171 characters:",
        "2 upper letters",
        "121 lower letters",
        "8 punctuation marks",
        "25 spaces",
        "15 digits"
    ]

    out, _, code = run_script_with_args(text)
    output_lines = out.strip().splitlines()

    for line in expected:
        assert line in output_lines, f"Missing or incorrect: '{line}'"

    assert code == 0


def test_valid_argument():
    """
    Checks counts for a simple sentence.
    """
    text = "Python 3.0, released in 2008."
    expected = [
        "The text contains 29 characters:",
        "1 upper letters",
        "15 lower letters",
        "3 punctuation marks",
        "4 spaces",
        "6 digits"
    ]

    out, _, code = run_script_with_args(text)
    output_lines = out.strip().splitlines()

    for line in expected:
        assert line in output_lines, f"Missing or incorrect: '{line}'"

    assert code == 0


def test_assertion_error_for_multiple_args():
    """
    Ensures the script raises AssertionError with > 1 argument.
    """
    out, _, code = run_script_with_args("Hello", "World")

    assert out == "AssertionError: more than one argument is provided"
    assert code == 1


# ❌ Error handling tests
def test_multiple_args_error():
    out, _, code = run_script_with_args("hello", "world")
    assert out == "AssertionError: more than one argument is provided"
    assert code == 1


# ✅ Prompt Input Test
def test_prompt_displays_message():
    result = subprocess.run(
        [sys.executable, "building.py"],
        input="Hello\n",  # input doesn't matter
        capture_output=True,
        text=True
    )
    assert "What is the text to count?" in result.stdout


def test_ctrl_d_no_input():
    out, _, code = run_script_without_args("")
    expected = [
        "The text contains 0 characters:",
        "0 upper letters",
        "0 lower letters",
        "0 punctuation marks",
        "0 spaces",
        "0 digits"
    ]
    for line in expected:
        assert line in out
    assert code == 0


def test_ctrl_d_after_input_buffer():
    result = subprocess.run(
        [sys.executable, "building.py"],
        input="Hello World!",
        capture_output=True,
        text=True,
        timeout=3
    )

    expected = [
        "The text contains 12 characters:",
        "2 upper letters",
        "8 lower letters",
        "1 punctuation marks",
        "1 spaces",
        "0 digits"
    ]

    output_lines = result.stdout.strip().splitlines()
    for line in expected:
        assert line in output_lines

    assert result.returncode == 0


def test_enter_after_input_buffer():
    result = subprocess.run(
        [sys.executable, "building.py"],
        input="Hello World!\n",  # Simulates pressing Enter
        capture_output=True,
        text=True,
        timeout=3
    )

    expected = [
        "The text contains 13 characters:",
        "2 upper letters",
        "8 lower letters",
        "1 punctuation marks",
        "2 spaces",  # Because prompt_input() appends '\r'
        "0 digits"
    ]

    output_lines = result.stdout.strip().splitlines()
    for line in expected:
        assert line in output_lines

    assert result.returncode == 0


def test_enter_after_input_buffer_with_carriage():
    result = subprocess.run(
        [sys.executable, "building.py"],
        input="Hello World!\r\n",
        capture_output=True,
        text=True,
        timeout=3
    )

    expected = [
        "The text contains 13 characters:",
        "2 upper letters",
        "8 lower letters",
        "1 punctuation marks",
        "2 spaces",  # Because prompt_input() appends '\r'
        "0 digits"
    ]

    output_lines = result.stdout.strip().splitlines()
    for line in expected:
        assert line in output_lines

    assert result.returncode == 0
