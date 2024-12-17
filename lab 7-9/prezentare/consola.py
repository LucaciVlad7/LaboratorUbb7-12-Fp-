from exceptii.erori import ValidationError, ProbEroare
import random
from infrastructura.repo_legatura import RepoLegatura

class Consola:

    def __init__(self,_service_invitati,_service_evenimente):
        self.__service_invitati=_service_invitati
        self.__service_evenimente=_service_evenimente
        self.__comenzi ={
            "adauga_invitat":self.__ui_add_invitat,
            "afiseaza_invitati":self.__ui_print_invitati,
            "sterge_invitat":self.__ui_delete_invitat,
            "cauta_invitat":self.__ui_cauta_invitat,
            "modifica_nume":self.__ui_modifica_nume,
            "modifica_adresa":self.__ui_modifica_adresa,
            "adauga_eveniment":self.__ui_add_eveniment,
            "afiseaza_evenimente":self.__ui_print_eveniment,
            "sterge_eveniment":self.__ui_delete_eveniment,
            "modifica_data":self.__ui_modifica_data,
            "modifica_timp":self.__ui_modifica_timp,
            "modifica_descriere":self.__ui_modifica_descriere,
            "cauta_eveniment":self.__ui_cauta_eveniment,
            "adauga_legatura":self.__ui_creare_legatura,
            "adauga_random":self.__ui_genereaza_invitati_random,
            "lista_invitat":self.__ui_lista_invitat_sortata_dupa_descriere,
            "invitat_maxim":self.__ui__invitatul_cu_max_evenimente,
            "lista_20ls":self.__ui_primele_20ls_evenimente,
            "lista_pers_2_eventuri":self.__ui_lista_persoanelor_care_participa_la_2_evenimente_simultan,
            "adauga_prob":self.__ui_prob_adauga,
            "stergere_prob":self.__ui_prob_stergere,
            "modifica_adresa_prob":self.__ui_prob_modifica_adresa,
            "modifica_nume_prob":self.__ui_prob_modifica_nume,
        }

    obLegatura = RepoLegatura()

    def __ui_prob_adauga(self):
        id_invitat = int(input("id invitat:"))
        id_invitat -= 1
        nume = input("nume:")
        adresa = input("adresa:")
        self.__service_invitati.adauga_prob(id_invitat, nume, adresa)

    def __ui_prob_stergere(self):
        id_invitat = int(input("Introduceti Id-ul invitatului care trebuie sters"))
        id_invitat -= 1
        self.__service_invitati.stergere_prob(id_invitat)

    def __ui_prob_modifica_adresa(self):
        id_invitat = int(input("Id invitat: "))
        id_invitat -= 1
        adresa = input("Adresa care va fi atribuita")
        self.__service_invitati.modifica_adresa_prob(id_invitat, adresa)

    def __ui_prob_modifica_nume(self):
        id_invitat = int(input("Id invitat: "))
        id_invitat -= 1
        nume = input("Numele care va fi atribuit: ")
        self.__service_invitati.modifica_nume_prob(id_invitat, nume,0)

    def __ui_print_invitati(self):#merge
        lista=self.__service_invitati.invitati_static_service()
        if len(lista) == 0:
            print("nu exista invitati!")
            return
        print("invitatii sunt:")
        for invitat in lista:
            print(f"Invitatul cu Id-ul: {invitat.id_invitat+1}")
            print(invitat.nume)
            print(invitat.adresa)

    def __ui_add_invitat(self):#merge
        id_invitat = int(input("id invitat:"))
        id_invitat -= 1
        nume = input("nume:")
        adresa = input("adresa:")
        self.__service_invitati.service_adauga(id_invitat,nume,adresa)

    def __ui_genereaza_invitati_random(self):
        for i in range(1,11):
            id_invitat = random.randint(1, 3)
            nume = ["Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ioana", "Mihai", "Gabriela", "Cristian", "Daniela",
                "Florin", "Anca", "Vasile", "Diana", "Radu"]
            nume_invitat = random.choice(nume)
            strazi = ["Calea Victoriei", "Bulevardul Unirii", "Șoseaua Kiseleff", "Strada Lipscani", "Strada Academiei",
                  "Bulevardul Magheru", "Calea Dorobanților", "Strada Mihai Eminescu", "Strada Ion Luca Caragiale"]
            adresa_invitat = random.choice(strazi)
            self.__service_invitati.service_adauga(id_invitat, nume_invitat, adresa_invitat)

    def __ui_delete_invitat(self):#merge
        id_invitat=int(input("Introduceti Id-ul invitatului care trebuie sters"))
        id_invitat -= 1
        self.__service_invitati.service_delete(id_invitat)

    def __ui_cauta_invitat(self):
        id_invitat=(int(input("Introduceti Id-ul invitatului cautat")))
        id_invitat -= 1
        nume,adresa=self.__service_invitati.cautare_invitat_dupa_id(id_invitat)
        if nume!=None and adresa!=None:
            print(f"Invitatul cu Id-ul: {id_invitat+1} este {nume} si sta la adresa {adresa}")
        else:
            print(f"Invitatul nu exista")

    def __ui_modifica_nume(self):#merge
        id_invitat=int(input("Id invitat: "))
        id_invitat-=1
        nume=input("Numele care va fi atribuit: ")
        self.__service_invitati.service_modifica_nume(id_invitat,nume)

    def __ui_modifica_adresa(self):#merge
        id_invitat=int(input("Id invitat: "))
        id_invitat -= 1
        adresa=input("Adresa care va fi atribuita")
        self.__service_invitati.service_modifica_adresa(id_invitat,adresa)

    def __ui_add_eveniment(self):#merge
        id_eveniment = int(input("id eveniment:"))
        id_eveniment-=1
        data = input("data: ")
        timp = input("timp: ")
        descriere= input("descriere: ")
        self.__service_evenimente.adauga_event(id_eveniment,data,timp,descriere)

    def __ui_print_eveniment(self):#merge
        evenimente=self.__service_evenimente.evenimente_static_service()
        if len(evenimente) == 0:
            print("nu exista evenimente!")
            return
        print("evenimentele sunt:")
        for eveniment in evenimente:
            print(f"Invitatul cu Id-ul: {eveniment.id_eveniment + 1}")
            print(eveniment.data)
            print(eveniment.timp)
            print(eveniment.descriere)

    def __ui_delete_eveniment(self):#merge
        id_event=int(input("Id-ul evenimentului care va fi sters"))
        id_event-=1
        if id_event > len(self.__service_evenimente.evenimente_static_service()):
            raise ValueError("Nu exista invitat")
        self.__service_evenimente.sterge_event(id_event)

    def __ui_modifica_descriere(self):#merge
        id_event=int(input("Id eveniment: "))
        id_event -= 1
        if id_event > len(self.__service_evenimente.evenimente_static_service()):
            raise ValueError("Nu exista invitat")
        descriere=input("Descrierea care va fi atribuit: ")
        self.__service_evenimente.modifica_descriere(id_event,descriere)

    def __ui_modifica_timp(self):#merge
        id_event = int(input("Id eveniment: "))
        id_event-=1
        if id_event > len(self.__service_evenimente.evenimente_static_service()):
            raise ValueError("Nu exista invitat")
        timp = input("Durata care va fi atribuit: ")
        self.__service_evenimente.modifica_timp(id_event, timp)

    def __ui_modifica_data(self):#merge
        id_eveniment = int(input("Id eveniment: "))
        id_eveniment-=1
        if id_eveniment>len(self.__service_evenimente.evenimente_static_service()):
            raise ValueError("Nu exista invitat")
        data = input("Data care va fi atribuit: ")
        self.__service_evenimente.modifica_data(id_eveniment, data)

    def __ui_cauta_eveniment(self):
        id_eveniment = (int(input("Introduceti Id-ul invitatului cautat")))
        id_eveniment -= 1
        data,timp,descriere=self.__service_evenimente.cautare_eveniment_dupa_id(id_eveniment)
        if data!=None and timp!=None and descriere!=None:
            print(f"Evenimentul cautat este {descriere} si se va desfasura in data de {data} la ora {timp}")
        else :
            print("Evenimentul nu exista")




    def __ui_creare_legatura(self):#merge,aici ai ramas
        id_invitat=int(input("Introduceti Id-ul invitatului"))
        id_eveniment=int(input("Introduceti Id-ul evenimentului"))
        id_eveniment-=1
        id_invitat-=1
        lista_invitati=self.__service_invitati.invitati_static_service()
        lista_evenimente=self.__service_evenimente.evenimente_static_service()
        Consola.obLegatura.legatura(id_invitat,id_eveniment,lista_invitati, lista_evenimente)

    def __ui_lista_invitat_sortata_dupa_descriere(self):#merge
        id_invitat=int(input("Introduceti Id-ul invitatului dorit"))
        id_invitat-=1
        lista_participanti=Consola.obLegatura.lista_participanti_static()
        lista_la_care_participa=self.__service_invitati.lista_sortata(id_invitat,lista_participanti)
        print("Invitatul dorit participa la evenimentele:")
        for lista in lista_la_care_participa:
            print("----------------------------------")
            print(lista.id_eveniment+1)
            print(lista.descriere_eveniment)


    def __ui__invitatul_cu_max_evenimente(self):
        lista_participanti=Consola.obLegatura.lista_participanti_static()
        topParticipantiLaEventuri=self.__service_invitati.persoana_care_participa_la_cele_mai_multe_event(lista_participanti)
        for i in topParticipantiLaEventuri:
            print(topParticipantiLaEventuri[i][0])
            print(topParticipantiLaEventuri[i][1])

    def __ui_primele_20ls_evenimente(self):#merge
        lista_participanti = Consola.obLegatura.lista_participanti_static()
        sorted_events,douazeciLaSuta=self.__service_evenimente.primele_20ls_evenimente(lista_participanti)
        for i in range(douazeciLaSuta):
            print("_____________________")
            print(sorted_events[i][0])  # ID
            print(sorted_events[i][1][0])  # Nr paticipanti
            print(sorted_events[i][1][1])  # Descriere

    def __ui_lista_persoanelor_care_participa_la_2_evenimente_simultan(self):
        lista_participanti = Consola.obLegatura.lista_participanti_static()
        lista_persoane=self.__service_invitati.lista_persoanelor_care_participa_la_2_evenimente_simultan(lista_participanti)
        if lista_persoane!=None:
            print("Invitati care participa la 2 sau mai multe evenimente simultan:")
            for inv in lista_persoane:
                print(inv.nume)
        else:
            print("Nu exista invitati care sa participe la 2 sau mai multe evenimente simultan")



    def run(self):
        while True:
            nume_comanda = input(">>>")
            nume_comanda = nume_comanda.lower()
            nume_comanda = nume_comanda.strip()
            if nume_comanda == "":
                continue
            if nume_comanda == "exit":
                break
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError as ve:
                    print("valoare numerica invalida!")
                except ValidationError as ve:
                    print(f"eroare de validare:{ve}")
                except ProbEroare as pe:
                    print(f"erorare de probabilitate:{pe}")
            else:
                print("comanda invalida!")
