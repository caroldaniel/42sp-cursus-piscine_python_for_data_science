def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!") 
    ft_set = {"Hello", "tutu!"} 
    ft_dict = {"Hello" : "titi!"}

    replacements = ["World!", "Brazil!", "Sao Paulo!", "42SP!"]

    # Replace the second element of the list
    # ft_list: List - A mutable, ordered sequence of elements.
    # Lists allow duplicate elements and can be modified (add, remove, change items).
    ft_list[1] = replacements[0]

    # Replace the second element of the tuple using concatenation
    # ft_tuple: Tuple - An immutable, ordered sequence of elements.
    # Once a tuple is created, it cannot be modified (elements cannot be added, removed, or changed).
    ft_tuple = ft_tuple[:1] + (replacements[1],)

    # Replace the second element of the set using update
    # ft_set: Set - An unordered collection of unique elements.
    # Sets do not allow duplicate elements and are mutable (you can add or remove items).
    # The order of elements in a set is not guaranteed.
    ft_set = ft_set.difference({"tutu!"})
    ft_set.update({replacements[2]})
    ft_set = sorted(ft_set)

    # Replace the value of the key "Hello" in the dictionary
    # ft_dict: Dictionary - A mutable collection of key-value pairs.
    # Dictionaries are unordered (prior to Python 3.7) and do not allow duplicate keys.
    # Each key is unique, and it maps to a specific value.
    ft_dict["Hello"] = replacements[3]    

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()