finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    index_min = 0
    index_max = len(array) - 1
    
    while index_min <= index_max:
        index_find = (index_max + index_min) // 2
        if array[index_find] == target:
            return True
        elif array[index_find] > target:
            index_max = index_find - 1
        else:
            index_min = index_find + 1

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)