# Time Complexity: O(1)
# Space Complexity: O(1)
numbers = list(map(int, input().split()))
verification_number = sum(n**2 for n in numbers) % 10

print(verification_number)
