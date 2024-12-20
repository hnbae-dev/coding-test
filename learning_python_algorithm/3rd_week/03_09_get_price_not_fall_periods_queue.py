from collections import deque

example_prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        price_not_fall_period = 0
        for current_price in queue:
            if current_price >= price:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        answer.append(price_not_fall_period)
    return answer


print(get_price_not_fall_periods(example_prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(example_prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ",
      get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ",
      get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))
