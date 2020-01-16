# -*- coding: utf-8 -*-

'''Gustavo'''
'''Implementação de um enigma sudoku e sua solução utilizando força bruta
para executar: python3 sudoku.py'''

import time
import copy
import random


class quadro():
    '''quadro representa cada um dos 81 quadrinhos do enigma do sudoku. Um objeto quadro é inicializado com
    todas as possíveis respostas (1 a 9), resolvido como false, e a posição do quadro dentro do tabuleiro'''
    def __init__(self,posicao):
        self.respostasPossiveis = [1,2,3,4,5,6,7,8,9]
        self.resposta = None
        self.posicao = posicao
        self.resolvido = False

    def remove(self, num):
        '''
        :param num: possível resposta
        Função para remover o número passado das possíveis respostas
        '''
        if num in self.respostasPossiveis and self.resolvido == False:
            '''Se num está dentro das respostas possíveis e o quadro ainda não foi resolvido
            num é removido das respostas possíveis, até que reste apenas uma resposta possível'''
            self.respostasPossiveis.remove(num)
            if len(self.respostasPossiveis) == 1:
                '''Caso o tamanho da lista de resposatas possívei for igual a 1
                esse elemento é a resposta'''
                self.resposta = self.respostasPossiveis[0]
                self.resolvido = True
        if num in self.respostasPossiveis and self.resolvido == True:
            self.resposta = 0

    def resolvidoM(self):
        '''
        :return: se o quadro está ou não resolvido
        '''
        return self.resolvido

    def checkPosicao(self):
        '''
        :return: retorna a posição do quadro no tabuleiro (linha, coluna, quadrante).
        '''
        return self.posicao

    def returnPossiveis(self):
        '''
        :return: Retorna as possíveis respostas para um determinado quadro
        '''
        return self.respostasPossiveis

    def tamDasPossibilidades(self):
        '''
        :return: Retorna a quantidade de respostas possíveis
        '''
        return len(self.respostasPossiveis)

    def returnResolvido(self):
        '''
        :return: o elemento que resta dentro das respostas possíveis ou 0, caso o quadro ainda não esteja resolvido
        '''
        if self.resolvido == True:
            return self.respostasPossiveis[0]
        else:
            return 0

    def setResposta(self,num):
        '''
        :param num: Resposta
         Verifica se o número recebido não é 0, se não for, configura-o como resposta.

        '''
        if num in [1,2,3,4,5,6,7,8,9]:
            self.resolvido = True
            self.resposta = num
            self.respostasPossiveis = [num]
        else:
            raise(ValueError)

    def reset(self):
        '''
        Reseta todos os atributos de um quadro para os valores originais
        '''
        self.respostasPossiveis = [1,2,3,4,5,6,7,8,9]
        self.resposta = None
        self.resolvido = False

def sudokuVazio():
    '''Criando um sudoku vazio
    x = linha;
    y = coluna
    z = quadrante
    Inicialmente (x,y,z) = (1,1,1), começa iterando pelas colunas (1,2,1), depois quadrantes (1,2,2), até linhas (2,1,1)
    '''
    res = []
    for x in range(1,10):
        if x in [7,8,9]:
            intz = 7
            z = 7
        if x in [4,5,6]:
            intz = 4
            z = 4
        if x in [1,2,3]:
            intz = 1
            z = 1
        for y in range(1,10):
            z = intz
            if y in [7,8,9]:
                z += 2
            if y in [4,5,6]:
                z += 1
            if y in [1,2,3]:
                z += 0
            c = quadro((x,y,z))
            res.append(c)
    return res

def printSudoku(sudoku):
    '''Formato do sudoku'''
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    for i in range(81):
        if i in range(0,9):
            row1.append(sudoku[i].returnResolvido())
        if i in range(9,18):
            row2.append(sudoku[i].returnResolvido())
        if i in range(18,27):
            row3.append(sudoku[i].returnResolvido())
        if i in range(27,36):
            row4.append(sudoku[i].returnResolvido())
        if i in range(36,45):
            row5.append(sudoku[i].returnResolvido())
        if i in range(45,54):
            row6.append(sudoku[i].returnResolvido())
        if i in range(54,63):
            row7.append(sudoku[i].returnResolvido())
        if i in range(63,72):
            row8.append(sudoku[i].returnResolvido())
        if i in range(72,81):
            row9.append(sudoku[i].returnResolvido())
    print(row1[0:3],row1[3:6],row1[6:10])
    print(row2[0:3],row2[3:6],row2[6:10])
    print(row3[0:3],row3[3:6],row3[6:10])
    print('')
    print(row4[0:3],row4[3:6],row4[6:10])
    print(row5[0:3],row5[3:6],row5[6:10])
    print(row6[0:3],row6[3:6],row6[6:10])
    print('')
    print(row7[0:3],row7[3:6],row7[6:10])
    print(row8[0:3],row8[3:6],row8[6:10])
    print(row9[0:3],row9[3:6],row9[6:10])


def geraSudoku():
    '''Gera um sudoku completo atribuindo valores aleatórios a um número também aleatório de quadros inicialmente preenchidos,
    sempre respeitando as regras do sudoku
    '''
    quadros = [i for i in range(81)]
    sudoku = sudokuVazio()
    while len(quadros) != 0:
        menorNum = []
        menor = []
        for i in quadros:
            '''Encontra o tamanho das possibilidades de respostas dos quadros que sobraram
            e seleciona a menor entre elas'''
            menorNum.append(sudoku[i].tamDasPossibilidades())
            m = min(menorNum)
        for i in quadros:
            if sudoku[i].tamDasPossibilidades() == m:
                menor.append(sudoku[i])
        '''Escolhendo aleatoriamente a resposta para um quadro'''
        seleciona = random.choice(menor)
        selecionaIndex = sudoku.index(seleciona)
        quadros.remove(selecionaIndex)
        posicao1 = seleciona.checkPosicao()
        if seleciona.resolvidoM() == False:
            valores = seleciona.returnPossiveis()
            valorFinal = random.choice(valores)
            seleciona.setResposta(valorFinal)
            for i in quadros:
                '''Verificando se há valores repetidos na mesma linha, coluna e quadrante, se houver esse valor é removido'''
                posicao2 = sudoku[i].checkPosicao()
                if posicao1[0] == posicao2[0]:
                    sudoku[i].remove(valorFinal)
                if posicao1[1] == posicao2[1]:
                    sudoku[i].remove(valorFinal)
                if posicao1[2] == posicao2[2]:
                    sudoku[i].remove(valorFinal)
        else:
            valorFinal = seleciona.returnResolvido()
            '''Verificando se há valores repetidos na mesma linha, coluna e quadrante, se houver esse valor é removido'''
            for i in quadros:
                posicao2 = sudoku[i].checkPosicao()
                if posicao1[0] == posicao2[0]:
                    sudoku[i].remove(valorFinal)
                if posicao1[1] == posicao2[1]:
                    sudoku[i].remove(valorFinal)
                if posicao1[2] == posicao2[2]:
                    sudoku[i].remove(valorFinal)
    return sudoku

def sudokuChecker(sudoku):
    '''
    :param sudoku: Recebe um enigma sudoku
    :return: True -> Se o sudoku passado está no formato correto e obedece às regras
    :return: False -> Caso contrário
    '''
    for i in range(len(sudoku)):
        for n in range(len(sudoku)):
            if i != n:
                posicao1 = sudoku[i].checkPosicao()
                posicao2 = sudoku[n].checkPosicao()
                if posicao1[0] == posicao2[0] or posicao1[1] == posicao2[1] or posicao1[2] == posicao2[2]:
                    num1 = sudoku[i].returnResolvido()
                    num2 = sudoku[n].returnResolvido()
                    if num1 == num2:
                        return False

    return True

def sudokuPerfeito():
    '''
    :return: Sudoku
    Gera um sudoku completo e totalmente aleatório
    '''
    result = False
    while result == False:
        s = geraSudoku()
        result = sudokuChecker(s)
    return s


def resolucaoFB(sudoku, f = 0):
    '''
    :param sudoku: Enigma do sudoku
    :param f: tentativas de resolução do sudoku
    Recebe como entrada um enigma do sudoku ainda não resolvido e utiliza um algoritmo de força bruta para resolvê-lo.
    Primeiro verifica se há algum quadro com respostas óbvias, em seguida busca por soluçoes fáceis em linhas,
    colunas e quadrantes. Ele ataca na ordem descrita (quadro,linha,coluna,quadrante) tendo como base o tamanho das possibilidades
    dado por tamDasPossibilidades, buscando sempre aqueles de menor tamanho. O algoritmo tenta adivinhar na base da tentativa e erro, se
    um valor tentado para um quadro estiver incorreto, ele é removido da lista e o algorimto tenta uma resposta
    diferente para outro quadro até que todas os quadros estejam resolvidos
    '''
    if f > 900:
        return False

    copy_s = copy.deepcopy(sudoku)
    quadros = [i for i in range(81)]
    quadrosResolvidos = []
    for i in quadros:
        #Verifica os quadros com tamanho de possíveis respostas igual a 1 e os adiciona aos quadros resolvidos
        if copy_s[i].tamDasPossibilidades() == 1:
            quadrosResolvidos.append(i)
    while quadrosResolvidos != []:
        for n in quadrosResolvidos:
            quadro = copy_s[n]
            posicao1 = quadro.checkPosicao()
            valorFinal = copy_s[n].returnResolvido()
            for i in quadros:
                '''Verificando as regras do sudoku, como em geraSudoku()'''
                posicao2 = copy_s[i].checkPosicao()
                if posicao1[0] == posicao2[0]:
                    copy_s[i].remove(valorFinal)
                if posicao1[1] == posicao2[1]:
                    copy_s[i].remove(valorFinal)
                if posicao1[2] == posicao2[2]:
                    copy_s[i].remove(valorFinal)
                if copy_s[i].tamDasPossibilidades() == 1 and i not in quadrosResolvidos and i in quadros:
                    quadrosResolvidos.append(i)

            quadrosResolvidos.remove(n)
            quadros.remove(n)
        if quadros != [] and quadrosResolvidos == []:
            menorNum = []
            menor = []
            for i in quadros:
                menorNum.append(copy_s[i].tamDasPossibilidades())
            m = min(menorNum)
            for i in quadros:
                if copy_s[i].tamDasPossibilidades() == m:
                    menor.append(copy_s[i])
            seleciona = random.choice(menor)
            randQ = copy_s.index(seleciona)
            randT = random.choice(copy_s[randQ].returnPossiveis())
            copy_s[randQ].setResposta(randT)
            quadrosResolvidos.append(randQ)
    if sudokuChecker(copy_s):
        return copy_s
    else:
        return resolucaoFB(sudoku, f + 1)


def resolve(sudoku, n = 0):
    '''
    :param sudoku: enigma do sudoku
    :param n: número de tentativas
    :return: Sudoku resolvido e número de tentativas ou false caso o número máximo de tentativas
    Esse método chama resolucaoFB para evitar erros de recursão. Retorna True se o enigma for solucionável
    '''
    if n < 30:
        s = resolucaoFB(sudoku)
        if s != False:
            return s
        else:
            resolve(sudoku, n+1)
    else:
        return False

def geraEnigma(sudoku):
    '''
    :param sudoku: Enigma sudoku
    :return: Um enigma sudoku, sua possível solução e o número de tentativas
    Função para gerar um enigma sudoku
    '''
    quadros = [i for i in range(81)]
    while quadros != []:
        copy_s = copy.deepcopy(sudoku)
        randIndex = random.choice(quadros)
        quadros.remove(randIndex)
        copy_s[randIndex].reset()
        s = resolve(copy_s)
        if s[0] == False:
            f = resolve(sudoku)
            return printSudoku(sudoku)
        elif Check(s, resolve(copy_s)):
            if Check(s, resolve(copy_s)):
                sudoku[randIndex].reset()
        else:
            f = resolve(sudoku)
            return sudoku, f[1], f[2]


def Check(s1,s2):
    '''

    :param s1: sudoku 1
    :param s2: sudoku 2
    :return: True se dois enigmas forem iguais, False o contrário
    Função para verificar se dois enigmas do sudoku são iguais.
    '''
    for i in range(len(s1)):
        if s1[i].returnResolvido() != s2[i].returnResolvido():
            return False
    return True


#Demonstrando o enigma do sudoku e ele resolvido.
print("Desafio sudoku: \n")
c = geraEnigma(sudokuPerfeito())
printSudoku(c[0])
print("\nDesafio resolvido\n")
a = resolucaoFB(c[0])
printSudoku(a)
