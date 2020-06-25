# A-star---Joc---Evadarea-lui-Mormolocel

O broscuta mica de tot statea pe o frunza la fel de mica, ce plutea alene pe suprafata unui lac. Broscuta,
spre deosebire de alte surate de-ale sale nu stia sa inoate si nu-i placea apa si poate de aceea isi dorea
tare mult sa scape din lac si sa ajunga la mal. Singurul mod in care putea sa realizeze acest lucru era
sa sara din frunza in frunza.
Forma lacului poate fi aproximata la un cerc. Coordonatele frunzelor sunt raportate la centrul acestui
cerc (deci originea axelor de coordonate, adica punctul (0,0) se afla in centrul cercului). Lungimea unei
sarituri e maxim valoarea greutatii/3. Din cauza efortului depus, broscuta pierde o unitate de
energie(greutate) la fiecare saritura. Se considera ca pierderea in greutate se face in timpul saltului,
deci cand ajunge la destinatie are deja cu o unitate mai putin. Daca broscuta ajunge la greutatea 0,
atunci moare.
Pe unele frunze exista insecte, pe altele nu. Cand broscuta ajunge pe o frunza mananca o parte din
insectele gasite si acest lucru ii da energie pentru noi sarituri. In fisierul de intrare se va specifica
numarul de insecte gasite pe fiecare frunza. Daca broscuta mananca o insecta, ea creste in greutate
cu o unitate. Atentie, odata ce a mancat o parte din insectele de pe o frunza, aceasta ramane bineinteles
fara acel numar de insecte. O tranzitie e considerata a fi un salt plus consumarea insectelor de pe
frunza pe care a ajuns.
Formatul fisierului este:
raza
GreutateInitialaBroscuta
id_frunza_start
identificator_frunza_1 x1 y1 nr_insecte_1 greutate_max_1
...
identificator_frunza_n xn yn nr_insecte_n greutate_max_n
De exemplu, pentru fisierul de intrare:
7
5
id1
id1 0 0 0 5
id2 -1 1 3 8
id3 0 2 0 7
id4 2 2 3 10
id5 3 0 1 5
id6 -3 1 1 6
id7 -4 1 3 7
id8 -4 0 1 7
id9 -5 0 2 8
id10 -3 -3 4 10

Un exemplu de drum este:
1)Broscuta se afla pe frunza initiala id1(0,0). Greutate broscuta: 5
2)Broscuta sarit de la id1(0,0) la id2(-1,1). Broscuta a mancat 2 insecte. Greutate broscuta: 6
3)Broscuta sarit de la id2(-1,1) la id6(-3,1). Broscuta a mancat 1 insecte. Greutate broscuta: 6
4)Broscuta sarit de la id6(-3,1) la id8(-4,0). Broscuta a mancat 1 insecte. Greutate broscuta: 6
5)Broscuta sarit de la id8(-4,0) la id9(-5,0). Broscuta a mancat 1 insecte. Greutate broscuta: 6
6)Broscuta a ajuns la mal in 5 sarituri.
Drumurile vor trebui afisate in ordinea costului, unde costul e dat de distanta parcursa.
Outputul de mai sus arata si formatul fisierului de ieisire. Pentru fiecare pas se pune numarul de ordine
urmat de o paranteza. Pentru starea initiala si finala avem afisaj diferit asa cum se vede mai sus. Pentru
celelalte stari afisam de unde pana unde a sarit broscuta, apoi cat a mancat si care e noua greutate.
