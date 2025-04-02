from ft_filter import ft_filter


def test_positive_filter():
    result = list(ft_filter(lambda x: x > 0, [-2, 0, 1, 3]))
    assert result == [1, 3]


def test_even_numbers():
    result = list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
    assert result == [2, 4]


def test_none_function_identity_filter():
    result = list(ft_filter(None, [0, 1, "", "ok", False, True]))
    assert result == [1, "ok", True]


def test_string_with_str_methods():
    result = list(ft_filter(str.islower, "ABCdefGHI"))
    assert result == list("def")


def test_filter_on_tuple():
    result = list(ft_filter(lambda x: x == "keep", ("drop", "keep", "drop")))
    assert result == ["keep"]


def test_empty_iterable():
    result = list(ft_filter(lambda x: x, []))
    assert result == []


def test_generator_type_returned():
    gen = ft_filter(lambda x: x, [1, 2, 3])
    assert iter(gen) is gen  # is an iterator
    assert not isinstance(gen, list)  # not a list
