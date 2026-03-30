from itertools import permutations

L = ['A', 'B', 'C']
print(list(permutations(L, 2)))

from itertools import combinations
print(list(combinations(L, 2)))