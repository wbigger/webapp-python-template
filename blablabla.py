qualche_lista = [1,2,3,4]

altra_lista = ["ciao","buongiorno"]

lista_boolean = [True,False,False]


class GiornoAppuntamento:
    def __init__(self,nomeGiorno):
        self.nome = nomeGiorno
        self.ora_00 = False
        self.ora_01 = False

        self.ora = []

        for idx in range(0,24):
            self.ora[idx] = False



lista_giorni = [
    GiornoAppuntamento("martedi"),
    GiornoAppuntamento("mercoledi"),
    GiornoAppuntamento("giovedi"),
    GiornoAppuntamento("venerdi"),
    GiornoAppuntamento("sabato")
    ]

