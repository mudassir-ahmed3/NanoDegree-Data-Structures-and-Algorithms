def sqrt(num):
    if num is None:
        return None

    if num == 0 or num == 1:
        return num

    elif num < 0:
        raise ValueError("Math Error, please enter positive number")

    else:
        return findsqrt_BS(1,num-1,num)
        # for x in range(1,num): // simple logic, time complexity O(n)
        #     if x*x <= num:
        #         continue
        #     return x-1

def findsqrt_BS(lower_bound, higher_bound, target):
    while lower_bound <= higher_bound:
        mid = (lower_bound + higher_bound)//2

        if mid*mid == target:
            return mid

        elif mid*mid > target:
            higher_bound = mid - 1

        else:
            lower_bound = mid + 1


    return higher_bound

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
#Additional test cases or edge cases
print ("Pass" if (1 == sqrt(1)) else "Fail")
print ("Pass" if (None == sqrt(None)) else "Fail") #test None
print ("Pass" if (100 == sqrt(10200)) else "Fail") #test big number
print(sqrt(-16)) # value error: Math Error, please enter positive number

