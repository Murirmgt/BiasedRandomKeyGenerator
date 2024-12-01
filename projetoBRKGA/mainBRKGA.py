# Importing the module as FBRKGA
import funcoesbrkga as FBRKGA
numeromutantes = 3
chanceelite = 0.7
numerofilhos = 3
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

populacaoinicial= FBRKGA.geravetoresaleatorios(10,10)
populacaoordenada= FBRKGA.ordenavetoresaleatorios(populacaoinicial)
####CORPO GENERICO PARTE 1-FIM

solucoes = FBRKGA.calculacustotsp_variosvetores(populacaoordenada,matriz_distancias)
populacaoordenada = FBRKGA.organizapop(populacaoinicial,populacaoordenada,solucoes)
populacaoordenada = FBRKGA.ordenadaBporFit(populacaoordenada)
elite_pop,plebe_pop = FBRKGA.SeparaBPlebeElite(populacaoordenada,3)
vetoreliterand,vetorpleberand = FBRKGA.EscolhaRandElitePleb(elite_pop,plebe_pop)
vetorfilho = FBRKGA.PopulaFilho(vetoreliterand,vetorpleberand,chanceelite)
filhoformatado = FBRKGA.organizafilho (vetorfilho,matriz_distancias)
PopulacaoMutante = FBRKGA.GeraMutantes(numeromutantes,matriz_distancias)
PopulacaoFilhos = FBRKGA.GeraFilhos(elite_pop,plebe_pop,numerofilhos,chanceelite,matriz_distancias)
GeracaoNova = FBRKGA.PopulandoNovaGeracao(PopulacaoMutante, PopulacaoFilhos, elite_pop)
print(len(GeracaoNova))
