""" 243 FILIP IOANA ALEXANDRA
PB 7 - EVADAREA LUI MORMOCEL """

from math import sqrt
import time
import io

# DATE GLOBALE

# liste fisiere input/output
date_input = ["input1.txt", "input2.txt", "input3.txt", "input4.txt"]
date_output = ["output1.txt", "output2.txt", "output3.txt", "output4.txt"]
# datele citite din fisierele de input
raza = 0    # raza este distanta de la centru(0,0) la mal
greutate_init = 0
id_frunza_start = ""
frunze = []
frunza_start = []
# euristica folosita
opt_h = -1

# CIRIREA DATELOR DIN FISIER
# primeste ca parametru indicele fisierului din lista de inputuri
def citire_date_input(i):

    with open(date_input[i]) as fin:

        global raza, greutate_init, frunza_start, frunze, id_frunza_start

        raza = int(next(fin))
        greutate_init = int(next(fin))
        id_frunza_start = fin.readline()
        id_frunza_start = id_frunza_start.replace('\n','')

        line = fin.readline()

        while(line):

            date = line.split()
            date[1] = int(date[1])
            date[2] = int(date[2])
            date[3] = int(date[3])
            date[4] = int(date[4])
            frunze.append(date)

            if date[0] == id_frunza_start:
                 frunza_start = date

            line = fin.readline()

# SCRIEREA DATELOR IN FISIER
# primeste ca parametrii: lista open(frunzele pe care sarim pt a ajunge la mal), nod_curent(frunza pe care sarim
# ultima data inainte de a ajunge la mal), i(indicele fisierului din lista de inputuri) si timp(timpul pt rularea
# fiecarei euristici, pe inputul i)
def scriere_date_output(open, nod_curent, i, timp):

    with io.open(date_output[i], "a+", encoding="utf8") as out:

        if opt_h == 1:
            out.write("------------------ Concluzie input" + str(i+1) + ".txt-----------------------\n\n")

        out.write("------------------ Euristica " + str(opt_h) + " cu timpul " + str(timp) + " -----------------------\n")

        if (len(open) == 0):
            out.write("Broscuta nu poate ajunge la mal!\n\n")

        else:

            numar_sarituri = 1 # luam in considerare ultima saritura, pe mal
            sarituri = nod_curent.drum_arbore()

            for saritura in sarituri:

                frunza = saritura.nod_graf.info
                greutate = saritura.nod_graf.greutate

                if frunza == frunza_start:

                    out.write("Broscuta se afla pe frunza initiala " + str(frunza[0]) + "(" + str(frunza[1]) + ","
                              + str(frunza[2]) + "). Greutate broscuta : " + str(greutate) + "\n")
                    greutate_ant = greutate

                else:

                    numar_sarituri = numar_sarituri + 1
                    insecte = greutate - greutate_ant + 1
                    greutate_ant= greutate

                    out.write("Broscuta a sarit la " + str(frunza[0]) + "(" + str(frunza[1]) + "," + str(frunza[2])
                              + "). Broscuta a mancat " + str(insecte) +" insecte. Greutate Broscuta :" + str(greutate) + "\n")

            out.write("Broscuta a ajuns la mal in " + str(numar_sarituri) + " sarituri." + "\n\n")


class Nod:

    def __init__(self, frunza, greutate):
        self.info = frunza
        self.greutate = greutate
        self.h = self.calcul_h()
        self.distanta_mal = self.calcul_distanta_mal()

    def __str__(self):
        return "({}, h={})".format(self.info, self.h)

    def __repr__(self):
        return f"({self.info}, h={self.h})"

    def calcul_h(self):

        # euristica distanta pana la mal
        # este consistenta deoarece cu cat ne apropiem mai mult de mal, cu atat distanta scade
        if opt_h == 1:
            distanta_fata_de_centru = sqrt((self.info[1] - 0) ** 2 + (self.info[2] - 0) ** 2)
            h = raza - distanta_fata_de_centru

        # euristica nr de frunze mai apropiate de mal(nr de eventuali succesori)
        # este consistenta deoarece cu cat ne apropiem mai mult de mal, cu atat nr de frunze mai apropiate de mal descreste
        elif opt_h == 2:
            h = 0
            for f in frunze:
                # verific daca sunt mai apropiate de mal decat nodul curent prin compararea coordonatelor x si y
                if f != self.info and (abs(f[1]) > abs(self.info[1]) or abs(f[2]) > abs(self.info[2])):
                    h = h + 1

        # medie a diferentelor (raza,x) si (raza,y)
        # este consistenta deoarece cu cat ne apropiem mai mult de mal, cu atat valorile absolute ale coordonatelor(x,y)
        # cresc si deci media diferentelor scade
        elif opt_h == 3:
            h = ((raza - abs(self.info[1])) + (raza - abs(self.info[2]))) / 2

        # euristica neadmisibila
        # luandu-ne dupa greutate ne dam seama cate sarituri mai putem face pana broscuta va muri, deci nr maxim de
        # sarituri pe care il mai facem pana la mal, daca ea poate ajunge acolo
        # euristica ar fi consistenta doar daca nu ar mai exista insecte pe frunzele succesori
        # deci euristica nu descreste daca gasim insecte pe urmatoarele frunze, deci nu este consistenta si nici admisibila
        elif opt_h == 4:
            h = self.greutate

        return h

    def calcul_distanta_mal(self):

        # distanta nodului curent pana la mal, de care ne folosim in expandeaza
        frunza = self.info
        x = frunza[1]
        y = frunza[2]
        distanta_fata_de_centru = sqrt((x - 0) ** 2 + (y - 0) ** 2)
        distanta = raza - distanta_fata_de_centru

        return distanta


class Arc:

    def __init__(self, capat, varf, cost):
        self.capat = capat	# de unde pleaca muchia
        self.varf = varf	# unde ajunge muchia
        self.cost = cost	# cosul g al muchiei


class Problema:

    def __init__(self):
        self.frunze = frunze
        self.greutate = greutate_init
        self.nod_start = Nod(frunza_start, greutate_init)

    def cauta_nod_nume(self, info):
        """Stiind doar informatia "info" a unui nod,
        trebuie sa returnati fie obiectul de tip Nod care are acea informatie,
        fie None, daca nu exista niciun nod cu acea informatie."""
        for nod in self.noduri:
            if info == nod.info:
                return nod
        return None


""" Clase folosite in algoritmul A* """


class NodParcurgere:
    """O clasa care cuprinde informatiile asociate unui nod din listele open/closed
        Cuprinde o referinta catre nodul in sine (din graf)
        dar are ca proprietati si valorile specifice algoritmului A* (f si g).
        Se presupune ca h este proprietate a nodului din graf
    """

    problema = None  # atribut al clasei (se suprascrie jos in __main__)

    def __init__(self, nod_graf, parinte=None, g=0, f=None):
        self.nod_graf = nod_graf  # obiect de tip Nod
        self.parinte = parinte  # obiect de tip NodParcurgere
        self.g = g  # costul drumului de la radacina pana la nodul curent
        if f is None:
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f

    def drum_arbore(self):
        """
            Functie care calculeaza drumul asociat unui nod din arborele de cautare.
            Functia merge din parinte in parinte pana ajunge la radacina
        """
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
        return drum

    def contine_in_drum(self, nod):
        """
            Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
            Verificarea se face mergand din parinte in parinte pana la radacina
            Se compara doar informatiile nodurilor (proprietatea info)
            Returnati True sau False.

            "nod" este obiect de tip Nod (are atributul "nod.info")
            "self" este obiect de tip NodParcurgere (are "self.nod_graf.info")
        """
        nod_curent = self
        while nod_curent:
            if nod.info == nod_curent.nod_graf.info:
                return True
            nod_curent = nod_curent.parinte
        return False


    def expandeaza(self):
        """Pentru nodul curent (self) parinte, trebuie sa gasiti toti succesorii (fiii)
        si sa returnati o lista de tupluri (nod_fiu, cost_muchie_tata_fiu),
        sau lista vida, daca nu exista niciunul.
        (Fiecare tuplu contine un obiect de tip Nod si un numar.)
        """
        lista_succesori = []

        # pentru fiecare frunza(diferita de cea pe care ne aflam si aflata mai aproape de mal) vedem daca putem sa
        # sarim pe ea, dupa ce manacam suficiente insecte de pe frunza curenta
        for i in range(0, len(frunze)):

            # datele frunzei pe care ne aflam
            frunza_curenta = self.nod_graf.info
            greutate = self.nod_graf.greutate
            distanta_mal_curenta = self.nod_graf.distanta_mal

            # daca gasim o frunza diferita de frunza curenta
            if frunza_curenta != frunze[i]:

                frunza_noua = frunze[i]

                # distanta dintre frunza curenta si frunza pe care vreau sa sar
                distanta_frunze = sqrt(
                    (frunza_noua[1] - frunza_curenta[1]) ** 2 + (frunza_noua[2] - frunza_curenta[2]) ** 2)

                # distanta de la frunza noua la mal
                x = frunza_noua[1]
                y = frunza_noua[2]
                distanta_fata_de_centru = sqrt((x - 0) ** 2 + (y - 0) ** 2)
                distanta_mal_noua = raza - distanta_fata_de_centru

                # daca distanta pana la mal a frunzei noi este mai mica decat distanta curenta pana la mal
                if distanta_mal_noua < distanta_mal_curenta:

                    # mancam insectele de pe frunza curenta
                    insecte_mancate = 0
                    # atat timp cat mai sunt frunze de mancat, nu depasim greuatea maxima de pe frunza curenta
                    # si cat timp nu am ajuns la greutatea necesar pt a putea sari pe frunza noua
                    while frunza_curenta[3] > 0 and greutate <= frunza_curenta[4] and distanta_frunze > greutate/3:

                        greutate = greutate + 1
                        frunza_curenta[3] = frunza_curenta[3] - 1
                        insecte_mancate = insecte_mancate + 1

                    # daca intr-un final am putut manca suficiente insecte pt a sari pe frunza noua, inseamna ca
                    # aceasta este succesor
                    if distanta_frunze <= greutate / 3:

                        greutate = greutate - 1 # scadem din greutate cosul sariturii
                        lista_succesori.append((Nod(frunza_noua, greutate), 1))

        return lista_succesori


    def test_scop(self):
        # pentru ca testul_scop sa fie indeplinit inseamna ca de pe frunza curenta putem sari pe mal

        # datele frunzei curente
        frunza = self.nod_graf.info
        greutate = self.nod_graf.greutate
        distanta_pana_la_mal = self.nod_graf.distanta_mal

        # mancam frunzele de pe frunza curenta, pt a creste lungimea sariturii pe care o putem face
        while frunza[3] > 0 and greutate <= frunza[4] and distanta_pana_la_mal > greutate/3:
            greutate = greutate + 1
            frunza[3] = frunza[3] - 1

        # actualizam datele frunzei curente
        self.nod_graf.info[3] = frunza[3]
        self.nod_graf.greutate = greutate

        # returnam val de adevar ca conditiei sariturii pana la mal
        return distanta_pana_la_mal <= greutate / 3

    def __str__(self):
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
        return f"({self.nod_graf}, parinte={parinte}, f={self.f}, g={self.g})"


""" Algoritmul A* """


def str_info_noduri(l):
    """
        o functie folosita strict in afisari - poate fi modificata in functie de problema
    """
    sir = "["
    for x in l:
        sir += str(x) + "  "
    sir += "]"
    return sir


def afis_succesori_cost(l):
    """
        o functie folosita strict in afisari - poate fi modificata in functie de problema
    """
    sir = ""
    for (x, cost) in l:
        sir += "\nnod: " + str(x) + ", cost arc:" + str(cost)

    return sir


def in_lista(l, nod):
    """
    lista "l" contine obiecte de tip NodParcurgere
    "nod" este de tip Nod
    """
    for i in range(len(l)):
        if l[i].nod_graf.info == nod.info:
            return l[i]
    return None


def a_star():
    rad_arbore = NodParcurgere(NodParcurgere.problema.nod_start)
    open = [rad_arbore]  # open va contine elemente de tip NodParcurgere
    closed = []  # closed va contine elemente de tip NodParcurgere

    while len(open) > 0:

        nod_curent = open[0]
        closed.append(nod_curent)

        if nod_curent.test_scop():  # daca nodul curent este nod scop
            break

        open.pop(0)

        succesori_nod_curent = nod_curent.expandeaza()  # succesorii nodului curent

        for s in succesori_nod_curent:
            # s este format din s[0] = nodul si s[1] = costul

            # daca s nu apartine drumului lui nod_curent
            if nod_curent.contine_in_drum(s[0]) == False:

                # daca nodul s[0] e in open returneaza s[0]
                nod_in_open = in_lista(open, s[0])
                # g-ul si f-ul pt s
                g_s = nod_curent.g + s[1]
                f_s = g_s + s[0].h

                # daca s se afla in closed
                if nod_in_open:
                    # daca f-ul nodului din open e mai mare decat f-ul gasit pt s
                    if nod_curent.f > f_s:
                        # seteaza parintele, g-ul si f-ul pt s
                        s[0].parinte = nod_curent
                        s[0].g = g_s
                        s[0].f = f_s

                # daca s a fost expandat (se afla in closed)
                nod_in_closed = in_lista(closed, s[0])
                if nod_in_closed:
                    s[0].parinte = nod_curent
                    s[0].g = g_s
                    s[0].f = f_s

                else:
                    nod_cautare = NodParcurgere(nod_graf=s[0], parinte=nod_curent, g=g_s)
                    open.append(nod_cautare)

        # sortez crescator dupa f, apoi descrescator dupa g
        open.sort(key=lambda nod: (nod.f, -nod.g))

    return open, nod_curent

if __name__ == "__main__":

    # pr fiecare fisier de input
    for i in range(len(date_input)):

        # aplicam toate euristicile
        for j in range(4):

            citire_date_input(i)
            opt_h = j + 1

            start = time.time()
            problema = Problema()
            NodParcurgere.problema = problema
            lista, nod = a_star()
            stop = time.time()

            timp = stop - start
            scriere_date_output(lista, nod, i, timp)

        # dupa fiecare fisier de input trebuie sa actualizam datele globale de intrare
        raza = 0
        greutate_init = 0
        id_frunza_start = ""
        frunze = []
        frunza_start = []



