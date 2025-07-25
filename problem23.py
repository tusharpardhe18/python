# change the values inside a list which is contained in set S?

s = {8,7,12,"Harry",[1,2]}

# Because sets in Python can only contain hashable (immutable) elements. Lists are mutable, so they’re not hashable and can’t be added to a set.