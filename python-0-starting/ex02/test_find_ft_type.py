import subprocess
from find_ft_type import all_thing_is_obj


def test_function_outputs(capfd):
    # Test List
    assert all_thing_is_obj(["Hello", "tata!"]) == 42
    out, _ = capfd.readouterr()
    assert out.strip() == "List : <class 'list'>"

    # Test Tuple
    assert all_thing_is_obj(("Hello", "toto!")) == 42
    out, _ = capfd.readouterr()
    assert out.strip() == "Tuple : <class 'tuple'>"

    # Test Set
    assert all_thing_is_obj({"Hello", "tutu!"}) == 42
    out, _ = capfd.readouterr()
    assert out.strip() == "Set : <class 'set'>"

    # Test Dict
    assert all_thing_is_obj({"Hello": "titi!"}) == 42
    out, _ = capfd.readouterr()
    assert out.strip() == "Dict : <class 'dict'>"

    # Test "Brian"
    assert all_thing_is_obj("Brian") == 42
    out, _ = capfd.readouterr()
    assert out.strip() == "Brian is in the kitchen : <class 'str'>"

    # Test "Toto"
    assert all_thing_is_obj("Toto") == 42
    out, _ = capfd.readouterr()
    assert out.strip() == "Toto is in the kitchen : <class 'str'>"

    # Test unexpected type
    assert all_thing_is_obj(10) == 42
    out, _ = capfd.readouterr()
    assert out.strip() == "Type not found"


def test_tester_script_execution():
    result = subprocess.run(
        ["python3", "tester.py"],
        capture_output=True,
        text=True
    )
    output = result.stdout.strip().split('\n')

    expected = [
        "List : <class 'list'>",
        "Tuple : <class 'tuple'>",
        "Set : <class 'set'>",
        "Dict : <class 'dict'>",
        "Brian is in the kitchen : <class 'str'>",
        "Toto is in the kitchen : <class 'str'>",
        "Type not found",
        "42"
    ]

    assert output == expected, f"Expected:\n{expected}\n\nGot:\n{output}"


def test_find_ft_type_execution_alone():
    result = subprocess.run(
        ["python3", "find_ft_type.py"],
        capture_output=True,
        text=True
    )
    output = result.stdout.strip()
    assert output == "", f"Expected no output, but got: {output}"
