one_four = {1, 2, 3, 4}
three_six = {3, 4, 5, 6}
one_ten = set(range(1, 11))
evens = {2, 4, 6, 8}
odds = {1, 3, 5, 7}

# Shorthand for a union of sets
print(one_four.union(three_six))
print(one_four | three_six)  # Shorthand for union

# Check if a set is fully contained within another
print(one_ten.issuperset(three_six))
print(three_six.issubset(one_ten))

# Get a new set of shared (or not) values in sets
print(evens.intersection(one_four))
print(evens & one_four)
print(evens.difference(one_four))  # Shorthand for intersection

# Get a new set only containing the elements NOT in either
print(one_four.symmetric_difference(three_six))

# Check if sets are completely unique to each other
print(evens.isdisjoint(odds))


