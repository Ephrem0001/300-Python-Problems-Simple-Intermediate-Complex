Subject_1 = int(input("Enter the 1 subject Mark: "))
Subject_2 = int(input("Enter the 2 subject Mark: "))
Subject_3 = int(input("Enter the 3 subject Mark: "))
Subject_4 = int(input("Enter the 4 subject Mark: "))
Subject_5 = int(input("Enter the 5 subject Mark: "))
Subject_6 = int(input("Enter the 6 subject Mark: "))

Total = Subject_1 + Subject_2 + Subject_3 + Subject_4 + Subject_5 + Subject_6
Average = Total/6
Percentage = Average
print("Total of 6 subject =" + str(Total))
print("Average of 6 subject =" + str(Average))
print("Percentage of 6 subject =" + str((Percentage*100)/600) + "%")
