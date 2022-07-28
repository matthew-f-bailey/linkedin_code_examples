from sys import getsizeof
from timeit import timeit

"""
List comprehension will allocate the entire list in memory upon creation
Generator comprehensions will create items on the fly as you iterate

Both have upsides in some situations, but heres a decent way to think about it:

If you need to iterate multiple times or apply common list methods over the
iterable you are creating, then list comprehensions are they way to go.

However generator comprehensions will be much more memory and speed efficient
and can hypothetically handle infinite iteration. So if you are simply grabbing
elements one at a time from a massive list and thats your intention, consider
using generator comprehensions instead.
(This is true for general generators v. lists as well)
"""

num = 100_000

# List comprehension
l_comp = [i for i in range(num)]
print(
    f"List comprehension size: {getsizeof(l_comp)}"
) # size => 824456
print(
    timeit(f"[i for i in range({num})]", number=3_000)
)  # time => 12.11917 seconds

# Generator comprehension
g_comp = (i for i in range(num))
print(
    f"Generator comprehension size: {getsizeof(g_comp)}"
) # size => 112
print(
    timeit(f"(i for i in range({num}))", number=3_000)
)  # time => 0.00153 seconds


