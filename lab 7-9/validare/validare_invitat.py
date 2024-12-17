from exceptii.erori import ValidationError
#se apeleaza in service

class ValidatorInvitat:

    def valideaza_invitat(self,invitat):
        erori = ""
        if invitat.id_invitat<0:
            erori+= "id invitat invalid!\n"
        if invitat.nume=="" or len(invitat.nume)<3 or invitat.nume[0].isupper()==False:
            erori+="Nume invalid\n"
        if invitat.adresa=="" or len(invitat.adresa)<3 or invitat.adresa[0].isupper()==False:
            erori+="Adresa invalida\n"
        if len(erori)>0:
            raise ValidationError(erori)
