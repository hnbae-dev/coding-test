array = [5, 3, 2, 1, 6, 8, 7, 4]

# MergeSort(0, N) = Merge(MergeSort(0, N/2) + MergeSort(N/2, N))

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    return merge(left_array, right_array)


def merge(array1, array2):
    point_1 = 0
    point_2 = 0
    result = []
    
    while point_1 < len(array1) and point_2 < len(array2):
        if array1[point_1] < array2[point_2]:
            result.append(array1[point_1])
            point_1 += 1
        else:
            result.append(array2[point_2])
            point_2 += 1
    
    if point_1 < len(array1):
        while point_1 < len(array1):
            result.append(array1[point_1])
            point_1 += 1
    if point_2 < len(array2):
        while point_2 < len(array2):
            result.append(array2[point_2])
            point_2 += 1
    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

# print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
# print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
# print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))
