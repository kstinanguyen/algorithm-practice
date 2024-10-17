# Add your clarifying questions here

def rotate_list(list, shift_by):
    k = shift_by

    if len(list) < shift_by:
        raise ValueError(f"Number must be less than the length of the list: {len(list)}")

    return list[-k:] + list[:-k]



assert rotate_list([1, "c", 5], 4) == [1, "c", 5]

assert rotate_list([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]