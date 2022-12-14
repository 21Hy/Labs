# Lab_4_1 functions.py
# Aluno: 30011447

# exercicio 1, a)
def mesmo_tamanho(lista1, lista2):
    if len(lista1) == len(lista2):
        return True
    
# exercicio 1, b)
def valores_repetidos(lista):
    nova_lista = []
    for elemento in lista:
        if lista.count(elemento) > 1 and elemento not in nova_lista:
            nova_lista.append(elemento)
    return nova_lista

# exercicio 1, c)
def soma_do_primeiro_e_ultimo(lista):
    # verificação de números in or float
    nova_lista = []
    for elemento in lista:
        if ((type(elemento) == int) or (type(elemento) == float)):
            nova_lista.append(elemento)
    # soma do primeiro e último
    return nova_lista[0] + nova_lista[len(nova_lista) - 1]

# exercicio 1, d)
def soma_de_duas_listas_com_o_mesmo_indice(lista1, lista2):
    # verificação de númereros int or float
    nova_lista1 = []
    nova_lista2 = []
    for elemento in lista1:
        if ((type(elemento) == int) or (type(elemento) == float)):
            nova_lista1.append(elemento)
    for elemento in lista2:
        if ((type(elemento) == int) or (type(elemento) == float)):
            nova_lista2.append(elemento)
    # soma das duas listas
    if len(nova_lista1) > len(nova_lista2):
        retorno = []
        for i in range(len(nova_lista2)):
            retorno.append(nova_lista1[i] + nova_lista2[i])
    else: 
        retorno = []
        for i in range(len(nova_lista1)):
            retorno.append(nova_lista1[i] + nova_lista2[i])
    return retorno

# exercicio 1, e)
def retornar_string(lista):
    nova_lista = []
    for i in range(len(lista)):
        if type(lista[i]) == str:
            nova_lista.append(lista[i])
    return nova_lista

# exercicio 1, f)
def media_dos_valores_da_lista(lista):
    # verificação de números in or float
    nova_lista = []
    for elemento in lista:
        if ((type(elemento) == int) or (type(elemento) == float)):
            nova_lista.append(elemento)
    # média dos valores
    return sum(nova_lista)/ len(nova_lista)

# exercicio 1, g)
def elementos_arredondados(lista):
    nova_lista = []
    for elemento in lista:
        arredondamento = int(elemento)
        nova_lista.append(arredondamento)
    return nova_lista
