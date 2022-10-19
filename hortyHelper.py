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

    def scenario_index():
        for i, l in list(self.scenario_dict):
            self.dict_index[l] = i
        print(self.dict_index)

"simple tests"
tester = hortyHelper()
tester.set_dict({"socrates" : "man", "man" : "mortal"})
tester.make_subset()
tester.dict_index()
