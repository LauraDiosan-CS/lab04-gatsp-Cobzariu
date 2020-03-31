from random import randint, seed
import numpy as np


def generateARandomPermutation(n):
    # perm = [i for i in range(n)]
    # pos1 = randint(0, n - 1)
    # pos2 = randint(0, n - 1)
    # perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    # return perm
    return np.random.permutation(n).tolist()


def reverse_sublist(lst, start, end):
    sublist = lst[start:end]
    sublist.reverse()
    lst[start:end] = sublist


# permutation-based representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam  # problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['noNodes'])
        self.__fitness = 0.0

    def get_repres(self):
        return self.__repres

    def get_fitness(self):
        return self.__fitness

    def set_repres(self, l=[]):
        self.__repres = l

    def set_fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        # order XO
        pos1 = randint(-1, self.__problParam['noNodes'] - 1)
        pos2 = randint(-1, self.__problParam['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if el not in newrepres:
                if len(newrepres) < self.__problParam['noNodes'] - pos1:
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__problParam)
        offspring.set_repres(newrepres)
        return offspring

    def insert_mutation(self):
        # insert mutation
        pos1 = randint(0, self.__problParam['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)

    def inversion_mutation(self):

        pos1 = randint(0, self.__problParam['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        if pos2 - pos1 == 1:
            self.__repres[pos1], self.__repres[pos2] = self.__repres[pos2], self.__repres[pos1]
            return
        reverse_sublist(self.__repres, pos1, pos2)

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

    def __lt__(self, other):
        return self.__fitness > other.get_fitness()
