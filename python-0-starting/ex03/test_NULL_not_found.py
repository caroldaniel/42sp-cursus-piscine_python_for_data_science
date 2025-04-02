import subprocess
from NULL_not_found import NULL_not_found


def test_null_not_found_function(capfd):
    assert NULL_not_found(None) == 0
    out, _ = capfd.readouterr()
    assert out.strip() == "Nothing: None <class 'NoneType'>"

    assert NULL_not_found(float('NaN')) == 0
    out, _ = capfd.readouterr()
    assert "Cheese: nan <class 'float'>" in out.strip()

    assert NULL_not_found(0) == 0
    out, _ = capfd.readouterr()
    assert out.strip() == "Zero: 0 <class 'int'>"

    assert NULL_not_found('') == 0
    out, _ = capfd.readouterr()
    assert out.strip() == "Empty: <class 'str'>"

    assert NULL_not_found(False) == 0
    out, _ = capfd.readouterr()
    assert out.strip() == "Fake: False <class 'bool'>"

    assert NULL_not_found("Brian") == 1
    out, _ = capfd.readouterr()
    assert out.strip() == "Type not Found"


def test_tester_py_script():
    result = subprocess.run(
        ["python3", "tester.py"],
        capture_output=True,
        text=True
    )
    output = result.stdout.strip().split("\n")

    expected_lines = [
        "Nothing: None <class 'NoneType'>",
        "Cheese: nan <class 'float'>",
        "Zero: 0 <class 'int'>",
        "Empty: <class 'str'>",
        "Fake: False <class 'bool'>",
        "Type not Found",
        "1"
    ]
    assert output == expected_lines, (
        f"Expected:\n{expected_lines}\nGot:\n{output}"
    )


def test_null_not_found_file_execution():
    result = subprocess.run(
        ["python3", "NULL_not_found.py"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "", (
        "Expected no output when running NULL_not_found.py directly"
    )
