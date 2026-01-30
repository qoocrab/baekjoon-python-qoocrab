# Time Complexity: O(N)
# Space Complexity: O(N)
import sys

data = sys.stdin.read().split()

x = int(data[1])
numbers = data[2:]

result = [n for n in numbers if int(n) < x]
print(*(result))
