from numpy import random
import numpy as np
#GERA UM VETOR ALEATORIO DE TAMANHO N
def geranumeroaleatorio(n):
  vetorinicial = random.rand(n)
  return vetorinicial
#ORDENA UM VETOR ALEATORIO, RETORNANDO OS INDICES ORDENADOS E ELE ORDENADO
def ordenavetoraleatorio(vetorinicial):
  return np.argsort(vetorinicial),np.sort(vetorinicial)
#GERA N VETORES ALEATORIOS DE TAMANHO N CADA
def geravetoresaleatorios(tamanhovetor,numerovetor):
  vetoresfinais = []
  for i in range(numerovetor):
    vetoresfinais.append (geranumeroaleatorio(tamanhovetor))
  return vetoresfinais
#ORDENA OS VETORES ALEATORIOS, RETORNANDO OS INDICES ORDENADOS E ELES ORDENADOS
def ordenavetoresaleatorios(vetores):
  vetoresordenados = []
  for i in range(len(vetores)):
    vetoresordenados.append (ordenavetoraleatorio(vetores[i]))
  return vetoresordenados

#ORGANIZAMOS A POPULACAO b PARA QUE:
#b[][0] é indices ordenados
#b[][1] é vetor ordenado
#b[][2] é vetor desordenado
#b[][3] é fitness
def organizapop (a,b,solucoes):
  for i in range(len(b)):
    b[i] = list(b[i])
    b[i].append(a[i])
    b[i].append(solucoes[i])
  return b
#ORDENAMOS A POPULACAO b DE MELHOR PARA PIOR
def ordenadaBporFit (b):
  b = sorted(b, key=lambda x: x[3])
  return b
#SEPARAMOS A POPULACAO b ENTRE ELITE E NÃO ELITE, PASSANDO N COMO ARGUMENTO DE  QUANTOS ELITE TEREMOS
def SeparaBPlebeElite (b,n):
  elite_b = b[:n]
  plebe_b = b[n:]
  return elite_b,plebe_b
#ESCOLHEMOS UM ELITE E UM NÃO ELITE ALEATORIO
def EscolhaRandElitePleb (elite_b,plebe_b):
  vetoreliterand=elite_b[random.randint(0,len(elite_b))][2]
  vetorpleberand=plebe_b[random.randint(0,len(plebe_b))][2]
  return vetoreliterand,vetorpleberand
#CRIAMOS UM FILHO COM CHANCE DE ESCOLHER ELITE DADA POR CHANCEELITE
def PopulaFilho (vetoreliterand,vetorpleberand, chanceelite):
  vetorfilho = []
  for i in range(len(vetorpleberand)):
    ale = random.rand()
    valorplebe = vetorpleberand[i]
    valorelite = vetoreliterand[i]
    if ale < chanceelite:
      vetorfilho.append(valorelite)
    else:
        vetorfilho.append(valorplebe)
  return vetorfilho
#ORGANIZAMOS O FILHO PARA ELE TER O MESMO FORMATO DE B:
#b[][0] é indices ordenados
#b[][1] é vetor ordenado
#b[][2] é vetor desordenado
#b[][3] é fitness
def organizafilho (vetorfilho,matriz_distancias):
  bfilho0 = ordenavetoraleatorio(vetorfilho)
  bfilho=[]
  bfilho.append(bfilho0[0])
  bfilho.append(bfilho0[1])
  bfilho.append(vetorfilho)
  solucaofilho = calculacustotsp(bfilho0,matriz_distancias)
  bfilho.append(solucaofilho)
  return bfilho
#GERAMOS A PARTE DA POPULACAO MUTANTE, APENAS PRECISANDO DE QUANTOS MUTANTES TEREMOS, DADO POR PMUTANTE
def GeraMutantes (pMutante,matriz_distancias):
  Mutantes = geravetoresaleatorios(10,pMutante)
  MutantesOrdenados = ordenavetoresaleatorios(Mutantes)
  SolucoesMutantes=calculacustotsp_variosvetores(MutantesOrdenados,matriz_distancias)
  organizapop(Mutantes,MutantesOrdenados,SolucoesMutantes)
  return MutantesOrdenados
#GERAMOS FILHOS A PARTIR DE ELITEB E PLEBEB, NUM_FILHOS VEZES
def GeraFilhos(elite_b, plebe_b, num_filhos,chanceelite,matriz_distancias):
    bfilhos = []
    for _ in range(num_filhos):
        vetoreliterand,vetorpleberand=EscolhaRandElitePleb(elite_b,plebe_b)
        vetorfilho = PopulaFilho(vetoreliterand, vetorpleberand,chanceelite)
        bfilho = organizafilho(vetorfilho,matriz_distancias)
        bfilhos.append(bfilho)
    return bfilhos
#PEGAMOS A POPULACAO DE MUTANTES, BFILHOS QUE É A POPULACAO DE B GERADA E ELITE_B QUE É A ELITE DA GERAÇÃO PASSADA
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

###############DEPENDE DO PROBLEMA
###############TSP
#CALCULO DA FUNCAO TSP, É UMA DAS CAIXAS QUE MUDA A CADA TIPO DE PROBLEMA
def calculacustotsp(b,matriz_distancias):
    custototal = 0
    for i in range(len(b[0]) - 1):
        lista = b[0]
        L = matriz_distancias[lista[i]][lista[i + 1]]
        custototal += L
    custototal += matriz_distancias[lista[-1]][lista[0]]
    return custototal
#CALCULO DA FUNCAO TSP PARA VARIOS VETORES, É UMA DAS CAIXAS QUE MUDA A CADA TIPO DE PROBLEMA
def calculacustotsp_variosvetores(vetoresordenados,matriz_distancias):
    custos_totais = []
    for b in vetoresordenados:
        custototal = 0
        lista = b[0]
        for i in range(len(lista) - 1):
            custototal += matriz_distancias[lista[i]][lista[i + 1]]
        custototal += matriz_distancias[lista[-1]][lista[0]]
        custos_totais.append(custototal)
    return custos_totais
#########################
