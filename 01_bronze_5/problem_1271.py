# Time Complexity: O(max(log10n,log10m))
# Space Complexity: O(max(log10n,log10m))
n, m = map(int, input().split())

print(n // m)
print(n % m)
