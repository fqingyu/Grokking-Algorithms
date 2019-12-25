import math


def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = math.floor((high+low)/2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = high - 1
    return None


print(binary_search([1, 3, 5, 6, 7, 9], -1))
