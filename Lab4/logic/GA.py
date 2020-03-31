import random
import math
from logic.Chromosome import Chromosome



class GA:
    def __init__(self, param=None, problParam=None, net=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []
        self.__network = net

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__network)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            fitness = self.__problParam['function'](c.get_repres(), self.__network)
            c.set_fitness(fitness)

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.get_fitness() < best.get_fitness():
                best = c
        return best

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.get_fitness() > best.get_fitness():
                best = c
        return best

    def selection(self):
        pos1 = random.randint(0, self.__param['popSize'] - 1)
        pos2 = random.randint(0, self.__param['popSize'] - 1)
        if self.__population[pos1].get_fitness() < self.__population[pos2].get_fitness():
            return pos1
        else:
            return pos2

    def k_selection(self):
        pos_array=[]
        for i in range(int(self.__param['popSize']/2)):
            pos1 = random.randint(0, self.__param['popSize'] - 1)
            pos_array.append(pos1)
        best_length=math.inf
        for pos in pos_array:
            if self.__population[pos].get_fitness()<best_length:
                best_length=self.__population[pos].get_fitness()
                best_pos=pos
        return best_pos

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.k_selection()]
            p2 = self.__population[self.k_selection()]
            off = p1.crossover(p2)
            off.inversion_mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.inversion_mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.insert_mutation()
            off.set_fitness = self.__problParam['function'](off.set_repres)
            worst = self.worstChromosome()
            if (off.set_fitness < worst.set_fitness):
                worst = off
