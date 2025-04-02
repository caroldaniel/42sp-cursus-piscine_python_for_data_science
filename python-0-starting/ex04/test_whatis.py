import subprocess


def run_script(*args):
    """
    Helper to run whatis.py with command-line arguments.
    Returns:
        stdout (str), stderr (str), returncode (int)
    """
    result = subprocess.run(
        ["python3", "whatis.py", *args],
        capture_output=True,
        text=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


# ✅ Valid integer tests

def test_even_number():
    out, _, code = run_script("10")
    assert out == "I'm Even."
    assert code == 0


def test_odd_number():
    out, _, code = run_script("3")
    assert out == "I'm Odd."
    assert code == 0


def test_zero():
    out, _, code = run_script("0")
    assert out == "I'm Even."
    assert code == 0


def test_negative_odd():
    out, _, code = run_script("-5")
    assert out == "I'm Odd."
    assert code == 0


def test_negative_even():
    out, _, code = run_script("-4")
    assert out == "I'm Even."
    assert code == 0


# ❌ Error handling tests

def test_no_argument():
    out, _, code = run_script()
    assert out == ""
    assert code == 0


def test_too_many_arguments():
    out, _, code = run_script("1", "2")
    assert out == "AssertionError: more than one argument is provided"
    assert code == 1


def test_non_integer_string():
    out, _, code = run_script("hello")
    assert out == "AssertionError: argument is not an integer"
    assert code == 1


def test_float_string():
    out, _, code = run_script("3.14")
    assert out == "AssertionError: argument is not an integer"
    assert code == 1


def test_special_characters():
    out, _, code = run_script("!@#")
    assert out == "AssertionError: argument is not an integer"
    assert code == 1
