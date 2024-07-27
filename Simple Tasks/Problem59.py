bio = input("Enter bio ")
collect = ["is", "are", "am"]

bio_list = bio.split(" ")
c = int(0)
for i in bio_list:
    if i in collect:
        c += 1
print(c)
