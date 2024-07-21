# to get Temp in F
# Convert to K and C


f = float(input("Enter temp in F")) #"43.5" -> 43.5
f_to_c  = (f-32)*(5/9) 

print("Temp is converted from F to C "+str(f_to_c)+"\n")

f_to_k = f_to_c + 273.15
print("Temp is converted from F to K "+str(f_to_k))


#Formula F to C(°F − 32) × 5/9 = °C
#Formula F to K(32°F − 32) × 5/9 + 273.15 = 273.15K
