from domeniu.eveniment import Spectacole
from exceptii.erori import RepoError


class RepoEvenimente:

    def __init__(self):
        self.lista_evenimente = []

    def evenimente_static_repo(self):
        return self.lista_evenimente

    def adauga_eveniment(self, id_eveniment, data, timp, descriere, index=0):
        """
        Adauga un eveniment in lista utilizând o abordare recursivă.
        :param id_eveniment: Id-ul evenimentului
        :param data: Data evenimentului
        :param timp: Ora evenimentului
        :param descriere: Descrierea evenimentului
        :param index: Indexul curent în timpul recursiei (implicit 0)
        """
        if index >= len(self.lista_evenimente):
            event = Spectacole(id_eveniment, data, timp, descriere)
            self.lista_evenimente.append(event)
            return
        if self.lista_evenimente[index].id_eveniment == id_eveniment:
            raise RepoError("Id-ul exista deja")
        self.adauga_eveniment(id_eveniment, data, timp, descriere, index + 1)

    def stergere_eveniment(self, id_eveniment, index=0):
        """
        Sterge evenimentul cu Id-ul dat utilizând o abordare recursivă.
        :param id_eveniment: Id-ul evenimentului care trebuie sters
        :param index: Indexul curent în timpul recursiei (implicit 0)
        """
        if index >= len(self.lista_evenimente):
            raise RepoError("Id-ul nu exista")
        if self.lista_evenimente[index].id_eveniment == id_eveniment:
            self.lista_evenimente.pop(index)
            self._actualizeaza_iduri(index)
            return
        self.stergere_eveniment(id_eveniment, index + 1)

    def _actualizeaza_iduri(self, start_index):
        """
        Actualizează ID-urile evenimentelor începând de la un index dat.
        :param start_index: Indexul de la care începem actualizarea
        """
        if start_index >= len(self.lista_evenimente):
            return
        self.lista_evenimente[start_index].id_eveniment -= 1
        self._actualizeaza_iduri(start_index + 1)



    def modifica_descriere_eveniment(self, id_eveniment, descriere):
        """
        Modifica descrierea evenimentului cu Id-ul dat
        :param id_eveniment: Id-ul evenimentului dorit
        :param descriere: Descrierea care se va atribui evenimentului
        """
        self.lista_evenimente[id_eveniment].descriere=descriere

    def modifica_timp_eveniment(self, id_eveniment, timp):
        """
        Modifica timpul evenimentului cu Id-ul dat
        :param id_eveniment: Id-ul evenimentului dorit
        :param timp: Ora care se va atribui evenimentului
        """
        self.lista_evenimente[id_eveniment].timp= timp

    def modifica_data_eveniment(self, id_eveniment, data):
        """
        Modifica data evenimentului cu Id-ul dat
        :param id_eveniment: Id-ul evenimentului dorit
        :param data: Ora care se va atribui evenimentului
        """
        self.lista_evenimente[id_eveniment].data= data

class RepoFileEvent(RepoEvenimente):
    def __init__(self,cale_fisier):
        super().__init__()
        self.__cale_fisier=cale_fisier
        self.__citeste_tot_din_fisier()

    def evenimente_static_repo(self):
        return self.lista_evenimente

    def adauga_eveniment(self,id_eveniment,data,timp,descriere,index):
        self.adauga_eveniment_fisier(id_eveniment,data,timp,descriere)
        self.write_at_end(id_eveniment,data,timp,descriere)

    def adauga_eveniment_fisier(self,id_eveniment,data,timp,descriere):
        for lista1 in self.lista_evenimente:
            if id_eveniment == lista1.id_eveniment:
                raise RepoError("Id-ul exista deja")
        event = Spectacole(id_eveniment, data, timp, descriere)
        self.lista_evenimente.append(event)

    def stergere_eveniment(self,id_eveniment):
        self.stergere_eveniment_fisier(id_eveniment)
        self.__scrie_tot_in_fisier()

    def stergere_eveniment_fisier(self,id_eveniment):
        if id_eveniment >= len(self.lista_evenimente):
            raise RepoError("Id-ul nu exista")
        self.lista_evenimente = [eveniment for eveniment in self.lista_evenimente if eveniment.id_eveniment != id_eveniment]
        for lista in self.lista_evenimente:
            if lista.id_eveniment > id_eveniment:
                lista.id_eveniment-=1

    def modifica_descriere_eveniment(self,id_eveniment,descriere):
        self.modifica_descriere_eveniment_fisier(id_eveniment,descriere)
        self.__scrie_tot_in_fisier()

    def modifica_descriere_eveniment_fisier(self,id_eveniment,descriere):
        self.lista_evenimente[id_eveniment].descriere = descriere

    def modifica_data_eveniment(self,id_eveniment,data):
        self.modifica_data_eveniment_fisier(id_eveniment,data)
        self.__scrie_tot_in_fisier()

    def modifica_data_eveniment_fisier(self,id_eveniment,data):
        self.lista_evenimente[id_eveniment].data = data

    def modifica_timp_eveniment(self,id_eveniment,timp):
        self.modifica_timp_eveniment_fisier(id_eveniment,timp)
        self.__scrie_tot_in_fisier()

    def modifica_timp_eveniment_fisier(self,id_eveniment,timp):
        self.lista_evenimente[id_eveniment].timp = timp

    def write_at_end(self,id_eveniment,data,timp,descriere):
        with open(self.__cale_fisier,"a") as f:
            f.write(f"{id_eveniment}, {data}, {timp}, {descriere} \n")

    def __citeste_tot_din_fisier(self):
       with open(self.__cale_fisier,"r") as f:
           self.lista_evenimente.clear()
           lines=f.readlines()
           for line in lines:
               line =line.strip()
               if line!="":
                   parts=line.split(",")
                   id_invitat=int(parts[0])
                   id_invitat-=1
                   nume=parts[1]
                   adresa=parts[2]
                   descriere=parts[3]
                   event=Spectacole(id_invitat,nume,adresa,descriere)
                   self.lista_evenimente.append(event)

    def __scrie_tot_in_fisier(self):
        with open(self.__cale_fisier, "w") as f:
            for event in self.lista_evenimente:
                f.write(f"{event.id_eveniment},{event.data},{event.timp},{event.descriere} \n")
