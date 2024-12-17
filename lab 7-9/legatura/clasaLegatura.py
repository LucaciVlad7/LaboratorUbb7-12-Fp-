from business.service_evenimente import serviceEvenimente

class LegaturaInvtEvnt:
    def __init__(self,id_invitat,nume_invitat,id_eveniment,descriere_eveniment):
        self.id_invitat=id_invitat
        self.nume_invitat=nume_invitat
        self.id_eveniment=id_eveniment
        self.descriere_eveniment=descriere_eveniment
