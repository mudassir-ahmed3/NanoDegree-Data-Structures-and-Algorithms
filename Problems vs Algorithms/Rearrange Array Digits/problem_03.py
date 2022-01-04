def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        return []
    size = len(input_list)
    if size <= 0:
        return []
    num1 = []
    num2 = []
    quick_sort(input_list)
    for i in range(size-1,-1,-2):
        num1.append(input_list[i])

    for i in range(size-2,-1,-2):
        num2.append(input_list[i])


    #convert the sub arrays into number
    num1 = sum(digit*10**index for index,digit in enumerate(num1[::-1]))
    num2 = sum(digit * 10**index for index,digit in enumerate(num2[::-1]))

    return [num1, num2]


def quick_sort(input_list):
    sort_all(input_list,0,len(input_list)-1)

def sort_all(items,begin_index, end_index):
    if end_index <= begin_index: #base case would achive when list would have o or 1 item, means it's already sorted simply return
        return

    pivot_index = sort_a_little_bit(items,begin_index,end_index)
    #recursively call sortall for both parts of list one before pivot and another after pivot
    sort_all(items, begin_index, pivot_index-1)
    sort_all(items, pivot_index+1, end_index)

def sort_a_little_bit(items,begin_index,end_index):
    #work on part of list define by begin index and end index, sorts item as per pivot value chosen and return final pivot_index
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while pivot_index != left_index:
        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index-1]
        items[pivot_index-1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1



    return pivot_index



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [532, 41]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], []])
test_function([None, []])
test_function([[1], [1]])
test_function([[1,2], [1,2]])
test_function([[1,2,3], [31,2]])
test_function([[3,1,3,3], [31,33]])
