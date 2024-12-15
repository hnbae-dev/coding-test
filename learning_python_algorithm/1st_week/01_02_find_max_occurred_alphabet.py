def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    
    for char in string:
        if char.isalpha():
            alphabet_occurrence_array[ord(char) - ord('a')] += 1
    
    max_occurrence = 0
    max_occurred_alphabet = "a"
    
    for i in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[i] > max_occurrence:
            max_occurrence = alphabet_occurrence_array[i]
            max_occurred_alphabet = chr(ord("a") + i)
            
    return max_occurred_alphabet

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))