element = []

for n in range(6):
    ele = int(input("Enter name: "))
    element.append(ele)

for n in range(3):
    squ = element[n]
    result_1 = squ**2
    print("square " + result_1)

for n in range(3, 6):
    cube = element[n]
    result_2 = cube**3
    print("cube " + result_2)
