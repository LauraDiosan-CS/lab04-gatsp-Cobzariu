from logic.GA import GA


def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    S=0
    for i in range(0, noNodes-1):
        S=S+mat[communities[i]][communities[i+1]]
    S+=mat[communities[-1]][communities[0]]
    return S




def AI_function(network,popsize,gen):
    gaParam = {'popSize': popsize, 'noGen': gen}
    problParam = {'function': modularity, 'network': network}
    output_info = {}
    bestChromosomes = []

    ga = GA(gaParam, problParam, network)
    ga.initialisation()
    ga.evaluation()
    bestRoute = ga.bestChromosome()
    for g in range(gaParam['noGen']):

        ga.oneGeneration()
        bestChromo = ga.bestChromosome()
        if bestChromo>bestRoute:
            bestRoute=bestChromo
        bestChromosomes.append(bestChromo)
    output_info['bestChromo'] = bestChromosomes
    output_info['bestRoute'] = bestRoute


    return output_info
