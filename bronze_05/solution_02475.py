# Time Complexity: O(1)
# Space Complexity: O(1)
nums = map(int, input().split())
print(sum(n**2 for n in nums) % 10)
