from logic import Al


class Service:
    def __init__(self, r):
        self.__repo = r

    def find_communities(self,popSize,nr):
        return Al.AI_function(self.__repo.get_network(),popSize,nr)
