
from Hello import ft_list, ft_tuple, ft_set, ft_dict


def test_list():
    assert ft_list == ["Hello", "World!"], \
        "ft_list should be ['Hello', 'World!']"


def test_tuple():
    assert ft_tuple == ("Hello", "Brazil!"), \
        "ft_tuple should be ('Hello', 'Brazil!')"


def test_set():
    assert ft_set == {"Hello", "Sao Paulo!"}, \
        "ft_set should be {'Hello', 'Sao Paulo!'}"


def test_dict():
    assert ft_dict == {"Hello": "42SP!"}, \
        "ft_dict should be {'Hello': '42SP!'}"
