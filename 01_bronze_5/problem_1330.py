# Time Complexity: O(1)
# Space Complexity: O(1)
a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
