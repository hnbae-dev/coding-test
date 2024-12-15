shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "사이다", "떡"]


def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        is_exist = binary_search(menus, order)
        if is_exist is False:
            return False
    return True

def binary_search(array, target):
    l = 0
    r = len(array) - 1
    while l <= r:
        i = (l + r) // 2
        if array[i] == target:
            return True
        elif array[i] > target:
            r = i - 1
        else:
            l = i + 1
    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)

