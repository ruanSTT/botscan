# test_script.py

import os


def exemplo_try_except():
    try:
        # Simula erro de arquivo
        open("arquivo_inexistente.txt", "r")
    except:  # Exceção genérica, isso vai ser detectado pelo checker!
        print("Erro ao abrir o arquivo.")


def exemplo_funcao_com_erro():
    if 10 == 10:  # Linha vazia entre expressões
        print("Isso é um erro!")  # Linha de código sem um propósito real.


def exemplo_formatacao_incorreta():
    a = 1
    b = 2
    if a == b:
        print("A igualdade é verdadeira!")


def exemplo_codigo_sem_uso():
    a = 42  # Definição de variável sem uso
    return True
