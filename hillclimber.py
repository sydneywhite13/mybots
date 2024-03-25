
from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Show_Best(self):
        self.parent.Evaluate('GUI')

    def Evolve(self):
        self.parent.Evaluate('GUI')
        for currentGeneration in range(c.numberofGenerations):
            self.Evolve_For_One_Generation()
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        # up to 61 all good - weights are changing

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(f'parent: {self.parent.fitness} child: {self.child.fitness}')

