def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE 
    return nums.__contains__(7)


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
