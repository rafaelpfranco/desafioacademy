# Autor: Rafael Pinheiro Franco Gouveia
# Entrada: Um arquivo .json com n alunos e m ciclos. Também é pedido a quantidade de membros por grupos.
# Saída: Um ciclo de alunos otimizados
# Lógica: Primeiro passo é transformar a entrada json em grafo,
# onde os alunos são os nós e o peso dos vértices são a quantidade
# de vezes que o aluno A esteve em um grupo com o Aluno B. 
# Segundo passo é escolher o próximo ciclo então para isso é 
# definido que o primeiro aluno sempre estará no primeiro grupo,
# para escolher o próximo aluno é checado o menor peso desse aluno
# com todos os outros e escolhemos o menor, caso tenha vários pesos
# iguais escolhemos o primeiro menor, para escolher o terceiro indivíduo
# verificamos o peso do primeiro aluno com todos os outros mais o peso
# do segundo alunos com todos os outros, o que significa que estamos
# escolhendo a melhor escolha pensando em quem já está no grupo e isso
# é feito até completarmos o grupo.

from tabulate import tabulate as tb
import json
import numpy as np
import math as mt

# abre a entrada de alunos
f = open("ciclos.json")
ciclos = json.load(f)
f.close()

# Aloco todos os alunos uma lista
alunos = []
for grupo in ciclos['ciclo1']:
  for aluno in grupo:
    alunos = alunos + [aluno]

# Inicializa a matriz de alunos x alunos com 0, onde cada elemento é o peso
pesos = {alunos[i]: {alunos[j]: 0 for j in range(len(alunos))} for i in range(len(alunos))}

# Popula a matriz de aluno com o peso das arestas do grafo
for c in ciclos:
  for grupo in ciclos[c]: 
    for aluno1 in grupo:
      for aluno2 in grupo:
        pesos[aluno1][aluno2] += 1

tamGrupo = -1
while tamGrupo <= 0 or tamGrupo > len(alunos):
  tamGrupo = int(input("Digite o tamanho do grupo do próximo ciclo:"))
  if tamGrupo <= 0 or tamGrupo > len(alunos):
    print("Entrada Incorreta! Por favor digite um valor válido!")
    
# Quando a divisão não é inteira, pega-se o proximo valor inteiro
qntdGrupos = mt.ceil(len(alunos)/int(tamGrupo))

# Inicializa o uma lista de listas com a quantidade de grupos solicitados
grupos = []
for i in range(qntdGrupos):
  grupos.append([])

for g in grupos:
  # Inicializa o peso de todos os grupos em zero
  pesoGrupo = {alunos[j]: 0 for j in range(len(alunos))}
  while len(g) < tamGrupo and len(alunos) > 0:
    min = alunos[0]
    minizou = False
    #  seta o mínimo para o primeiro aluno que não tá no grupo
    for j in range(len(alunos)):
      if alunos[j] not in g and not minizou :
        min = alunos[j]
        minizou = True
    # verifica qual aluno que não está no grupo e tem o menor peso com os alunos escolhidos
    for a in alunos:
      if a not in g:
        if len(g) > 0:
          pesoGrupo[a] = pesoGrupo[g[-1]]
        for i in range(len(g)):
          pesoGrupo[a] +=  pesos[a][g[i]]
        if pesoGrupo[a] < pesoGrupo[min]:
          min = a
    g.append(min)
    alunos.remove(min)
print(tb(grupos))  
