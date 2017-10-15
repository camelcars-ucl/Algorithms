def total_sum(a,b):
    '''
    Given the two coordinates, finds the non-diagonal distance between them
    e.g. (9,8),(5,6) would yield 6
    '''
    the_sum = abs(a[0]-b[0])+abs(a[1]-b[1])
    return the_sum

def dif_components(node_1,another_node,array_of_nodes):
    '''
    The objective is to see whether 2 given nodes in the parameter are of different components. The term 'components' is
    difficult to explain, an example would be more ept.
    given array_of_nodes = [{0,4},{2,3},{1}]
    if node_1 were associated with 0 and another_node associated with 2, they are of different components
    :return: the first value shows whether they are of the same components or not, the second returns the new
    array_of_nodes
    '''
    counter = 0
    while counter < len(array_of_nodes):
        #assert (node_1 in array_of_nodes[counter] and another_node not in array_of_nodes[counter])
        if node_1 in array_of_nodes[counter] and another_node not in array_of_nodes[counter]:

            index = 0
            while True:
                if another_node in array_of_nodes[index]:
                    break
                else:
                    index = index + 1
            array_of_nodes[counter] |= array_of_nodes[index]
            array_of_nodes.pop(index)
            statement = True
            break
        if node_1 in array_of_nodes[counter] and another_node in array_of_nodes[counter]:
            statement = False
            break
        counter = counter + 1
    return statement, array_of_nodes

def the_smallest_value(initial_key,dict_of_all_lengths):
    '''
    The objective is to find the smallest value in all of the arrays
    :return: returns the key associated with the smallest value amongst all the arrays
    '''
    key_now = initial_key
    smallest = dict_of_all_lengths[initial_key][0]
    for keys , values in dict_of_all_lengths.items():
        tempo = values[0]
        if tempo < smallest:
            smallest = tempo
            key_now = keys
    return key_now,smallest

def gridland(*args):
    '''

    :param args:
    :var nodes:  Gives me a dict of coordinates associated with numbers e.g. {(3,8):0}
    :return:
    '''
    final_length = 0
    array = [(args[i],args[i+1]) for i in range(0,len(args)-1,2)]
    nodes = {}
    for i in range(len(array)):
        nodes[array[i]] = i
    array_of_nodes = [{i} for i in range(len(array))]
    dict_of_all_lengths = {}
    new_sum = []        #This contains all the possible arcs from one node to the others
    min_array = []      #min_array contains all of the smallest_arcs
    i = 0
    for i in range(len(array)):
        for x in range(len(array)):
            if x != i:
                new_sum.append(total_sum(array[i],array[x]))
        dict_of_all_lengths[array[i]] = sorted(new_sum)
        new_sum = []
    while len(array_of_nodes) != 1:
        to_be_considered = the_smallest_value(array[0],dict_of_all_lengths)
        for i in range(len(array)):
            if array[i] != to_be_considered[0]:
                if total_sum(to_be_considered[0],array[i]) == to_be_considered[1]:
                    target_node = array[i]
                    break
        tempo = dif_components(nodes[to_be_considered[0]],nodes[target_node],array_of_nodes)
        if tempo[0]:
            array_of_nodes = tempo[1]
            final_length = final_length +to_be_considered[1]
            dict_of_all_lengths[to_be_considered[0]].remove(to_be_considered[1])
        else:
            dict_of_all_lengths[to_be_considered[0]].remove(to_be_considered[1])
    print(final_length)
    return final_length
gridland(8190, 2731, 5538, 8804, 2079, 3325, 8464, 1925, 7301, 9075, 4771, 9078, 6740, 3169, 2452, 1536, 4979, 3672, 1934, 1487, 5377, 1795, 6722, 1443, 1648, 3802, 6475, 8077, 1823, 5336, 5534, 474, 8712, 8452, 4842, 3918, 6070, 3936, 5795, 7315)
