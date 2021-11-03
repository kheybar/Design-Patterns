"""

    Shallow Copy vs Deep Copy
        only for mutable objects(list, dict, set)

"""



# --- Pointer (Shallow Copy)
a= [1, 2, 3, 4, 5]
b = a

print(id(a)) # 140191642993088
print(id(b)) # 140191642993088

# change Shallow copy(b) == change main object(a)
b[0] = 0 # [0, 2, 3, 4, 5]
print(a) # [0, 2, 3, 4, 5]

# ---

print('-------------')

# --- Use ( list(), dict(), set() ) to make a copy of object

c = ['M', 'R', 'A']
d = list(c)

print(id(c)) # 140703803328320
print(id(d)) # 140703803329024

d[0] = 'H'
print(c) # ['M', 'R', 'A']
print(d) # ['H', 'R', 'A']

# this method have problem in nested!
print('---method problem---')

e = [1, 2, 3, [4, 5]]
f = list(e)

print(id(e)) # 140106903992192
print(id(f)) # 140106903992832

f[3][0] = 44
print(e) # [1, 2, 3, [44, 5]]
print(f) # [1, 2, 3, [44, 5]]
# ---

print('-------------')

# --- Use module Copy

from copy import copy, deepcopy

g = [1, 2, 3, [44, 5]]
h = deepcopy(g) # deep copy

print(id(g)) # 139826905668288
print(id(h)) # 139826905665792

h[3][0] = 4
print(g) # [1, 2, 3, [44, 5]]
print(h) # [1, 2, 3, [4, 5]]

# ---