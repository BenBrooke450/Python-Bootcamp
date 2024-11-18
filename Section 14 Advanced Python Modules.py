
####################################################################
#                   Python Collections Module
####################################################################


from collections import Counter

from dask.array.random import choice

mylist = [1,1,1,1,2,2,3,3,4,5,5,6]

print(Counter(mylist))
#Counter({1: 4, 2: 2, 3: 2, 5: 2, 4: 1, 6: 1})


mylist2 = ["a","a","b",10,10,10]

print(Counter(mylist2))
Counter({10: 3, 'a': 2, 'b': 1})



sentence = "How many times does this word show up in this sentence"
print(Counter(sentence.lower().split()))
Counter({'this': 2, 'how': 1, 'many': 1, 'times': 1, 'does': 1, 'word': 1, 'show': 1, 'up': 1, 'in': 1, 'sentence': 1})



letters = "aaaaabbbbcccvvghdtfy"

c = Counter(letters)

print(c)
#Counter({'a': 5, 'b': 4, 'c': 3, 'v': 2, 'g': 1, 'h': 1, 'd': 1, 't': 1, 'f': 1, 'y': 1})


print(c.most_common())
#[('a', 5), ('b', 4), ('c', 3), ('v', 2), ('g', 1), ('h', 1), ('d', 1), ('t', 1), ('f', 1), ('y', 1)]


####################################################################


from collections import defaultdict

d = {"a":10}

print(d)
{'a': 10}


print(d["a"])
10






####################################################################


mytuple = (10,20,30)

print(mytuple[1])
20


from collections import namedtuple

Dog = namedtuple("Dog",["age","breed","name"])

sammy  = Dog(age = 5, breed = "BOB", name = "Sam")

print(sammy)
#Dog(age=5, breed='BOB', name='Sam')

print(sammy.age)
5










####################################################################
#                       Math and Random Module
####################################################################



import math

help(math)
"""DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

        The result is between 0 and pi.........."""


value = 4.35
print(math.floor(value))
4


print(math.ceil(value))
5


print(round(4.56777))
5


print(math.pi)
3.141592653589793


print(math.e)
2.718281828459045



print(math.log(math.e))
1.0


print(math.log(100,10))
2.0


####################################################################

import random

print(random.randint(1,100))
79
...


mylist = list(range(0,20))

print(random.choice(mylist))
2

random.shuffle(mylist)

print(mylist)
[17, 5, 2, 10, 14, 11, 19, 4, 13, 0, 16, 6, 8, 18, 3, 1, 12, 15, 9, 7]




####################################################################
#                       Python Regular Expressions
####################################################################










