# Time Complexity: O(N)
# Space Complexity: O(N)
import sys

data = sys.stdin.read().split()
numbers = data[1:-1]
v = data[-1]

print(numbers.count(v))
