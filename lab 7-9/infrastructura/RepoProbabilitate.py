from operator import truediv

from exceptii.erori import ProbEroare, RepoError
from infrastructura.repo_invitat import RepoFileInv
import random

class RepoProbabilitate(RepoFileInv):
    def __init__(self, path,probabilititate):
        self.__probabilititate=probabilititate
        super().__init__(path)

    def adauga_invitat_probabilitate(self,id_invitat,nume,adresa):
        if random.randint(900,1000)<self.__probabilititate:
            raise ProbEroare("Probabilitate")
        super().adauga_invitat(id_invitat,nume,adresa)

    def sterge_invitat_probabilitate(self,id_invitat):
        if random.randint(900,1000)<self.__probabilititate:
            raise ProbEroare("Probabilitate")
        super().stergere_invitat(id_invitat)

    def modifica_invitat_nume_probabilitate(self,id_invitat,nume):
        if random.randint(900,1000)<self.__probabilititate:
            raise ProbEroare("Probabilitate")
        super().modifica_numele_invitatului(id_invitat,nume)



    def modifica_adresa_invitatului_probabilitate(self,id_invitat,adresa):
        if random.randint(900,1000)<self.__probabilititate:
            raise ProbEroare("Probabilitate")
        super().modifica_adresa_invitatului(id_invitat,adresa)
