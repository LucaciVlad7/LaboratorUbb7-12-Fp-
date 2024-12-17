from exceptii.erori import ValidationError

class ValidatorEveniment:

    def valideaza_eveniment(self,eveniment):
        erori = ""
        if eveniment.id_eveniment<0:
            erori+= "id student invalid!\n"
        data=eveniment.data
        lista=data.split(".")
        if eveniment.data=="" or len(eveniment.data)!=10 or len(lista)!=3:
            erori+= "data este invalida\n"
        timp=eveniment.timp
        lista=timp.split(":")
        if eveniment.timp=="" or len(eveniment.timp)!=5 or len(lista)!=2:
            erori+="timpul este invalid\n"
        if eveniment.descriere=="":
            erori+="descrierea este invalida\n"
        if len(erori)>0:
            raise ValidationError(erori)
