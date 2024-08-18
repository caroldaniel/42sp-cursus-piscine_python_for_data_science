def all_thing_is_obj(object: any)-> int:
    obj_type = type(object)
    if obj_type:
        class_name = str(obj_type).split("'")[1]
        # print(f"{class_name.capitalize()} : {obj_type}")

    if isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    elif isinstance(object, list) or isinstance(object, tuple) or isinstance(object, set) or isinstance(object, dict):
        print(f"{class_name.capitalize()} : {obj_type}")
    else:
        print("Type not found")
    
    return 42
