def find_not_repeating_first_character(string):
    char_array = [0] * 26
    
    for char in string:
        arr_index = ord(char) - ord("a")
        char_array[arr_index] += 1
        
    for char in string:
        arr_index = ord(char) - ord("a")
        count = char_array[arr_index]
        if count == 1:
            return char
    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))