
from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):

        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")
        #os.system("del tmp*.nndf")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(0, c.populationSize):
            #self.nextAvailableID as parameter
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        pass
    def Show_Best(self):
        min_fitness = 0
        min_res = self.parents[0]
        for parent in self.parents:
            if self.parents[parent].fitness < min_fitness:
                min_fitness = self.parents[parent].fitness
                min_res = self.parents[parent]
        print(min_fitness, min_res)
        min_res.Start_Simulation("GUI")
        #self.parent.Evaluate('GUI')


    def Evolve(self):
        self.Evaluate(self.parents)
        #self.parent.Evaluate('GUI')

        for currentGeneration in range(c.numberofGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Evaluate(self, solutions):

        for parent in solutions:
            solutions[parent].Start_Simulation('DIRECT')
        for parent in solutions:
            solutions[parent].Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        for parent in self.parents:
            print(f'\nparent: {self.parents[parent].fitness} child: {self.children[parent].fitness}\n')
