

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True



numbers = []
for i in range(1, 11):
  num = int(input(f"Enter number {i}: "))
  numbers.append(num)

# Find prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

# Print prime numbers
print(f"Prime numbers: {prime_numbers}")
