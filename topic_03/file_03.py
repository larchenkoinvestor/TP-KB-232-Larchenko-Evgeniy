def test_dict_func():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Початковий словник:", my_dict)

    # update()
    my_dict.update({'d': 4, 'e': 5})
    print("update({'d': 4, 'e': 5}):", my_dict)

    # del()
    del my_dict['a']
    print("del 'a':", my_dict)

    # clear()
    temp_dict = my_dict.copy()
    temp_dict.clear()
    print("clear():", temp_dict)

    # keys()
    print("keys():", list(my_dict.keys()))

    # values()
    print("values():", list(my_dict.values()))

    # items()
    print("items():", list(my_dict.items()))

test_dict_func()
