import logging
import itertools

def default_calculator(world, scenario_dict, priority_dict):
    dict_subset = []
    output_matrix = []

    def make_subset():
        for i in range(len(list(scenario_dict)) + 1):
            for subset in itertools.combinations(list(scenario_dict), i):
                dict_subset.append(subset)

    def run_scenario(scenario):
        def trigger_world(world):
            if type(world) is dict:
                return list(world.values())
            return world

        def consistent_check(triggered_world):
            seen = set()
            for i in triggered_world:
                seen.add(i)
            conflict = 0
            for i in dict_subset[scenario]:
                if scenario_dict[i][0] is not '!' and '!' + scenario_dict[i] in seen:
                    conflict = 1
                elif scenario_dict[i][0] is '!' and scenario_dict[i][1] in seen:
                    conflict = 1
                seen.add(scenario_dict[i])
            output_matrix[scenario].append(seen)
            if conflict is not 0:
                output_matrix[scenario].append('Not Consistent')
            else:
                output_matrix[scenario].append('Consistent')
            return seen

        def extension(triggered_world, seen):
            extensions = triggered_world
            extension_seen = set()
            for i in seen:
                if i in scenario_dict and scenario_dict[i] not in extension_seen:
                    extensions.append(scenario_dict[i])
                    extension_seen.add(scenario_dict[i])
            return extensions

        def conflict_check(seen, extensions_seen):
            conflict = []
            for i in extensions_seen:
                if (i[0] is '!' and i[1] in seen) or (i[0] is not '!' and '!' + i[0] in seen):
                    conflict.append(i)
            if len(conflict) is 0:
                conflict.append('No Conflicts')
            return conflict

        def defeated_check(seen, extensions, priority):
            defeated = set()
            for i in seen:
                if i[0] is '!' and i[1] in extensions and i in priority:
                    defeated.add(i[1])
                elif i[0] is '!' and i[1] in extensions:
                    defeated.add(i)
                elif i[0] is not '!' and '!' + i in extensions and i in priority:
                    defeated.add('!' + i)
                elif i[0] is not '!' and '!' + i in extensions:
                    defeated.add(i)
            return defeated

        def binding_check(extensions, conflicts, defeated):
            for i in extensions:
                if i in conflicts or i in defeated:
                    extensions.remove(i)
            return extensions

        def proper_check(seen, binding):
            for i in seen:
                if i not in binding:
                    return 'Improper'
            return 'Proper'

        scenario_arr = []
        for i in dict_subset[scenario]:
            scenario_arr.append(scenario_dict[i])
        if scenario == 0:
            scenario_arr = 'none'
        output_matrix.append([])

        triggered_world = trigger_world(world)
        seen = consistent_check(triggered_world)
        extensions = extension(triggered_world, seen)
        conflicts = conflict_check(seen, extensions)
        defeated = defeated_check(seen, extensions, {"a" : "!a"})
        binding = binding_check(extensions, conflicts, defeated)

        output_matrix[scenario].append(extensions)
        output_matrix[scenario].append(conflicts)
        output_matrix[scenario].append(defeated)
        output_matrix[scenario].append(binding)
        output_matrix[scenario].append(proper_check(seen, binding))
        print(output_matrix[scenario])

    make_subset()
    for i in range(len(dict_subset)):
        run_scenario(i)
    return output_matrix

"simple test"
default_calculator({0 : 'p', 1 : 'b'}, {'b': 'f', 'p' : '!f'}, {'!f' : 'f'})
