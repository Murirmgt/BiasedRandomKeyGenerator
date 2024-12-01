from numpy import random
import numpy as np
#############################################
def geranumeroaleatorio(n):

  vetorinicial = random.rand(n)
  return vetorinicial
def ordenavetoraleatorio(vetorinicial):
  return np.argsort(vetorinicial),np.sort(vetorinicial)
#############################################

def geravetoresaleatorios(tamanhovetor,numerovetor):
  vetoresfinais = []
  for i in range(numerovetor):
    vetoresfinais.append (geranumeroaleatorio(tamanhovetor))
  return vetoresfinais

def ordenavetoresaleatorios(vetores):
  vetoresordenados = []
  for i in range(len(vetores)):
    vetoresordenados.append (ordenavetoraleatorio(vetores[i]))
  return vetoresordenados


#############################################
a= geravetoresaleatorios(10,10)
b = ordenavetoresaleatorios(a)
###TSP###

matriz_distancias = [
    [0, 55, 51, 43, 52, 90, 47, 40, 88, 32],
    [55, 0, 47, 24, 75, 51, 23, 64, 40, 43],
    [51, 47, 0, 38, 18, 38, 62, 89, 72, 65],
    [43, 24, 38, 0, 50, 54, 64, 56, 72, 22],
    [52, 75, 18, 50, 0, 56, 3, 41, 64, 57],
    [90, 51, 38, 54, 56, 0, 33, 53, 44, 35],
    [47, 23, 62, 64, 3, 33, 0, 62, 54, 67],
    [40, 64, 89, 56, 41, 53, 62, 0, 62, 64],
    [88, 40, 72, 72, 64, 44, 54, 62, 0, 55],
    [32, 43, 65, 22, 57, 35, 67, 64, 55, 0]
]
def calculacustotsp(b):
    custototal = 0
    for i in range(len(b[0]) - 1):
        lista = b[0]
        L = matriz_distancias[lista[i]][lista[i + 1]]
        custototal += L
    custototal += matriz_distancias[lista[-1]][lista[0]]
    return custototal
def calculacustotsp_variosvetores(vetoresordenados):
    custos_totais = []
    for b in vetoresordenados:
        custototal = 0
        lista = b[0]
        for i in range(len(lista) - 1):
            custototal += matriz_distancias[lista[i]][lista[i + 1]]
        custototal += matriz_distancias[lista[-1]][lista[0]]
        custos_totais.append(custototal)
    return custos_totais
solucoes = calculacustotsp_variosvetores(b)
######TSP FIM######

def organizapop (a,b,solucoes):
  for i in range(len(b)):
    b[i] = list(b[i])
    b[i].append(a[i])
    b[i].append(solucoes[i])
  return b

organizapop(a,b,solucoes)
#b[][0] é indices ordenados
#b[][1] é vetor ordenado
#b[][2] é vetor desordenado
#b[][3] é fitness
def ordenadaBporFit (b):
  b = sorted(b, key=lambda x: x[3])
  return b

b = ordenadaBporFit(b)

def SeparaBPlebeElite (b):
  elite_b = b[:3]
  plebe_b = b[3:]
  return elite_b,plebe_b

elite_b,plebe_b = SeparaBPlebeElite(b)

def EscolhaRandElitePleb (elite_b,plebe_b):
  vetoreliterand=elite_b[random.randint(0,len(elite_b))][2]
  vetorpleberand=plebe_b[random.randint(0,len(plebe_b))][2]
  return vetoreliterand,vetorpleberand
vetoreliterand,vetorpleberand = EscolhaRandElitePleb(elite_b,plebe_b)

def PopulaFilho (vetoreliterand,vetorpleberand):
  vetorfilho = []
  for i in range(len(vetorpleberand)):
    ale = random.rand()
    valorplebe = vetorpleberand[i]
    valorelite = vetoreliterand[i]
    if ale < 0.7:
      vetorfilho.append(valorelite)
    else:
        vetorfilho.append(valorplebe)
  return vetorfilho


vetorfilho = PopulaFilho(vetoreliterand,vetorpleberand)

#b[][0] é indices ordenados
#b[][1] é vetor ordenado
#b[][2] é vetor desordenado
#b[][3] é fitness
def organizafilho (vetorfilho):
  bfilho0 = ordenavetoraleatorio(vetorfilho)
  bfilho=[]
  bfilho.append(bfilho0[0])
  bfilho.append(bfilho0[1])
  bfilho.append(vetorfilho)
  solucaofilho = calculacustotsp(bfilho0)
  bfilho.append(solucaofilho)
  return bfilho
bfilho = organizafilho (vetorfilho)

def GeraMutantes (pMutante):
  Mutantes = geravetoresaleatorios(10,pMutante)
  MutantesOrdenados = ordenavetoresaleatorios(Mutantes)
  SolucoesMutantes = calculacustotsp_variosvetores(MutantesOrdenados)
  organizapop(Mutantes,MutantesOrdenados,SolucoesMutantes)
  return MutantesOrdenados

PopulacaoMutante = GeraMutantes(3)

def GeraFilhos(elite_b, plebe_b, num_filhos):
    bfilhos = []
    for _ in range(num_filhos):
        vetoreliterand,vetorpleberand=EscolhaRandElitePleb(elite_b,plebe_b)
        vetorfilho = PopulaFilho(vetoreliterand, vetorpleberand)
        bfilho = organizafilho(vetorfilho)
        bfilhos.append(bfilho)
    return bfilhos

bfilhos = GeraFilhos(elite_b,plebe_b,10)


def PopulandoNovaGeracao(MutantesOrdenados, bfilhos, elite_b):
    NovaGenPop = []

    # Adiciona mutantes
    for mutante in MutantesOrdenados:
        NovaGenPop.append(mutante)
    for bfilho in bfilhos:
        NovaGenPop.append(bfilho)
    for elite in elite_b:
        NovaGenPop.append(elite)
    return NovaGenPop

GeracaoNova = PopulandoNovaGeracao(PopulacaoMutante, bfilhos, elite_b)
for i in range(len(GeracaoNova)):
  print(GeracaoNova[i][3])
print("\n")
GeracaoNova = ordenadaBporFit(GeracaoNova)
for i in range(len(GeracaoNova)):
  print(GeracaoNova[i][3])
