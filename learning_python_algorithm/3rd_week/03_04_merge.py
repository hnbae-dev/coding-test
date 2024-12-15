array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


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


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))