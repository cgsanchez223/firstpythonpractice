def sum_nums(nums):
    """Given list of numbers, return sum of those numbers"""

    addition = 0

    for num in nums:
        addition = addition + num

    return addition

print(sum_nums([1, 2, 3, 4])) # 10