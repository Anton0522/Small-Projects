# the array in which we are searching
array = [1, 2, 3, 4, 5, 10, 20, 30]

# number to find x
x = 20
start_side = 0
end_side = len(array) - 1


def binary_search(array, x, start_side, end_side):
    middle = (start_side + end_side) // 2
    if end_side >= start_side:
        if array[middle] == x:
            return middle

        elif array[middle] < x:
            start_side = middle + 1

            return binary_search(array, x, start_side, end_side)
        elif array[middle] > x:
            end_side = middle - 1

            return binary_search(array, x, start_side, end_side)
    else:
        return -1


result = binary_search(array, x, start_side, end_side)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

# Every time we check if the number is lower or higher than x then we ignore the side which x is not present either
# the left or right side and repeat until x is found
