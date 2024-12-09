def test_list_fun():
    my_list = [1, 2, 3]
    print("Початковий список:", my_list)

    # extend()
    my_list.extend([4, 5])
    print("extend([4, 5]):", my_list)

    # append()
    my_list.append(6)
    print("append(6):", my_list)

    # insert()
    my_list.insert(2, 99)
    print("insert(2, 99):", my_list)

    # remove()
    my_list.remove(99)
    print("remove(99):", my_list)

    # clear()
    my_list.clear()
    print("clear():", my_list)

    # sort()
    my_list = [5, 2, 4, 3, 1]
    my_list.sort()
    print("sort():", my_list)

    # reverse()
    my_list.reverse()
    print("reverse():", my_list)

    # copy()
    copy_list = my_list.copy()
    print("copy():", copy_list)

test_list_fun()
