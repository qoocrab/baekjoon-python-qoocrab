# Time Complexity: O(N)
# Space Complexity: O(N)
import sys

data = map(int, sys.stdin.read().split())

for a in data:
    b = next(data)
    
    if a == 0 and b == 0:
        break
    
    print(a + b)
