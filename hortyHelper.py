import itertools

class hortyHelper:
    world = ""
    dict = {}
    dict_subset = []
    output_matrix = []

    def make_subset():
        for i in range(len(list(dict)) + 1):
            for subset in itertools.combinations(list(dict), i):
                dict_subset.append(subset)
