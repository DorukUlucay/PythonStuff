import tree

Tree = tree.Tree()

Tree.Add('branch one')
Tree.Branches[0].Add('branch of branch one')
Tree.Add('branch two')
Tree.Branches[1].Add('first sub branch of branch two')
Tree.Branches[1].Branches[0].Add('first sub branch of sub branch of branch two')
Tree.Branches[1].Branches[0].Add('second sub branch of sub branch of branch two')
Tree.Branches[1].Branches[0].Add('third sub branch of sub branch of branch two')
Tree.Branches[1].Add('second sub branch of branch two')

Tree.PrintTree(None)

Tree.FindBranchByName(None, 'Tkinter')
