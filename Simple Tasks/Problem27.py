arr = []

for n in range(5):
    arr.append(int(input("Enter Year: ")))
for i in range(5):
    if arr[i] % 4 == 0:
        print(arr[i])
    else:
        print("no leap year")
