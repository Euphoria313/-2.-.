my_list = [3, None, -56, 'True', True, 4.2]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)