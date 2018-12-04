from carta import *
r1 = Rodada_1()

arquetipoID = [1, 2, 3]
animalID = [4, 5, 6]
metaforaID = [7, 8, 9, 10, 11, 12, 13]

arquetipoT = ['O Montro', 'O Hacker', 'O Comum']
animalT = ['Black Jellyfish', 'Black Elephant', 'Black Swan']
metaforaT = ['Correntes do presente', 'Perdido na Multidão', 'Pacto com o Demônio', 'Fire', 'ice', 'spark', 'explosion']

arquetipoID[:] = arquetipoT[:]
animalID[:] = animalT[:]
metaforaID[:] = metaforaT[:]

lista = []

a = input('Arquetipo: \n').split(",")
sq = input('Status-Quo: \n').split(",")
an = input('Animal: \n').split(",")
cr = input('Crise: \n').split(",")
j = input('Jornada: \n').split(",")
c = input('Conflito: \n').split(",")
nsq = input('Novo Status-Quo: \n').split(",")

print(lista)

r1.append_a(lista[0])
r1.append_sq(lista[1])
r1.append_an(lista[2])
r1.append_c(lista[3])
r1.append_j(lista[4])
r1.append_cr(lista[5])
r1.append_nsq(lista[6])
r1.print_states()