
from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Show_Best(self):
        #self.parent.Evaluate('GUI')
        pass

    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].Evaluate('GUI')
        #self.parent.Evaluate('GUI')
        #for currentGeneration in range(c.numberofGenerations):
        #    self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.setID(self.nextAvailableID)
        self.nextAvailableID += 1


    def Mutate(self):
        self.child.Mutate()
        # up to 61 all good - weights are changing

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(f'parent: {self.parent.fitness} child: {self.child.fitness}')

