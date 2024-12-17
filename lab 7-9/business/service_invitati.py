from math import trunc

from domeniu.invitat import Persoane
from infrastructura.repo_legatura import RepoLegatura
from infrastructura.RepoProbabilitate import RepoProbabilitate


class serviceInvitat:

    def __init__(self, _validator_invitat, _repo_invitat):
        self.__validator_invitat=_validator_invitat
        self.__repo_invitat=_repo_invitat
        self.__legatura= RepoLegatura()

    prob=RepoProbabilitate("./infrastructura/invitat.txt",100)

    def adauga_prob(self,id_invitat,nume,adresa):
        serviceInvitat.prob.adauga_invitat_probabilitate(id_invitat,nume,adresa)

    def stergere_prob(self,id_invitat):
        serviceInvitat.prob.sterge_invitat_probabilitate(id_invitat)

    def modifica_nume_prob(self,id_invitat,nume,index):
        serviceInvitat.prob.modifica_invitat_nume_probabilitate(id_invitat,nume)

    def modifica_adresa_prob(self,id_invitat,adresa):
        serviceInvitat.prob.modifica_adresa_invitatului_probabilitate(id_invitat,adresa)


    def invitati_static_service(self):
        return self.__repo_invitat.invitati_static_repo()

    def service_adauga(self,id_invitat,nume,adresa):
        inv=Persoane(id_invitat,nume,adresa)
        self.__validator_invitat.valideaza_invitat(inv)
        lista=self.__repo_invitat.adauga_invitat(id_invitat,nume,adresa)
        return lista

    def service_delete(self,id_invitat):
        lista=self.__repo_invitat.stergere_invitat(id_invitat)
        return lista

    def service_modifica_nume(self,id_invitat,nume):
        lista=self.__repo_invitat.modifica_numele_invitatului(id_invitat,nume)
        return lista

    def service_modifica_adresa(self,id_invitat,adresa):
        lista=self.__repo_invitat.modifica_adresa_invitatului(id_invitat,adresa)
        return lista

    def cautare_invitat_dupa_id(self,id_invitat_cautat):
        """
        afiseaza informatiile despre invitatul dorit
        :param id_invitat_cautat: Id-ul invitatului dorit
        """
        """
        Analiza Complexitatii
        caz favorabil: invitatul cautat este primul in lista
        caz mediu: invitatul cautat este in lista
        caz nefavorabil: invitatul nu este in lista
        Complexitate timp: O(n)
        """
        lista_invitati=self.invitati_static_service()
        for lista in lista_invitati:
            if lista.id_invitat==id_invitat_cautat:
                return lista.nume,lista.adresa
        return None,None

    def lista_sortata(self,id_invitat,lista_participanti):#test
        """
        Returneaza lista evenimentelor la care participa un invitat
        sortata dupa descriere
        :param id_invitat: Id-ul invitatului dorit
        :param lista_participanti: lista cu legaturile dintre evenimente si invitati
        """
        lista_sortata=[]
        for participant in lista_participanti:
            if participant.id_invitat == id_invitat:
                lista_sortata.append(participant)
        lista_sortata.sort(key=lambda item: item.descriere_eveniment)
        return lista_sortata

    def persoana_care_participa_la_cele_mai_multe_event(self, lista_participanti):#teste
        """
        Afiseaza id-ul si numele invitatilor care participa la cele
        mai multe evenimente.
        :param lista_participanti: lista dintre inv si evente curenta
        """
        if len(lista_participanti) == 0:
            print("Nu exista participanti")
            return

        #Selection sort
        n=len(lista_participanti)
        for i in range(n-1):
            index_min=i
            for j in range(i+1,n):
                if(lista_participanti[j].id_invitat<lista_participanti[index_min].id_invitat):
                    index_min=j
                if index_min!=i:
                    lista_participanti[i],lista_participanti[index_min]=lista_participanti[index_min],lista_participanti[i]

        maxEvenimente = 0
        last_id = -1
        curent = 0
        nume = ""
        topParticipantiLaEventuri = {}
        nrParticipanti=0
        for participant in lista_participanti:
            if last_id == -1 or participant.id_invitat == last_id:
                curent += 1
            else:
                if curent > maxEvenimente:
                    maxEvenimente = curent
                    nrParticipanti=0
                    topParticipantiLaEventuri.clear()
                    topParticipantiLaEventuri[nrParticipanti]=[0,0]
                    topParticipantiLaEventuri[nrParticipanti][0] = participant.id_invitat
                    topParticipantiLaEventuri[nrParticipanti][1] = participant.nume_invitat
                elif curent == maxEvenimente:
                    nrParticipanti+=1
                    topParticipantiLaEventuri[nrParticipanti]=[0,0]
                    topParticipantiLaEventuri[nrParticipanti][0] = participant.id_invitat
                    topParticipantiLaEventuri[nrParticipanti][1] = participant.nume_invitat
                curent = 1
            last_id = participant.id_invitat
            nume = participant.nume_invitat
        if curent > maxEvenimente:
            maxEvenimente = curent
            nrParticipanti = 0
            topParticipantiLaEventuri.clear()
            topParticipantiLaEventuri[nrParticipanti]=[0,0]
            topParticipantiLaEventuri[nrParticipanti][0] =last_id
            topParticipantiLaEventuri[nrParticipanti][1] = nume
        elif curent == maxEvenimente:
            nrParticipanti += 1
            topParticipantiLaEventuri[nrParticipanti]=[0,0]
            topParticipantiLaEventuri[nrParticipanti][0] = last_id
            topParticipantiLaEventuri[nrParticipanti][1] = nume
        return topParticipantiLaEventuri

    def lista_persoanelor_care_participa_la_2_evenimente_simultan(self,lista_participanti):#teste
        """
        Afiseaza lista invitatiilor care participa la 2 evenimente simultan
        :param lista_participanti: lista de participanti
        """
        last_id=-1
        curent=0
        nume=""
        lista_persoane=[]

        #Shake sort
        swapped=True
        n=len(lista_participanti)
        start=0
        end=n-1
        while swapped and start<end:
            swapped=False
            for i in range(start,end):
                if lista_participanti[i].id_invitat>lista_participanti[i+1].id_invitat:
                    lista_participanti[i],lista_participanti[i+1]=lista_participanti[i+1],lista_participanti[i]
                    swapped=True
            if not swapped:
                break
            swapped=False
            end-=1
            for i in range(end,start,-1):
                if lista_participanti[i].id_invitat<lista_participanti[i-1].id_invitat:
                    lista_participanti[i],lista_participanti[i-1]=lista_participanti[i-1],lista_participanti[i]
                    swapped=True
            start +=1


        for participant in lista_participanti:
            if last_id==-1 or last_id==participant.id_invitat:
                curent+=1
            else:
                if curent>=2:
                    inv=Persoane(last_id,nume,"Aaaaaa")
                    lista_persoane.append(inv)
                curent=1
            last_id=participant.id_invitat
            nume=participant.nume_invitat
        if curent >= 2:
            inv=Persoane(last_id,nume,"Aaaaa")
            lista_persoane.append(inv)
        if len(lista_persoane)!=0:
            return lista_persoane
        return None