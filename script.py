# code wonderfully* provided by one of my great* friends
from itertools import product

n = {"m", "n"}
c = {"ẗ", "c", "z̈", "d̈"}
ua = {"p", "t", "k"}
sa = {"b", "d", "g"}
ub = {"l", "f", "x", "w", "j", "s", "s̈"}
sb = {"l", "v", "w", "j", "z"}
v = {"i", "ÿ", "ä", "a", "o", "u", "y"}

cons = {""} | n | c | ua | sa | ub | sb
cons1 = cons | set(j[0] + j[1] for i in (product(ua, ub), product(sa, sb)) for j in i)
cons2 = cons | set(j[1] + j[0] for i in (product(ua, ub), product(sa, sb)) for j in i)
syllables = set(''.join(i) for i in product(cons1, v, cons2))
with open("syllables.md", "w") as file:
  file.write(syllables)
