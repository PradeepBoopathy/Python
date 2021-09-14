#Iterative Approach
def Binarysearch_iterative(elements, number_to_find):
    left_index = 0
    right_index = len(elements)-1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = elements[mid_index]
        if mid_number == number_to_find:
            return mid_index
        elif mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1
#Recursive Approach
def Binarysearch_recursive(elements,number_to_find,left_index,right_index):
    if right_index < left_index:
        return -1
    mid_index = (left_index + right_index) // 2
    mid_number = elements[mid_index]
    if mid_number == number_to_find:
        return mid_index
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return Binarysearch_recursive(elements, number_to_find, left_index, right_index)

if __name__ == '__main__':
    elements = [5, 10, 15, 20, 21, 22, 23, 25, 34, 36, 38, 40]
    search = 38
    iterative = Binarysearch_iterative(elements, search)
    print(f"Number found at index {iterative} using binary search iterative")
    recursive = Binarysearch_recursive(elements, search, 0, len(elements))
    print(f"Number found at index {recursive} using binary search recursive")