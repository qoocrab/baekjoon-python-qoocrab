# Time Complexity: O(L^2), where L is the number of digits in n.
# Space Complexity: O(L)
n, m = map(int, input().split())
print(n // m)
print(n % m)
