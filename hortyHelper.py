import itertools

class hortyHelper:
    world = ""
    scenario_dict = {}
    dict_subset = []
    scenario_index = {}
    output_matrix = []

    def set_dict(self, x):
        if type(x) is not dict:
            return print('Error: input must be a dictionary.')
        self.scenario_dict = x

    def make_subset(self):
        for i in range(len(list(self.scenario_dict)) + 1):
            for subset in itertools.combinations(list(self.scenario_dict), i):
                self.dict_subset.append(subset)

    def scenario_index(self):
        working_dict = {}
        for i, l in enumerate(list(self.scenario_dict)):
            val = self.scenario_dict[l]
            print(val)
            key = i
            print(key)
            working_dict[val] = key
        print(working_dict)
        self.scenario_index = working_dict
        print(self.scenario_index)

"simple tests"
tester = hortyHelper()
tester.set_dict({"socrates" : "man", "man" : "mortal"})
tester.make_subset()
tester.scenario_index()
