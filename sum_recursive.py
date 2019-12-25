"""
    Divide-and-conquer Algorithm(分治法)
    1.Base case(基线条件).
    2.Reduce the size, to make it close to the base case.
"""


def sum_list(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return num_list[0] + sum(num_list[1:])


print(sum_list([1, 3, 5, 6]))


def quicksort(num_list):
    if len(num_list) < 2:
        return num_list
    else:
        pilot = num_list[0]
        left = []
        right = []
        for num in num_list[1:]:
            if num <= pilot:
                left.append(num)
            else:
                right.append(num)
        return quicksort(left) + [pilot] + quicksort(right)


print(quicksort([1, 3, 1, 7, 4, 5, 9, 0]))
