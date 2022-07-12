# The Set Data Structure
The `Set` Data Structure can be used to find commonality between different groups of data.

For example, if I had two groups of people and I wanted to find out if there was redheads in both groups, I could use a `set` and it would output 'red' if there was any in both groups. The code to do that would look like this:
```Python
def intersection(group1, group2):
    redgroup = set()
    for r in group1:
        for r2 in group2:
            if r == r2:
                redgroup.add(r)
    return redgroup

group1 = {'red', 'black', 'brown', 'blonde', 'auburn', 'red'}
group2 = {'brunette', 'violet', 'green', 'darkred', 'red'}
print(intersection(group1, group2))
```

# Your Task
Using the groups above, write a function that will use a set to count how many redheads there are in both group

[Set Task](https://github.com/NicholasBoss/DataStructureTutorial/blob/master/settask.py)

[Set Solution](https://github.com/NicholasBoss/DataStructureTutorial/blob/master/setsolution.py)

# Back to Home

[Return to Home](https://github.com/NicholasBoss/DataStructureTutorial/blob/master/0-welcome.md)