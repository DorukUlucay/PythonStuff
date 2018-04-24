class Branch:

    Description = ""
    def __init__(self):
        self.Branches = []

    def Add(self, desc):
        x = Branch()
        x.Description = desc
        self.Branches.append(x)

class Tree:

    def __init__(self):
        self.Branches = []

    def Add(self, desc):
        x = Branch()
        x.Description = desc
        self.Branches.append(x)

    level = 0
    def PrintTree(self, branch):
        if(branch==None):
            for x in self.Branches:
                print('-'*self.level + x.Description)
                self.level = self.level + 1
                self.PrintTree(x)
                self.level = self.level - 1
        else:
            for x in branch.Branches:
                print('-'*self.level + x.Description)
                self.level = self.level + 1
                self.PrintTree(x)
                self.level = self.level - 1

    current = ""
    def FindBranchByName(self, branch, Description):
        if(branch==None):
            self.current="root"
            for x in self.Branches:
                if (x.Description == Description):
                    self.current="#>"+x.Description
                    return x
                else:
                    self.current="#>"+x.Description+">"
                    return self.FindBranchByName(x, Description)
        else:
            for x in branch.Branches:
                if (x.Description == Description):
                    self.current=self.current+x.Description
                    return x
                else:
                    return self.FindBranchByName(x, Description)
        
