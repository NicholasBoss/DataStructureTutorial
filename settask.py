def intersection(group1, group2):
    redgroup = set()
    for r in group1:
        for r2 in group2:
            if r == r2:
                redgroup.add(r)
    return redgroup



# Using the groups already given, write a function that will use a set to count how many redheads there are in the group
# and return the number.
def count_redheads(group):
    pass

group1 = {'red', 'black', 'brown', 'blonde', 'auburn'}
group2 = {'brunette', 'violet', 'green', 'darkred', 'red'}
print("Test case 1:")
print("------------")
print(intersection(group1, group2))
print("------------")
print("Test case 2:")
print("------------")
print(f"Total redheads in group 1:  {count_redheads(group1)}")
print(f"Total redheads in group 2: {count_redheads(group2)}")
total = count_redheads(group1) + count_redheads(group2)
print(f"Total in both groups: {total}")
print("------------")