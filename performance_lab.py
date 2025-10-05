# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get)


#Test Cases
print("Problem 1 Tests:")
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([7]) == 7

"""
Time and Space Analysis for problem 1:
- Best-case:0(n)
- Worst-case:0(n)
- Average-case:0(n)
- Space complexity:0(k) where k is the number of unique elements
- Why this approach? Because counting with a dictionary is simple and efficient.
- Could it be optimized? Not really, because this is optimal for single-pass frequency counting.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
   seen = set()
   result = []
   for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

#Test Cases
print("Problem 2 Tests:")
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([1, 1, 1]) == [1]

"""
Time and Space Analysis for problem 2:
- Best-case:0(n)
- Worst-case:0(n)
- Average-case:0(n)
- Space complexity:0(n)
- Why this approach? Because it is a clean and fast way to remove duplicates while keeping the same order.
- Could it be optimized? Not really, this is the most common and efficient way to do it.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

#Test Cases
print("Problem 3 Tests:")
res = find_pairs([1, 2, 3, 4], 5)
assert set(res) == {(1, 4), (2, 3)}  

"""
Time and Space Analysis for problem 3:
- Best-case:0(n)
- Worst-case:0(n)
- Average-case:0(n)
- Space complexity:0(n)
- Why this approach? Because it is quick and simple to check for complements instead of using two loops.
- Could it be optimized? Only if the list was sorted, then a two-pointer method could also work.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    items = []
    for i in range(1, n + 1):
        if len(items) == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            capacity *= 2
        items.append(i)
        print(f"Added {i}, size={len(items)}, capacity={capacity}")

#Test Case
print("Problem 4 Test:")
add_n_items(10)


"""
Time and Space Analysis for problem 4:
- When do resizes happen?  Every time the list reaches its current capacity.
- What is the worst-case for a single append? O(n) when resizing and copying to a new list.
- What is the amortized time per append overall? O(1), since resizing doesn’t happen often.
- Space complexity: 0(n)
- Why does doubling reduce the cost overall? Because it keeps the number of resizes small,
  spreading out the expensive copy steps over many cheap ones.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    current_sum = 0
    for num in nums:
        current_sum += num
        totals.append(current_sum)
    return totals

#Test Cases
print("Problem 5 Tests:")
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([5, -2, 7]) == [5, 3, 10]

"""
Time and Space Analysis for problem 5:
- Best-case:0(n)
- Worst-case:0(n)
- Average-case:0(n)
- Space complexity:0(n)
- Why this approach? Because it is simple and efficient, just adding numbers as we go.
- Could it be optimized?  Not really, it is already a straightforward one-pass solution.
"""
