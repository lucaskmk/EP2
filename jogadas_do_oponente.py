import random as rd
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    l = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            l.append([(linha+i), coluna])
        if orientacao == 'horizontal':
            l.append([linha, (coluna+i)])
    if navio in frota.keys():
        frota[navio] += [l]
    else:
        frota[navio] = [l]
    return frota
#================================================================    
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    validacao = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            validacao.append([(linha+i), coluna])
            if (linha+i) > 9:
                return False
        if orientacao == 'horizontal':
            validacao.append([linha, (coluna+i)])
            if (coluna+i) > 9:
                return False
    for barco, cordenadas_geral in frota.items():
        for cordenada_umbarco in cordenadas_geral:
            for posicao in cordenada_umbarco:
                for itemvalido in validacao:
                    if itemvalido == [posicao[0],posicao[1]]:
                        return False
    return True
#================================================================
def pergunta(navio, tamanho):
    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, tamanho))
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if navio == "submarino":
        orientacao = 'vertical'
    else:
        orientacao = int(input('[1] Vertical [2] Horizontal >'))
    if orientacao == 1:
        orientacao = 'vertical'
    elif orientacao == 2:
        orientacao = 'horizontal'
# se for invalido
    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
        return pergunta(navio, tamanho)
# se for valida ja adiciona
    else:
        preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)
        return ''
        
#================================================================
tamanho = ''
for navio in frota:
    if navio == "porta-aviões":
        tamanho = 4
        pergunta(navio, tamanho)

    if navio == "navio-tanque":
        tamanho = 3
        for i in range(2):
            pergunta(navio, tamanho)

    if navio == "contratorpedeiro":
        tamanho = 2
        for i in range(3):
            pergunta(navio, tamanho)

    if navio == "submarino":
        tamanho = 1
        for i in range(4):
            pergunta(navio, tamanho)


#==========================================




def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(frota):
    tabuleiro = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(10):
        tabuleiro[i] += [0 for x in range(10)]
    for barco, cordenadas_geral in frota.items():
        for cordenada_umbarco in cordenadas_geral:
            for posicao in cordenada_umbarco:
                for T in range(10):
                    for j in range(10):
                        if [T,j] == [posicao[0],posicao[1]]:
                            tabuleiro[T][j] = 1
    return tabuleiro
    
def afundados(frota, tabuleiro):
    total_afundados = 0
    for barco, cordenadas_geral in frota.items():
        for cordenada_umbarco in cordenadas_geral:
            afundo = 0
            for posicao in cordenada_umbarco:
                if tabuleiro[posicao[0]][posicao[1]] == 'X':
                    afundo += 1
                if afundo == len(cordenada_umbarco):
                    total_afundados += 1
    return total_afundados
#==============================================================
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
#==============================================================
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'
    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    print(texto)
    return texto
#==========================================
jogando = True
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
lposições = []
nvalidos = ['0','1','2','3','4','5','6','7','8','9']

while jogando == True:
    monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    linha = input('informe um número entre 0 e 9.')
    while linha not in nvalidos:
        print('Linha inválida!')
        linha = input('informe um número entre 0 e 9.')
        if linha in nvalidos:
            linha = int(linha)
            break
    coluna = input('informe um número entre 0 e 9.')
    while coluna not in nvalidos:
        print('Coluna inválida!')
        coluna = input('informe um número entre 0 e 9.')
        if coluna in nvalidos:
            coluna = int(coluna)
            break
    linha = int(linha)
    coluna = int(coluna)  
    if [linha, coluna] not in lposições:
        lposições.append([linha, coluna])
        faz_jogada(tabuleiro_oponente, linha, coluna)
    else:
        print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha, coluna))
#========CHECAR SE AFUNDOU TODOS==================
    nafundados = afundados(frota_oponente, tabuleiro_oponente)
    atk_oponente = []
    if nafundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    elif nafundados < 10:
        linha = rd.randint(0, 9)
        coluna = rd.randint(0, 9)
        if [linha, coluna] not in atk_oponente:
            atk_oponente.append([linha, coluna])
            print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha, coluna))
            faz_jogada(tabuleiro_jogador, linha, coluna)
        else:
            while True:
                linha = rd.randint(0, 9)
                coluna = rd.randint(0, 9)
                if [linha, coluna] not in atk_oponente:
                    atk_oponente.append([linha, coluna])
                    print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha, coluna))
                    faz_jogada(tabuleiro_jogador, linha, coluna)
                    break
        nselfafundados = afundados(frota, tabuleiro_jogador)
        if nselfafundados >= 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
        
#==========================================
