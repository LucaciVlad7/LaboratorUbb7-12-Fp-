from domeniu.eveniment import Spectacole

class serviceEvenimente:

    def __init__(self, _validator_evenimente, _repo_evenimente):
        self.__validator_evenimente = _validator_evenimente
        self.__repo_evenimente = _repo_evenimente

    def evenimente_static_service(self):
        return self.__repo_evenimente.evenimente_static_repo()

    def adauga_event(self,id_event,data,timp,descriere):
        #creezi eveniment si il bagi aici
        #self.__validator_evenimente.valideaza_evenimente(eveniment)
        event=Spectacole(id_event,data,timp,descriere)
        self.__validator_evenimente.valideaza_eveniment(event)
        lista=self.__repo_evenimente.adauga_eveniment(id_event,data,timp,descriere)
        return lista

    def sterge_event(self,id_event):
        lista = self.__repo_evenimente.stergere_eveniment(id_event)
        return lista

    def modifica_descriere(self,id_event,descriere):
        lista=self.__repo_evenimente.modifica_descriere_eveniment(id_event,descriere)
        return lista

    def modifica_timp(self,id_event,timp):
        lista=self.__repo_evenimente.modifica_timp_eveniment(id_event,timp)
        return lista

    def modifica_data(self,id_event,data):
        lista = self.__repo_evenimente.modifica_data_eveniment(id_event, data)
        return lista

    def cautare_eveniment_dupa_id(self,id_cautat):
        """
        afiseaza datele evenimentului cu id_ul dat
        :param id_cautat: Id-ul evenimentului cautat
        """
        lista_cautare=[]
        lista_evenimente = self.evenimente_static_service()
        for lista in lista_evenimente:
            if lista.id_eveniment == id_cautat:
                return lista.data,lista.timp,lista.descriere
        return None,None,None

    def primele_20ls_evenimente(self, lista_participanti):
        """
        Afiseaza numarul de participanti si descrierea pentru primele 20% evenimente
        (in functie de numarul de invitati)
        :param lista_participanti: lista de legatura
        """
        lista_evenimente = self.evenimente_static_service()
        douazeciLaSuta = int((2 * len(lista_evenimente)) / 10)
        lista_participanti.sort(key=lambda item: item.id_eveniment)
        event = {}
        curent = 0
        last_id = -1
        for participant in lista_participanti:
            if last_id == -1 or participant.id_eveniment == last_id:
                curent += 1
                if participant.id_eveniment not in event:
                    event[participant.id_eveniment] = [0, participant.descriere_eveniment]
            else:
                event[last_id][0] = curent
                curent = 1
                if participant.id_eveniment not in event:
                    event[participant.id_eveniment] = [0, participant.descriere_eveniment]

            last_id = participant.id_eveniment
        if last_id != -1:
            event[last_id][0] = curent
        sorted_events = sorted(event.items(), key=lambda item: item[1][0], reverse=True)
        douazeciLaSuta = min(douazeciLaSuta, len(sorted_events))
        for i in range(douazeciLaSuta):
            print("_____________________")
            print(sorted_events[i][1][0])  # Number of participants
            print(sorted_events[i][1][1])  # Event description
        return sorted_events[0][1][0],sorted_events[0][1][1]

    def doua_zeci_la_sute(self,lista_participanti):#teste
        """
        Afiseaza primele 20% evenimente cu cei mai multi participanti
        :param lista_participanti:
        :return:
        """
        lista_evenimente = self.evenimente_static_service()
        douazeciLaSuta = int((2 * len(lista_evenimente)) / 10)
        lista_participanti.sort(key=lambda item: item.id_eveniment)
        event = {}
        curent = 0
        last_id = -1
        for participant in lista_participanti:
            if last_id == -1 or participant.id_eveniment == last_id:
                curent += 1
                if participant.id_eveniment not in event:
                    event[participant.id_eveniment] = [0, participant.descriere_eveniment]
            else:
                event[last_id][0] = curent
                curent = 1
                if participant.id_eveniment not in event:
                    event[participant.id_eveniment] = [0, participant.descriere_eveniment]
            last_id = participant.id_eveniment
        if last_id != -1:
            event[last_id][0] = curent
        sorted_events = sorted(event.items(), key=lambda item: item[1][0], reverse=True)
        douazeciLaSuta = min(douazeciLaSuta, len(sorted_events))
        return sorted_events,douazeciLaSuta
