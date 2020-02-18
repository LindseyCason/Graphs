
# def earliest_ancestor(ancestors, starting_node):
#     #array of ancestors
#     #starting node
#     #ancestors_list which will keep track of connections

#     '''
#     Add starting node to the set.
#     if any 0 position matches starting node move that pair to the set
#     retrieve the 1 position and call it current_ancestor 
#     if the current_ancestor matches any 0 position add that pair to the set
#     set current_ancestor to the 1 position of the new pair passed in, repeat.
#     if no match, return last pair item in 1 position


#     [] make child array, target 9
#     [8] loop through and add to parent array
#     [4,11]  4<11 if no matches, retrn less num
#     '''
#     parent=list()
#     child=list()

#     print("starting node ", starting_node)
#     print("ancestors passed in ", ancestors)

#     for i in ancestors:
#         if starting_node == i[0]:
#             parent.append(i[1])

#     print(parent)