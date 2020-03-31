class Console:
    def __init__(self,s):
        self.__service=s

    def print_info(self,popSize,gen):
        info=self.__service.find_communities(popSize,gen)
        route=info['bestRoute']
        print('Drumul de lungime minima: ',route.get_fitness(),' ',route.get_repres(),'\n')
        nr=0
        for chrom in info['bestChromo']:
            print('Generatia ',nr,'fitness ',chrom.get_fitness(),' ',chrom.get_repres())
            nr+=1


