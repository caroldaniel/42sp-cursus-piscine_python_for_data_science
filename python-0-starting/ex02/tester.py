from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"} 

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

# all_thing_is_obj(10.5)
# all_thing_is_obj(3+4j)
# all_thing_is_obj(True)
# all_thing_is_obj(range(10))
# all_thing_is_obj(b"Hello")
# all_thing_is_obj(bytearray(5))
# all_thing_is_obj(memoryview(bytes(5)))
# all_thing_is_obj(None)
# all_thing_is_obj(lambda x: x+1)
