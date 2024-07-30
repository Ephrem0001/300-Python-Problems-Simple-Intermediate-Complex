num = int(input("enter a number to get factorial: "))
factoriall = 1
for i in range(1,num+1):
    factoriall = i * factoriall
print(f"factorial {factoriall}")
