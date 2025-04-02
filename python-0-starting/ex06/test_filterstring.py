import subprocess
import sys


def run_script(*args):
    """
    Runs filterstring.py with CLI arguments.
    Returns: stdout, stderr, returncode
    """
    result = subprocess.run(
        [sys.executable, "filterstring.py", *args],
        capture_output=True,
        text=True,
        timeout=3
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def test_valid_input():
    out, _, code = run_script("Hello the World", "4")
    assert out == "['Hello', 'World']"
    assert code == 0


def test_no_match():
    out, _, code = run_script("Hi no low", "10")
    assert out == "[]"
    assert code == 0


def test_single_word():
    out, _, code = run_script("Python", "3")
    assert out == "['Python']"
    assert code == 0


def test_uppercase_and_lowercase():
    out, _, code = run_script("HELLO Hello", "4")
    assert out == "['HELLO', 'Hello']"
    assert code == 0


def test_too_few_args():
    out, _, code = run_script("onlyone")
    assert out == "AssertionError: the arguments are bad"
    assert code == 1


def test_too_many_args():
    out, _, code = run_script("one two", "2", "extra")
    assert out == "AssertionError: the arguments are bad"
    assert code == 1


def test_non_integer_threshold():
    out, _, code = run_script("Hello World", "three")
    assert out == "AssertionError: the arguments are bad"
    assert code == 1


def test_string_with_numbers():
    out, _, code = run_script("Hello 123World", "3")
    assert out == "AssertionError: the arguments are bad"
    assert code == 1


def test_string_with_symbols():
    out, _, code = run_script("Hello! okay", "2")
    assert out == "AssertionError: the arguments are bad"
    assert code == 1


def test_exact_match_length():
    out, _, code = run_script("Word five match", "4")
    assert out == "['match']"
    assert code == 0
