def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None:
        return None
    if len(input_list) == 0:
        return input_list

    next_idx_0 = 0
    next_idx_2 = len(input_list) - 1

    front_index = 0

    while front_index <= next_idx_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_idx_0]
            input_list[next_idx_0] = 0
            next_idx_0 += 1
            front_index += 1

        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_idx_2]
            input_list[next_idx_2] = 2
            next_idx_2 -= 1

        else:
            front_index += 1


def test_function(test_case):
    sort_012(test_case)
    # print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0])  # given input list is all 0's means already sorted
test_function([1, 1, 1, 1, 1, 1])  # all 1's already sorted
test_function([2, 2, 2, 2, 2, 2, 2])  # all 2's already sorted
print(sort_012([]))  # result : []
print(sort_012(None))  # result : None

