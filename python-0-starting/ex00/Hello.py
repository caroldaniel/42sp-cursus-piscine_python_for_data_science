def modify_list(lst):
    """Modify ft_list using indexing."""
    lst[1] = "World!"
    return lst


def modify_tuple(tpl):
    """Modify ft_tuple using reconstruction (tuples are immutable)."""
    return (tpl[0], "Brazil!")


def modify_set(st):
    """Modify ft_set by removing and adding (sets are unordered)."""
    st.discard("tutu!")
    st.add("Sao Paulo!")
    return st


def modify_dict(dct):
    """Modify dictionary value by key assignment."""
    dct["Hello"] = "42SP!"
    return dct


# Make them available at the module level
ft_list = modify_list(["Hello", "tata!"])
ft_tuple = modify_tuple(("Hello", "toto!"))
ft_set = modify_set({"Hello", "tutu!"})
ft_dict = modify_dict({"Hello": "titi!"})


def main():
    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()
