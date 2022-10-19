import itertools

class hortyHelper:
    world = ""
    scenario_dict = {}
    dict_subset = []
    output_matrix = []

    def set_dict(self, x):
        if type(x) is not dict:
            return print('Error: input must be a dictionary.')
        self.scenario_dict = x

    def make_subset(self):
        for i in range(len(list(self.scenario_dict)) + 1):
            for subset in itertools.combinations(list(self.scenario_dict), i):
                self.dict_subset.append(subset)

    def run_scenario(self, scenario):
        if len(self.dict_suubset) == 0:
            make_subset()

        def consistent_check():
            seen = set()
            conflict = 0
            for i in self.dict_subset[scenario]:
                if self.scenario_dict[i][0] is not '!' and '!' + self.scenario_dict[i] in seen:
                    conflict = 1
                elif self.scenario_dict[i][0] is '!' and self.scenario_dict[i][1] in seen:
                    conflict = 1
                seen.add(self.scenario_dict[i])
            if conflict is not 0:
                self.output_matrix[scenario].append('Not Consistent')
            else:
                self.output_matrix[scenario].append('Consistent')
            return seen

        def extension(seen):
            extensions = []
            extension_seen = set()
            for i in seen:
                if i in self.scenario_dict and self.scenario_dict[i] not in extension_seen:
                    extensions.append(self.scenario_dict[i])
                    extension_seen.add(self.scenario_dict[i])
            return extensions

        def conflict_check(extensions_seen):
            conflict = []
            for i in seen:
                if (i[0] is '!' and i[1] in extensions_seen) or (i[0] is not '!' and '!' + i[0] in extensions_seen):
                    conflict.append(i)
            if len(conflict) is 0:
                conflict.append('No Conflicts')
            return conflict

        def defeated_check():
            # TODO: Write this function.
            """
            This will need to be able to reference a priority list
            and be able to understand the dictionary in terms of indices
            """

        self.output_matrix.append([self.dict_subset[scenario]])

"simple tests"
tester = hortyHelper()
tester.set_dict({"socrates" : "man", "man" : "mortal"})
tester.make_subset()
