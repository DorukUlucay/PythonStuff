import tree

#initialize tree
myTree = tree.Tree()

#add a branch
myTree.Add('Food')

#add branches to the branch above
myTree.Branches[0].Add('Fruit')
myTree.Branches[0].Add('Vegetable')
myTree.Branches[0].Add('Meat')

#add a subbranch
myTree.Branches[0].Branches[0].Add('Red')

#and another subbranch to one above
myTree.Branches[0].Branches[0].Branches[0].Add('Apple')

#find branch by name and add it a subbranch
myTree.FindBranchByName(None, 'Red').Add('Raspberry')

#print the tree
myTree.PrintTree(None)
