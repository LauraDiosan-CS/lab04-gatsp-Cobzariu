import os

import networkx as nx

from logic.Utils import distance


class Repository:
    def __init__(self, name):
        self.__filePath = name
        self.__network = {}

    def get_network(self):
        return self.__network

    def read_txt(self):
        f = open(self.__filePath, "r")
        net = {}
        n = int(f.readline())
        net['noNodes'] = n
        mat = []
        for i in range(n):
            mat.append([])
            line = f.readline()
            elems = line.split(",")
            for j in range(n):
                mat[-1].append(int(elems[j]))
        net['mat'] = mat
        f.close()
        self.__network = net

    def read_tsp_format(self):
        f = open(self.__filePath, "r")
        lines = f.readlines()
        cities = []
        for line in lines:
            city = line.split(' ')
            cities.append(dict(index=float(city[0]), x=float(city[1]), y=float(city[2])))
        cost_matrix = []
        rank = len(cities)
        for i in range(rank):
            row = []
            for j in range(rank):
                row.append(distance(cities[i], cities[j]))
            cost_matrix.append(row)
        net={}
        net['noNodes'] = rank
        net['mat'] = cost_matrix
        self.__network=net


