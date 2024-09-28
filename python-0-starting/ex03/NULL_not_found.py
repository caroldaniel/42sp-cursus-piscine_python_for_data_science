def NULL_not_found(object: any) -> int:
    # Check if the object is NoneType
    # In Python, the `None` object is a singleton used to represent the absence of a value.
    # The `is None` check is the most efficient way to check for this case.
    if object is None:
        print(f"Nothing : None {type(object)}")

    # Check if the object is NaN (Not a Number)
    # In Python, NaN (Not a Number) is a special floating-point value defined in IEEE 754 standard.
    # A unique property of NaN is that it is never equal to itself, i.e., `NaN != NaN` returns True.
    # So, `object != object` is a quick way to check for NaN in floating-point numbers.
    elif object != object:
        print(f"Cheese : NaN {type(object)}")

    # Check if the object is 0
    # Here, we check if the object is numerically equal to 0. This would work for both integers and floats.
    # `0` is considered a falsy value in Python, but this check explicitly looks for the number 0.
    elif object == 0:
        print(f"Zero : {type(object)}")

    # Check if the object is an empty string
    # An empty string `''` is another example of a falsy value in Python.
    # This condition checks explicitly if the object is an empty string (not any falsy value).
    elif object == '':
        print(f"Empty : {type(object)}")

    # Check if the object is False
    # Python treats `False` as a falsy value, and `False` is an instance of the `bool` type.
    # This condition checks if the object is the boolean `False` explicitly.
    elif object is False:
        print(f"Fake : {type(object)}")

    # If the object is not any of the above
    # If none of the above conditions were met, it means the object isn't None, NaN, 0, an empty string, or False.
    # This clause will catch all other cases, indicating the object's type was not one of the "special" types we're checking for.
    else:
        print("Type not found")
        return 1

    return 0
