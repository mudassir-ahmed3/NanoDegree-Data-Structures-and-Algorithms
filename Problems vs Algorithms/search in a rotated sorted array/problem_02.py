def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None:
        return None

    if len(input_list) <= 0 or number is None:
        return -1


    lower_bound = 0
    upper_bound = len(input_list) - 1
    smallestindex = smallest_element_index(input_list)

    if input_list[smallestindex]<= number <= input_list[upper_bound]:
        return binary_search_recursive(input_list,number,smallestindex,upper_bound)
    else:
        return binary_search_recursive(input_list,number,lower_bound,smallestindex-1)

def smallest_element_index(input_list):#print(smallest_element_index([9,10,11,12,1,2,3,4,5,6,7,8]))
    lower_bound = 0
    higher_bound = len(input_list)-1

    while lower_bound < higher_bound:
        mid = (lower_bound + higher_bound)// 2
        if input_list[mid] > input_list[higher_bound]:
            lower_bound = mid + 1
        else:
            higher_bound = mid

    return lower_bound

def binary_search_recursive(arr,target,left_index, right_index):
    if left_index > right_index:
        return -1
    mid = (left_index + right_index)//2
    if arr[mid] == target:
        # print("binarysearch index:"+str(mid))
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr,target,mid+1,right_index)
    else:
        return binary_search_recursive(arr,target,left_index,mid-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            # print("linear search:"+str(index))
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# print("Additional test cases")
print('Pass' if rotated_array_search([], 2) == -1 else 'Fail')
print('Pass' if rotated_array_search([], None) == -1 else 'Fail')
print('Pass' if rotated_array_search(None, None) is None else 'Fail')  # result None
print('Pass' if rotated_array_search(None, 9) is None else 'Fail')  # result None

#edge test  empty string
test_function([[], 1])
#edge test  large list
test_list=[i for i in range (3000,10000)]+[i for i in range (0,3000)]
# print(test_list)
test_function([test_list, 6])
# egde test  large list with negative numbers
test_list=[i for i in range (1000,10000)]+[i for i in range (-900,1000)]
# print(test_list)
test_function([test_list, -60])





# print(smallest_element_index([9,10,11,12,1,2,3,4,5,6,7,8]))



































