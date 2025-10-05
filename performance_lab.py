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
print("Input:", [1, 3, 2, 3, 4, 1, 3])
print("Expected Output: 3")
print("Actual Output:", most_frequent([1, 3, 2, 3, 4, 1, 3]))
print()

print("Input:", [4, 4, 5, 5])
print("Expected Output: 4 or 5 (tie)")
print("Actual Output:", most_frequent([4, 4, 5, 5]))
print()

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
nums = [4, 5, 4, 6, 5, 7]
print("Input:", nums)
print("Expected Output: [4, 5, 6, 7]")
print("Actual Output:", remove_duplicates(nums))
print()

nums = [1, 1, 1]
print("Input:", nums)
print("Expected Output: [1]")
print("Actual Output:", remove_duplicates(nums))
print()

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
nums = [1, 2, 3, 4]
target = 5
print("Input:", nums, "Target:", target)
print("Expected Output: [(1, 4), (2, 3)]")
print("Actual Output:", find_pairs(nums, target))
print()

nums = [2, 4, 6, 8]
target = 10
print("Input:", nums, "Target:", target)
print("Expected Output: [(2, 8), (4, 6)]")
print("Actual Output:", find_pairs(nums, target))
print()

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
print("Adding 10 items...")
add_n_items(10)
print("-" * 50, "\n")


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
nums = [1, 2, 3, 4]
print("Input:", nums)
print("Expected Output: [1, 3, 6, 10]")
print("Actual Output:", running_total(nums))
print()

nums = [5, -2, 7]
print("Input:", nums)
print("Expected Output: [5, 3, 10]")
print("Actual Output:", running_total(nums))
print()

"""
Time and Space Analysis for problem 5:
- Best-case:0(n)
- Worst-case:0(n)
- Average-case:0(n)
- Space complexity:0(n)
- Why this approach? Because it is simple and efficient, just adding numbers as we go.
- Could it be optimized?  Not really, it is already a straightforward one-pass solution.
"""

#Refactoring Problem 3
def find_pairs_optimized(nums, target):
    nums.sort()  # Sorting enables two-pointer technique
    left, right = 0, len(nums) - 1
    pairs = []

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            pairs.append((nums[left], nums[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs

#Refactored Version:
#-Uses two-pointer technique on a sorted list.
#-Avoids using extra memory like a set.
#-Returns pairs in sorted order automatically.

#Optimization:
#-Improved space usage from O(n) ➜ O(1)
#-Predictable output order (no randomness from set)
#-Slightly higher time cost for sorting (O(n log n)) vs O(n)

#Testing the Refactored Function
print("Refactored Problem 3:")

nums = [1, 2, 3, 4]
target = 5
print("Input:", nums, "Target:", target)
print("Expected Output: [(1, 4), (2, 3)]")
print("Actual Output:", find_pairs_optimized(nums, target))
print()

nums = [2, 4, 6, 8]
target = 10
print("Input:", nums, "Target:", target)
print("Expected Output: [(2, 8), (4, 6)]")
print("Actual Output:", find_pairs_optimized(nums, target))
print()
