input = [6, 9, 2, 7, 1888]

def find_max_num(array):
    max_num = array[0]
    index = 0
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
            index = i
    return [max_num, index]

result = find_max_num(input)

print(result[0])
print(result[1])
