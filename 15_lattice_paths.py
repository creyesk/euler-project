from math import comb


def n_paths(dim):
    # From the total steps we just need to decide which half goes down
    # the right steps will be automatically determined
    return comb(2 * dim, dim)


print(n_paths(20))
