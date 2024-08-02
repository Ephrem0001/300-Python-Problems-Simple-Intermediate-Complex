larg = int(input("enter the large number: "))
s = int(input("enter the small number: "))
arr = []
for i in range(larg, s, -1):
    arr.append(i)
    print(i)
summ = 0
for i in range(len(arr)):

    summ += i
print(f"sum = {summ}")
