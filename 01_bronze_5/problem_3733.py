# The number of input number pairs is referred to as 𝑘
# Time Complexity: O(k)
# Space Complexity: O(k)
import sys

for line in sys.stdin:
    data = line.split()

    for i in range(0, len(data), 2):
        n = int(data[i])
        s = int(data[i + 1])
        x = s // (n + 1)

        print(x)
