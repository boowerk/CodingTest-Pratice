from itertools import permutations

# 순열은 순서를 고려해서 원소를 뽑는다.
L = ['A', 'B', 'C']
print(list(permutations(L, 2)))

from itertools import combinations
# 조합은 순서를 무시하고 원소를 뽑는다.
print(list(combinations(L, 2)))
