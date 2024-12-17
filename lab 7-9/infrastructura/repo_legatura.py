from legatura.clasaLegatura import LegaturaInvtEvnt
from exceptii.erori import RepoError

class RepoLegatura:
    def __init__(self):
        self.lista_participanti = []

    def legatura(self, id_invitat,  id_eveniment,lista_invitati,lista_evenimente ):
        erori = ""
        nume = ""
        descriere = ""
        for lista in lista_invitati:
            if lista.id_invitat == id_invitat:
                nume += lista.nume
        if nume == "":
            erori += "Invitatul nu exita\n"
        for lista in lista_evenimente:
            if lista.id_eveniment == id_eveniment:
                descriere += lista.descriere
        if descriere == "":
            erori += "Evenimentul nu exista\n"
        if erori != "":
            raise ValueError(erori)
        nou = LegaturaInvtEvnt(id_invitat, nume, id_eveniment, descriere)
        self.lista_participanti.append(nou)

    def lista_participanti_static(self):
        return self.lista_participanti