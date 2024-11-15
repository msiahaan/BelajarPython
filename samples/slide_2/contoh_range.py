rangeku = range(5)
rangeku_list = list(rangeku)
blackpink_members= ["Jisoo", "Jennie", "Rose", "Lisa"]
odd_numbers = [1, 3, 5, 7, 9, 11]
blackpink_odd = [
     ["Jisoo", "Jennie", "Rose", "Lisa"],
     [1, 3, 5, 7, 9, 11]
]

print(rangeku)
print(rangeku_list)
print("=" * 10)
for i in rangeku_list:
    print(i)
print("=" * 10)
for blackpink in blackpink_members:
    print(blackpink)
print("=" * 10)
for the_list in blackpink_odd:
    for the_member in the_list:
        print(the_member)
