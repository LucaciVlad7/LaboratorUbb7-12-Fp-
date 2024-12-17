from business.service_invitati import serviceInvitat
from business.service_evenimente import serviceEvenimente
from infrastructura.repo_eveniment import RepoEvenimente, RepoFileEvent
from infrastructura.repo_invitat import RepoInvitat, RepoFileInv
from validare.validare_eveniment import ValidatorEveniment
from validare.validare_invitat import ValidatorInvitat
from infrastructura.repo_legatura import RepoLegatura

class Teste(object):

    def __init__(self):
        self.__validator_invitat = ValidatorInvitat()
        self.__repo_invitat = RepoInvitat()
        self.__service_invitat = serviceInvitat(self.__validator_invitat, self.__repo_invitat)
        self.__repo_invitat_file = RepoFileInv("infrastructura/invitat.txt")

        self.__validator_eveniment = ValidatorEveniment()
        self.__repo_eveniment = RepoEvenimente()
        self.__repo_eveniment_file = RepoFileEvent("infrastructura/event.txt")
        self.__service_eveniment = serviceEvenimente(self.__validator_eveniment, self.__repo_eveniment)


    def ruleaza_toate_testele(self):
        self.teste_service()
        self.teste_repo()

    def teste_validari(self):
        #Invitat
        self.__repo_invitat.adauga_invitat(-1, "Vlad", "Cluj")
        assert len(self.__repo_invitat.lista_invitati) == 0
        self.__repo_invitat.adauga_invitat(0, "", "Cluj")
        assert len(self.__repo_invitat.lista_invitati) == 0
        self.__repo_invitat.adauga_invitat(0, "Da", "Cluj")
        assert len(self.__repo_invitat.lista_invitati) == 0
        self.__repo_invitat.adauga_invitat(0, "daaa", "Cluj")
        assert len(self.__repo_invitat.lista_invitati) == 0
        self.__repo_invitat.adauga_invitat(0, "Vlad", "")
        assert len(self.__repo_invitat.lista_invitati) == 0
        self.__repo_invitat.adauga_invitat(0, "Vlad", "aaaa")
        assert len(self.__repo_invitat.lista_invitati) == 0
        self.__repo_invitat.adauga_invitat(0, "Vlad", "Aa")
        assert len(self.__repo_invitat.lista_invitati) == 0

        #Eveniment
        self.__repo_eveniment.adauga_eveniment(-1, "11.11.2024", "18:00", "Concert de muzica clasica")
        assert len(self.__repo_eveniment.lista_evenimente) == 0
        self.__repo_eveniment.adauga_eveniment(0, "", "18:00", "Concert de muzica clasica")
        assert len(self.__repo_eveniment.lista_evenimente) == 0
        self.__repo_eveniment.adauga_eveniment(0, "11.11.22", "18:00", "Concert de muzica clasica")
        assert len(self.__repo_eveniment.lista_evenimente) == 0
        self.__repo_eveniment.adauga_eveniment(0, "1010101010", "18:00", "Concert de muzica clasica")
        assert len(self.__repo_eveniment.lista_evenimente) == 0
        self.__repo_eveniment.adauga_eveniment(0, "11.11.2024", "", "Concert de muzica clasica")
        assert len(self.__repo_eveniment.lista_evenimente) == 0
        self.__repo_eveniment.adauga_eveniment(0, "11.11.2024", "11:1", "Concert de muzica clasica")
        assert len(self.__repo_eveniment.lista_evenimente) == 0
        self.__repo_eveniment.adauga_eveniment(0, "11.11.2024", "11111", "Concert de muzica clasica")
        assert len(self.__repo_eveniment.lista_evenimente) == 0
        self.__repo_eveniment.adauga_eveniment(0, "11.11.2024", "18:00", "")
        assert len(self.__repo_eveniment.lista_evenimente) == 0



    def teste_repo(self):
        # Test adaugare
        self.__repo_invitat.adauga_invitat(1, "Vlad", "Cluj")
        assert len(self.__repo_invitat.lista_invitati) == 1
        assert (self.__repo_invitat.lista_invitati[0].nume == "Vlad")

        # Test Stergere
        self.__repo_invitat.stergere_invitat(0)
        assert len(self.__repo_invitat.lista_invitati) == 1

        # Test modifica nume
        self.__repo_invitat.adauga_invitat(1, "Vlad", "Cluj")
        self.__repo_invitat.modifica_numele_invitatului(1, "Andrei")
        assert self.__repo_invitat.lista_invitati[1].nume == "Andrei"

        # Test modifica adresa
        self.__repo_invitat.modifica_adresa_invitatului(0, "Timisoara")
        assert self.__repo_invitat.lista_invitati[0].adresa == "Timisoara"

        # Test cautare invitat
        nume,adresa = self.__service_invitat.cautare_invitat_dupa_id(0)
        assert (nume) == "Vlad"

        # Test adaugare
        self.__repo_eveniment.adauga_eveniment(0, "11.11.2024", "18:00", "Concert de muzica clasica")
        assert len(self.__repo_eveniment.lista_evenimente) == 1
        assert self.__repo_eveniment.lista_evenimente[0].descriere == "Concert de muzica clasica"

        # Test stergere
        self.__repo_eveniment.stergere_eveniment(0)
        assert len(self.__repo_eveniment.lista_evenimente) == 0

        # Test modifica descriere
        self.__repo_eveniment.adauga_eveniment(0, "15.11.2024", "18:00", "Concert de muzica clasica")
        self.__repo_eveniment.modifica_descriere_eveniment(0, "Concert de jazz")
        assert self.__repo_eveniment.lista_evenimente[0].descriere == "Concert de jazz"

        # Test modifica timp
        self.__repo_eveniment.modifica_timp_eveniment(0, "19:00")
        assert self.__repo_eveniment.lista_evenimente[0].timp == "19:00"

        # Test modifica data
        self.__repo_eveniment.modifica_data_eveniment(0, "16.11.2024")
        assert self.__repo_eveniment.lista_evenimente[0].data == "16.11.2024"

        # Test cautare evenimt
        data,timp,descriere = self.__service_eveniment.cautare_eveniment_dupa_id(0)
        assert (data) == "16.11.2024"

        self.__repo_eveniment.lista_evenimente.clear()
        self.__repo_invitat.lista_invitati.clear()

    def teste_service(self):

        #Test legatura + adaugare service ambele
        self.__service_invitat.service_adauga(0, "Vlad", "Cluj")
        self.__service_eveniment.adauga_event(0, "11.11.2024", "18:00", "Concert de muzica clasica")
        assert len(self.__service_invitat.invitati_static_service())==1
        assert len(self.__service_eveniment.evenimente_static_service())==1
        obLegatura=RepoLegatura()
        lista_inv=self.__service_invitat.invitati_static_service()
        lista_eveniment=self.__service_eveniment.evenimente_static_service()
        obLegatura.legatura(0,0,lista_inv,lista_eveniment)
        assert obLegatura.lista_participanti[0].id_invitat==0

        #Test lista sortata invitat
        self.__repo_eveniment.adauga_eveniment(1, "11.11.2024", "18:00", "Aoncert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(2, "11.11.2024", "18:00", "Woncert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(3, "11.11.2024", "18:00", "Boncert de muzica clasica")
        obLegatura.legatura(0,1,lista_inv,lista_eveniment)
        obLegatura.legatura(0, 2, lista_inv, lista_eveniment)
        obLegatura.legatura(0, 3, lista_inv, lista_eveniment)
        lista_participanti=obLegatura.lista_participanti_static()
        lista_la_care_participa=self.__service_invitat.lista_sortata(0,lista_participanti)
        assert lista_la_care_participa[0].id_eveniment == 1

        #Test 20 la suta
        self.__repo_invitat.adauga_invitat(1, "Vlad", "Cluj")
        self.__repo_invitat.adauga_invitat(2, "Vlad", "Cluj")
        self.__repo_invitat.adauga_invitat(3, "Vlad", "Cluj")
        self.__repo_invitat.adauga_invitat(4, "Vlad", "Cluj")
        self.__repo_invitat.adauga_invitat(5, "Vlad", "Cluj")
        self.__repo_invitat.adauga_invitat(6, "Vlad", "Cluj")
        obLegatura.legatura(1, 1, lista_inv, lista_eveniment)
        obLegatura.legatura(2, 1, lista_inv, lista_eveniment)
        obLegatura.legatura(3, 1, lista_inv, lista_eveniment)
        obLegatura.legatura(4, 2, lista_inv, lista_eveniment)
        obLegatura.legatura(5, 2, lista_inv, lista_eveniment)
        obLegatura.legatura(6, 3, lista_inv, lista_eveniment)
        lista_participanti=obLegatura.lista_participanti_static()
        sorted_events, douazeciLaSuta  = self.__service_eveniment.doua_zeci_la_sute(lista_participanti)
        assert sorted_events[0][0]==1

        self.__repo_eveniment.lista_evenimente.clear()
        self.__repo_invitat.lista_invitati.clear()

        #Test participanti la max evenimente
        self.__repo_invitat.adauga_invitat(0, "Vlad", "Cluj")
        self.__repo_invitat.adauga_invitat(1, "Tudor", "Cluj")
        self.__repo_eveniment.adauga_eveniment(0, "11.11.2024", "18:00", "Concert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(1, "11.11.2024", "18:00", "Aoncert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(2, "11.11.2024", "18:00", "Woncert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(3, "11.11.2024", "18:00", "Boncert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(4, "11.11.2024", "18:00", "Aoncert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(5, "11.11.2024", "18:00", "Woncert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(6, "11.11.2024", "18:00", "Boncert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(7, "11.11.2024", "18:00", "Boncert de muzica clasica")
        obLegatura.legatura(0, 0, lista_inv, lista_eveniment)
        obLegatura.legatura(0, 1, lista_inv, lista_eveniment)
        obLegatura.legatura(0, 2, lista_inv, lista_eveniment)
        obLegatura.legatura(0, 3, lista_inv, lista_eveniment)
        obLegatura.legatura(1, 4, lista_inv, lista_eveniment)
        obLegatura.legatura(1, 5, lista_inv, lista_eveniment)
        obLegatura.legatura(1, 6, lista_inv, lista_eveniment)
        obLegatura.legatura(1, 7, lista_inv, lista_eveniment)
        lista_participanti=obLegatura.lista_participanti_static()
        topParticipantiLaEventuri=self.__service_invitat.persoana_care_participa_la_cele_mai_multe_event(lista_participanti)
        assert topParticipantiLaEventuri[0][1] == "Vlad"

        self.__repo_eveniment.lista_evenimente.clear()
        self.__repo_invitat.lista_invitati.clear()
        obLegatura.lista_participanti.clear()

        #Teste lista care participa la cel putin 2 eventuri simultan
        self.__repo_invitat.adauga_invitat(0, "Vlad", "Cluj")
        self.__repo_invitat.adauga_invitat(1, "Tudor", "Cluj")
        self.__repo_invitat.adauga_invitat(2, "Andrei", "Cluj")
        self.__repo_invitat.adauga_invitat(3, "Vasile", "Cluj")
        self.__repo_invitat.adauga_invitat(4, "Gigi", "Cluj")
        self.__repo_invitat.adauga_invitat(5, "Alex", "Cluj")
        self.__repo_eveniment.adauga_eveniment(0, "11.11.2024", "18:00", "Concert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(1, "11.11.2024", "18:00", "Aoncert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(2, "11.11.2024", "18:00", "Concert de muzica clasica")
        self.__repo_eveniment.adauga_eveniment(3, "11.11.2024", "18:00", "Aoncert de muzica clasica")

        obLegatura.legatura(0, 0, lista_inv, lista_eveniment)
        obLegatura.legatura(0, 1, lista_inv, lista_eveniment)
        obLegatura.legatura(0, 2, lista_inv, lista_eveniment)
        obLegatura.legatura(1, 0, lista_inv, lista_eveniment)
        obLegatura.legatura(1, 1, lista_inv, lista_eveniment)
        obLegatura.legatura(1, 2, lista_inv, lista_eveniment)
        obLegatura.legatura(1, 3, lista_inv, lista_eveniment)
        obLegatura.legatura(2, 1, lista_inv, lista_eveniment)
        lista_participanti=obLegatura.lista_participanti_static()
        lista_persoane=self.__service_invitat.lista_persoanelor_care_participa_la_2_evenimente_simultan(lista_participanti)
        assert len(lista_persoane)==2

        self.__repo_eveniment.lista_evenimente.clear()
        self.__repo_invitat.lista_invitati.clear()
        obLegatura.lista_participanti.clear()

        #Test stergere
        self.__service_invitat.service_adauga(0, "Vlad", "Cluj")
        self.__service_eveniment.adauga_event(0, "11.11.2024", "18:00", "Concert de muzica clasica")
        self.__service_invitat.service_delete(0)
        self.__service_eveniment.sterge_event(0)
        assert len(self.__service_invitat.invitati_static_service())==0
        assert len(self.__service_eveniment.evenimente_static_service())==0

        #Test modificari
        #invitati
        self.__service_invitat.service_adauga(0, "Vlad", "Cluj")
        self.__service_invitat.service_modifica_adresa(0,  "cluj")
        self.__service_invitat.service_modifica_nume(0,"Andrei")
        lista = self.__service_invitat.invitati_static_service()
        assert lista[0].adresa == "cluj"
        assert lista[0].nume == "Andrei"

        #evenimente
        self.__service_eveniment.adauga_event(0, "11.11.2024", "18:00", "Concert de muzica clasica")
        self.__service_eveniment.modifica_descriere(0,"descriere")
        self.__service_eveniment.modifica_data(0,"12.12.2024")
        self.__service_eveniment.modifica_timp(0,"19:00")
        lista = self.__service_eveniment.evenimente_static_service()
        assert lista[0].descriere == "descriere"
        assert lista[0].data == "12.12.2024"
        assert lista[0].timp == "19:00"

        self.__repo_eveniment.lista_evenimente.clear()
        self.__repo_invitat.lista_invitati.clear()
        obLegatura.lista_participanti.clear()