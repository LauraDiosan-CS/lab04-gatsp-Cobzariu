from Console import Console
from Repository import Repository
import os

from Service import Service


def main():
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data', 'hardE.txt')
    Repo = Repository(filePath)
    Repo.read_tsp_format()
    Serv=Service(Repo)
    Cons=Console(Serv)
    Cons.print_info(100,100)

main()