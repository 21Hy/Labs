# exercicio 1, a)
def mesmo_tamanho(lista1, lista2):
    if len(lista1) == len(lista2):
        return True
# parece estar certo.


# exercicio 1, b)
def valores_repetidos(lista):
    lista_retorno = []
    nova_lista = []

    for elemento in lista:
        if elemento not in lista_retorno:
            lista_retorno.append(elemento)
        else: 
            nova_lista.append(elemento)

    return nova_lista


# exercicio 1, c)
def soma_do_primeiro_e_ultimo(lista):
# dúvida, receber em números inteiros ou float em functions???
    return lista[0] + lista[len(lista) - 1]

# exercicio 1, d)
# dúvida, receber em números inteiros ou float em functions???
def soma_de_duas_listas_com_o_mesmo_indice(lista1, lista2): 
    if len(lista1) > len(lista2):
        retorno = []
        for i in range(len(lista2)):
            retorno.append(lista1[i] + lista2[i])
    else: 
        retorno = []
        for i in range(len(lista1)):
            retorno.append(lista1[i] + lista2[i])
    return retorno

# parece estar certo


# exercicio 1, e)
# ideia, usar um algoritmo que retire todos os elementos da lista, usando um loop com index de itereação, 
# para passarem por um 'check-in' de tipo de elemento, usando função type, caso sejam strings estes elementos
# serão adicionados a outra lista vazia, utilizando a função extend.




# exercicio 1, f)
# ideia, criar um loop que remova todos os elementos, usando index, para fazer operações
def media_dos_valores_da_lista(lista):
    for i in range(len(lista)):
        lista[i]

# exercicio 1, g)
# ideia, criar um loop em que cada elemento é retirado, utilizando indexação, e devolvido como inteiros.

# exercicio 2
# ideia, requisitos são meras condições, para se poder candidatar-se à vaga é preciso que todas elas sejam
# True.
