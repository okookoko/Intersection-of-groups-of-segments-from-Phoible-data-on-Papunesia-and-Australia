
desired_elements1 = input('Input the description of your first set of desired segments, separated by a comma ",":')
desired_elements2 = input('Input the description of your second set of desired segments, separated by a comma ",":')

elements1 = [x.strip() for x in desired_elements1.split(',')]
elements2 = [x.strip() for x in desired_elements2.split(',')]

elements_ids1 = [''] * len(elements1)
elements_ids2 = [''] * len(elements2)

elements_langs_pa_s1 = [set() for x in range(len(elements1))]
elements_langs_pa_s2 = [set() for x in range(len(elements2))]

elements_langs_p_s1 = [set() for x in range(len(elements1))]
elements_langs_p_s2 = [set() for x in range(len(elements2))]

elements_langs_a_s1 = [set() for x in range(len(elements1))]
elements_langs_a_s2 = [set() for x in range(len(elements2))]

# change human lang of the element into the id of the element
with open('parameters.csv', 'r', encoding='utf8') as p:
    for line in p:
        split_line = line.split(',')

        for i in range(len(elements1)):
            if split_line[2] == elements1[i]:
                elements_ids1[i] = split_line[0]

        for x in range(len(elements2)):
            if split_line[2] == elements2[x]:
                elements_ids2[x] = split_line[0]

# get a set of languages with the elements in them
with open('values_Papunesia_Australia.txt', 'r', encoding='utf8') as vpa:
    
    for line in vpa:

        split_line = line.split(',')

        for i in range(len(elements1)):
            if split_line[2] == elements_ids1[i]:
                elements_langs_pa_s1[i].add(split_line[1])

        for x in range(len(elements2)):
            if split_line[2] == elements_ids2[x]:
                elements_langs_pa_s2[x].add(split_line[1])

with open('values_Papunesia.txt', 'r', encoding='utf8') as vpa:
    for line in vpa:

        split_line = line.split(',')

        for i in range(len(elements1)):
            if split_line[2] == elements_ids1[i]:
                elements_langs_p_s1[i].add(split_line[1])

        for x in range(len(elements2)):
            if split_line[2] == elements_ids2[x]:
                elements_langs_p_s2[x].add(split_line[1])

with open('values_Australia.txt', 'r', encoding='utf8') as vpa:
    for line in vpa:

        split_line = line.split(',')

        for i in range(len(elements1)):
            if split_line[2] == elements_ids1[i]:
                elements_langs_a_s1[i].add(split_line[1])

        for x in range(len(elements2)):
            if split_line[2] == elements_ids2[x]:
                elements_langs_a_s2[x].add(split_line[1])

#create a set of mathing elements from more sets; intersection of multiple sets
def matching_elements(langs_sets):

    shared = langs_sets[0].intersection(langs_sets[1])
    for i in range(2, len(langs_sets)):
        shared = shared.intersection(langs_sets[i])

    return shared

print('Papunesia and Australia')
results1 = matching_elements(elements_langs_pa_s1)
results2 = matching_elements(elements_langs_pa_s2)
results = matching_elements([results1, results2])
print('results', len(results),  '\n', results)
print('results1', len(results1),  '\n', results1)
print('results2', len(results2),  '\n', results2)

print()

print('Papunesia')
results1 = matching_elements(elements_langs_p_s1)
results2 = matching_elements(elements_langs_p_s2)
results = matching_elements([results1, results2])
print('results', len(results),  '\n', results)
print('results1', len(results1),  '\n', results1)
print('results2', len(results2),  '\n', results2)

print()

print('Australia')
results1 = matching_elements(elements_langs_a_s1)
results2 = matching_elements(elements_langs_a_s2)
results = matching_elements([results1, results2])
print('results', len(results),  '\n', results)
print('results1', len(results1),  '\n', results1)
print('results2', len(results2), '\n', results2)
