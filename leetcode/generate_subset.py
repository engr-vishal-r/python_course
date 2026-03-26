from itertools import chain, combinations

def get_subsets(nums):
    return list(chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1)))

nums = {'a', 'c', 'b', 'd'}
subsets = get_subsets(nums)
for s in subsets:
    print(list(s))