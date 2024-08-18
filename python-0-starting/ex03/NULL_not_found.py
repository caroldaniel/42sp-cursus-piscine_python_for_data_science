def NULL_not_found(object: any)-> int:
    # Check if the object is NoneType
    if object is None:
        print(f"Nothing : None {type(object)}")
    # Check if the object is NaN
    elif object != object:
        print(f"Cheese : NaN {type(object)}")
    # Check if the object is 0
    elif object == 0:
        print(f"Zero : {type(object)}")
    # Check if the object is an empty string
    elif object == '':
        print(f"Empty : {type(object)}")
    # Check if the object is False
    elif object == False:
        print(f"Fake : {type(object)}")
    # If the object is not any of the above
    else:
        print(f"Type not found")
        return 1

    return 0