def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    for i in range(len(nums) - 2):
        if sum(nums[i:i+3]) % 2 != 0:
            return True
    return False

result1 = three_odd_numbers([1, 2, 3, 4, 5])
print(result1) # True

result2 = three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
print(result2) # True

result3 = three_odd_numbers([5, 2, 1])
print(result3) # False

result4 = three_odd_numbers([1, 2, 3, 3, 2])
print(result4) # False

