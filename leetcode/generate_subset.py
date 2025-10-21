from itertools import chain, combinations

def get_subsets(nums):
    return list(chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1)))

nums = {1, 2, 3}
subsets = get_subsets(nums)
for s in subsets:
    print(list(s))