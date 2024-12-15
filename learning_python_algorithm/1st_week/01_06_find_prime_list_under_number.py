input = 20

# 소수는 자기 자신과 1 외에는 아무 것도 나눌 수 없다.
def find_prime_list_under_number(number):
    prime_list = []
    
    # 2~20 중에서 소수라면 prime_list에 추가
    for n in range(2, number + 1): # 2 ~ number
        for i in prime_list:
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)
    
    return prime_list

result = find_prime_list_under_number(input)
print(result)