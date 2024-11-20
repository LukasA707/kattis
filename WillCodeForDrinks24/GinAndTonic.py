from collections import defaultdict
# numberOfMembers = int(input)

# members = list()

# for _ in range(numberOfMembers):
#     line = input().split()
#     members.append(line)

# numberOfGins = int(input)

# for _ in range(numberOfGins):
    

n = int(input())

guests = defaultdict(list)

for _ in range(n):
    name, i, allergies = input().split(" ")
    i = int(i)
    for allergy in allergies:
        guests[name].append()
    