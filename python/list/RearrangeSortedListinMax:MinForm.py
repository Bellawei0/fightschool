# Problem Statement
# Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, the 1st index will have the smallest, and the third index will have second-largest, and so on. In other words, all the odd-numbered indices will have the largest numbers in the list in descending order and the even-numbered indices will have the smallest numbers in ascending order.

# Input: A sorted list

# Output: # A list with elements stored in max/min form

# Sample Input
# lst = [1,2,3,4,5]
# Sample Output
# lst = [5,1,4,2,3]

# Solution #1: Creating a new list #
def max_min(lst):
    result = []

    for i in range(len(lst)//2):
        result.append(lst[-(i+1)])
        result.append(lst[i])
    if len(lst) % 2 == 1:
        result.append(lst[len(lst) // 2])
    return result


print(max_min([1, 2, 3, 4, 5, 6]))

# Solution #2: Using O(1)O(1) Extra Space
# Note: This approach only works for non-negative numbers!


def max_min(lst):
    # Return empty list for empty list
    if (len(lst) is 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst


print(max_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
