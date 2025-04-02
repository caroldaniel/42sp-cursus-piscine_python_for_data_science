import subprocess
import sys


def run_sos_script(*args):
    """
    Run the sos.py script with given command-line arguments.
    Returns (stdout, stderr, returncode)
    """
    result = subprocess.run(
        [sys.executable, "sos.py", *args],
        capture_output=True,
        text=True,
        timeout=3
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def test_hello_world():
    out, _, code = run_sos_script("Hello World")
    expected = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    assert out == expected
    assert code == 0


def test_uppercase_and_numbers():
    out, _, code = run_sos_script("PYTHON 123")
    expected = ".--. -.-- - .... --- -. / .---- ..--- ...--"
    assert out == expected
    assert code == 0


def test_only_numbers():
    out, _, code = run_sos_script("0123456789")
    expected = "----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----."
    assert out == expected
    assert code == 0


def test_one_word():
    out, _, code = run_sos_script("Test")
    expected = "- . ... -"
    assert out == expected
    assert code == 0


def test_extra_spaces_preserved():
    out, _, code = run_sos_script("Hi   there")
    assert "/ /" in out  # one or more slashes for multiple spaces
    assert ".... .." in out and "- .... . .-. ." in out
    assert code == 0


def test_invalid_characters_exclamation():
    out, _, code = run_sos_script("Hello!")
    assert "AssertionError: the arguments are bad" in out
    assert code == 1


def test_invalid_characters_at_symbol():
    out, _, code = run_sos_script("Email@here")
    assert "AssertionError: the arguments are bad" in out
    assert code == 1


def test_too_few_args():
    out, _, code = run_sos_script()
    assert "AssertionError: the arguments are bad" in out
    assert code == 1


def test_too_many_args():
    out, _, code = run_sos_script("Hello", "World")
    assert "AssertionError: the arguments are bad" in out
    assert code == 1
