from domeniu.invitat import Persoane
from exceptii.erori import RepoError


class RepoInvitat:

    def __init__(self):
        self.lista_invitati = []

    def invitati_static_repo(self):
        return self.lista_invitati

    def adauga_invitat(self,id_invitat,nume,adresa):
        """
        Adauga un invitat in lista
        :param id_invitat: Id-ul invitatului
        :param nume: Numele invitatului
        :param adresa: Adresa invitatului
        """
        lista = Persoane(id_invitat,nume,adresa)
        for lista1 in self.lista_invitati:
            if id_invitat == lista1.id_invitat:
                raise RepoError("Id-ul exista deja\n")
        self.lista_invitati.append(lista)
        return self.lista_invitati

    def stergere_invitat(self,id_invitat):
        """
        Sterge invitatul cu Id-ul dat
        :param id_invitat: Id-ul invitatului care trebuie sters
        """
        if id_invitat >= len(self.lista_invitati):
            raise RepoError("Id-ul nu exista")
        self.lista_invitati=[invitati for invitati in self.lista_invitati if invitati.id_invitat != id_invitat]
        for lista in self.lista_invitati:
            if lista.id_invitat > id_invitat:
                lista.id_invitat-=1

    def modifica_numele_invitatului(self,id_invitat,nume):
        """
        Modifica numele invitatul cu Id-ul dat
        :param id_invitat: Id-ul invitatului dorit
        :param nume: Numele care se va atribui invitatului
        """
        self.lista_invitati[id_invitat].nume=nume


    def modifica_adresa_invitatului(self,id_invitat,adresa):
        """
        Modifica adresa invitatul cu Id-ul dat
        :param id_invitat: Id-ul invitatului dorit
        :param adresa: Adresa care se va atribui invitatului
        """
        self.lista_invitati[id_invitat].adresa=adresa

class RepoFileInv(RepoInvitat):
    def __init__(self,cale_fisier):
        super().__init__()
        self.__cale_fisier=cale_fisier
        self.__citeste_tot_din_fisier()

    def invitati_static_repo(self):
        return self.lista_invitati

    def adauga_invitat(self,id_invitat,nume,adresa):
        self.adauga_invitat_fisier(id_invitat,nume,adresa)
        self.write_at_end(id_invitat,nume,adresa)

    def adauga_invitat_fisier(self,id_invitat,nume,adresa):
        lista = Persoane(id_invitat, nume, adresa)
        for lista1 in self.lista_invitati:
            if id_invitat == lista1.id_invitat:
                raise RepoError("Id-ul exista deja\n")
        self.lista_invitati.append(lista)
        return self.lista_invitati

    def stergere_invitat(self,id_invitat):
        self.sterge_invitat_fisier(id_invitat)
        self.__scrie_tot_in_fisier()

    def sterge_invitat_fisier(self,id_invitat):
        if id_invitat >= len(self.lista_invitati):
            raise RepoError("Id-ul nu exista")
        self.lista_invitati=[invitati for invitati in self.lista_invitati if invitati.id_invitat != id_invitat]
        for lista in self.lista_invitati:
            if lista.id_invitat > id_invitat:
                lista.id_invitat-=1

    def modifica_numele_invitatului(self,id_invitat,nume):
        self.modifica_numele_invitatului_fisier(id_invitat,nume)
        self.__scrie_tot_in_fisier()

    def modifica_numele_invitatului_fisier(self,id_invitat,nume):
        self.lista_invitati[id_invitat].nume=nume
        self.__scrie_tot_in_fisier()

    def modifica_adresa_invitatului(self,id_invitat,adresa):
        self.modifica_adresa_invitatului_fisier(id_invitat,adresa)
        self.__scrie_tot_in_fisier()

    def modifica_adresa_invitatului_fisier(self,id_invitat,adresa):
        self.lista_invitati[id_invitat].adresa=adresa
        self.__scrie_tot_in_fisier()

    def write_at_end(self, id_invitat,nume,adresa):
        with open(self.__cale_fisier, "a") as f:
            f.write(f"{id_invitat},{nume},{adresa} \n")

    def __citeste_tot_din_fisier(self):
       with open(self.__cale_fisier,"r") as f:
           self.lista_invitati.clear()
           lines=f.readlines()
           for line in lines:
               line =line.strip()
               if line!="":
                   parts=line.split(",")
                   id_invitat=int(parts[0])
                   id_invitat-=1
                   nume=parts[1]
                   adresa=parts[2]
                   invitat=Persoane(id_invitat,nume,adresa)
                   self.lista_invitati.append(invitat)

    def __scrie_tot_in_fisier(self):
        with open(self.__cale_fisier,"w") as f:
            for invitat in self.lista_invitati:
                f.write(f"{invitat.id_invitat},{invitat.nume},{invitat.adresa} \n")
