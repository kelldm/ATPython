import string
import random
import json
import os

banco_de_dados = []

def adicionar_dados_criptografados(dados):
    """
    Adiciona os dados criptografados ao banco de dados.
    dados (dict): Dicionário contendo os dados a serem adicionados (serviço, login, senha).
    """
    dados_criptografados = {}
    for chave, valor in dados.items():
        dados_criptografados[chave] = criptografar(valor)
    banco_de_dados.append(dados_criptografados)
    
def consultar_senha(servico, palavra_chave):
    """
    Consulta a senha de um serviço específico no banco de dados.

    servico (str): Nome do serviço.
    palavra_chave (str): Palavra chave para autorizar a consulta.

    Retorna:
    tuple: Tupla contendo o login e a senha do serviço consultado.
    """
    if palavra_chave != "mostrar_senha":
        print("Palavra chave incorreta.")
        return
    
    global banco_de_dados
    
    for item in banco_de_dados:
        if descriptografar(item["servico"]) == servico:
            login = descriptografar(item["login"])
            senha = descriptografar(item["senha"])
            return login, senha

def criptografar(texto):
    """
    Criptografa um texto usando ASCII
    texto (str): Texto a ser criptografado.
    Retorna:
    str: Texto criptografado.
    """
    texto_criptografado = ""
    for char in texto:
        if char.isalpha():
            codigo = ord(char)
            if char.islower():
                novo_codigo = (codigo - 97 + 3) % 26 + 97
            else:
                novo_codigo = (codigo - 65 + 3) % 26 + 65
            texto_criptografado += chr(novo_codigo)
        else:
            texto_criptografado += char
    return texto_criptografado

def descriptografar(texto_criptografado):
    """
    Descriptografa um texto criptografado usando ASCII
    texto_criptografado (str): Texto criptografado a ser descriptografado
    Retorna:
    str: Texto descriptografado
    """
    texto_original = ""
    for char in texto_criptografado:
        if char.isalpha():
            codigo = ord(char)
            if char.islower():
                novo_codigo = (codigo - 97 - 3) % 26 + 97
            else:
                novo_codigo = (codigo - 65 - 3) % 26 + 65
            texto_original += chr(novo_codigo)
        else:
            texto_original += char
    return texto_original

def gerar_senha(tamanho):
    """
    Gera uma senha aleatória.
    tamanho (int): Tamanho da senha a ser gerada
    Retorna:
    str: Senha gerada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gravar_banco():
    """
    Grava o banco de dados em um arquivo JSON
    """
    global banco_de_dados
    dados = json.dumps(banco_de_dados, indent=4)
    with open('senhas.json', "w") as arquivo:
        arquivo.write(dados)
    
def ler_banco():
    """
    Lê o banco de dados a partir de um arquivo JSON
    """
    global banco_de_dados
    
    if os.path.exists('senhas.json'):
        with open('senhas.json', "r") as arquivo:
            data = json.load(arquivo)
            banco_de_dados = data
             
def main():
    """
    Função principal que executa o programa 
    """
    global banco_de_dados
    
    ler_banco()
    
    while True:
        print("\n1. Gerar Senha")
        print("2. Consultar Senha")
        print("3. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            servico = input("Digite o nome do serviço: ")
            login = input("Digite o login: ")
            comprimento = int(input("Digite o comprimento da senha desejada: "))
            senha = gerar_senha(comprimento)
            dados = {
                "servico": servico,
                "login":login,
                "senha":senha
            }
            adicionar_dados_criptografados(dados)

        elif escolha == '2':
            servico = input("Digite o nome do serviço: ")
            palavra_chave = input("Digite a palavra chave: ")
            login, senha = consultar_senha(servico, palavra_chave)
            print(f"login: {login} - senha: {senha}")

        elif escolha == '3':
            print("Saindo...")
            gravar_banco()
            break

        else:
            print("Opção inválida. Tente novamente.")
    
main()
