def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return None,None

    min = ints[0]
    max = ints[0]

    for int in ints:
        if int < min:
            min = int

        if int > max:
            max = int

    return min,max



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((None, None) == get_min_max(None)) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((-341, -1) == get_min_max([-54,-2,-124,-341,-1, -341])) else "Fail")
print ("Pass" if ((-341, 2312) == get_min_max([-54,-2,-124,-341,-1, -341,2312,431,23])) else "Fail")