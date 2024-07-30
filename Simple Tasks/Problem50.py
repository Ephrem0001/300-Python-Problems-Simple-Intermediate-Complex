height_triangle = int(input("Enter height of triangle: "))
base_triangle = int(input("Enter base of triangle: "))

area_of_triangle = (height_triangle * base_triangle)/2
h_squ = height_triangle**2
b_squ = base_triangle**2

sum_total = area_of_triangle + h_squ + b_squ

print(f"total sum of squear of inputs and area of triangle {sum_total}")
