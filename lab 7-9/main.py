from testate.teste import Teste
from validare.validare_eveniment import ValidatorEveniment
from validare.validare_invitat import ValidatorInvitat
from infrastructura.repo_invitat import *
from infrastructura.repo_eveniment import RepoEvenimente, RepoFileEvent
from business.service_evenimente import serviceEvenimente
from business.service_invitati import serviceInvitat
from prezentare.consola import Consola

def file_or_manual():
    while True:
        print("1) Introduceti datele manual")
        print("2) Date din fisier")
        try:
            alegere = int(input("Alegeti optiunea: "))
            if alegere in [1,2]:
                break
            else:
                print("Optiunea introdusa nu exista")
        except ValueError as ve:
            print(ve)
    if alegere==2:
        return RepoFileInv("infrastructura/invitat.txt"),RepoFileEvent("infrastructura/event.txt")
    elif alegere==1:
        return RepoInvitat(),RepoEvenimente()


teste = Teste()
teste.ruleaza_toate_testele()

#Analiza complexitate in service invitati la cautare_invitat_dupa_id
#adaugare si stergere recursive la evenimente
#persoana_care_participa_la_cele_mai_multe_event in service invitati are selection sort
#lista_persoanelor_care_participa_la_2_evenimente_simultan in service invitati are shake sort

def main():
    repo_invitat,repo_eveniment=file_or_manual()
    validator_invitat=ValidatorInvitat()
    service_invitat=serviceInvitat(validator_invitat,repo_invitat)
    validator_eveniment=ValidatorEveniment()
    service_eveniment=serviceEvenimente(validator_eveniment,repo_eveniment)
    consola=Consola(service_invitat,service_eveniment)
    consola.run()

if __name__ == "__main__":
    main()
