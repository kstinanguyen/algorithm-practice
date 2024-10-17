# Add your clarifying questions here

def skyline(building_list):
    set_list = set(building_list)
    new_list = []
    initial_num = 0

    for num in list(set_list):
        if num > initial_num:
            new_list.append(num)
            initial_num = num
    return new_list


assert skyline([-1, 1, 3, 7, 7, 3]) == [1, 3, 7]
assert skyline([1, 10, 3, 5]) == [1, 10]