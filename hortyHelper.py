import itertools

class hortyHelper:
    world = ""
    scenario_dict = {}
    dict_subset = []
    output_matrix = []

    def set_dict(x):
        if type(x) is not dict:
            return print('Error: input must be a dictionary.')
        scenario_dict = x

    def make_subset():
        for i in range(len(list(dict)) + 1):
            for subset in itertools.combinations(list(dict), i):
                dict_subset.append(subset)
        print(dict_subset)

"simple tests"
def tester = hortyHelper()
tester.set_dict({"socrates" : "man", "man" : "mortal"})
tester.make_subset()
