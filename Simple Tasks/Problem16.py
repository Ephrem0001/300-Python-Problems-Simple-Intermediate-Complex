# To get a integer from the user
# perform compound assignment operators

num = int(input("Enter a integer: "))  # '4' -> 4
# num = 4
# addition assignment operator
summ = num + 5  # num + 5 -> 4 + 5 ->num
print(summ)  # 9

# Subtraction assignment operator
sub = num - 5  # num - 5 -> 4 - 5 ->num
print(sub)  # 4

# Multiplication assignment operator
mul = num * 5  # num * 5 -> 4 * 5 ->num
print(mul)  # 20

# Division assignment operator
div = num / 5  # num / 5 -> 20 / 5 ->num
print(div)  # 4

# Mod assignment operator
mod = num % 5  # num / 5 ->4 % 5 ->num
print(mod)  # ?

total = mod + mul + sub + summ + div
print("total sum of the operations: " + str(total))
