import json
import os

class Cinema:
    """
    Classe para o sistema de reservas de ingressos do cinema.
    """
    def __init__(self, fileiras, assentos_por_fileira):
        """
        Inicializa o sistema de reservas de ingressos.
        fileiras (int): Número de fileiras no cinema.
        assentos_por_fileira (int): Número de assentos por fileira no cinema.
        """
        self.fileiras = fileiras
        self.assentos_por_fileira = assentos_por_fileira
        self.assentos_disponiveis = {(chr(65 + i), j + 1) for i in range(fileiras) for j in range(assentos_por_fileira)}
        self.reservas = {}

    def visualizar_assentos(self):
        """
        Visualiza os assentos disponíveis no cinema.
        """
        print("Assentos disponíveis:")
        print("----------- TELA -------------")
        for fileira in range(self.fileiras):
            for assento in range(1, self.assentos_por_fileira + 1):
                if (chr(65 + fileira), assento) in self.assentos_disponiveis:
                    print(f"{chr(65 + fileira)}{assento}", end=" ")
                else:
                    print("--", end=" ")
            print()

    def reservar_ingresso(self, cliente, assento):
        """
        Reserva um ingresso para o cliente em um assento específico.
        cliente (str): Nome do cliente.
        assento (tuple): Tupla representando o assento no formato (fileira, assento).
        """
        if assento in self.assentos_disponiveis:
            self.assentos_disponiveis.remove(assento)
            self.reservas[cliente] = assento
            print(self.reservas)
            print("--------------------------------")
            print(f"Ingresso reservado com sucesso para {cliente} no assento {assento}.")
            print("--------------------------------")
        else:
            print("--------------------------------")
            print("Assento indisponível. Por favor, escolha outro assento.")
            print("--------------------------------")

    def salvar_reservas(self):
        """
        Salva as reservas em um arquivo JSON.
        """
        dados = json.dumps(self.reservas, indent=4)
        with open('dados.json', "w") as arquivo:
            arquivo.write(dados)
            
    def ler_reservas(self):
        """
        Lê as reservas a partir de um arquivo JSON.
        """
        if os.path.exists('dados.json'):
            with open('dados.json', "r") as arquivo:
                data = json.load(arquivo)
                self.reservas = data
                
                for reserva in self.reservas:
                    assento = tuple(self.reservas[reserva])
                    self.assentos_disponiveis.remove(assento)
                    

# Exemplo de uso do sistema de reservas de ingressos
if __name__ == "__main__":
    cinema = Cinema(5, 10)  # Cinco fileiras, dez assentos por fileira
    cinema.ler_reservas()

    while True:
        print("* * * * * * * * * * * * * * * * * * * *")
        print("--------------------------------------")
        print("----BEM VINDO AO SISTEMA DE CINEMA----")
        print("--------------------------------------")
        print("* * * * * * * * * * * * * * * * * * * *")

        print("\nMenu:")
        print("--------------------------------")
        print("1 - Visualizar assentos disponíveis")
        print("2 - Reservar ingresso")
        print("3 - Sair do sistema")
        print("--------------------------------")

        opcao = input("Escolha uma opção: ")
        print("--------------------------------")

        if opcao == '1':
            cinema.visualizar_assentos()
        elif opcao == '2':
            print("--------------------------------")
            cliente = input("Digite o nome do cliente: ")
            print("--------------------------------")
            assento = input("Digite o assento desejado (ex: A1): ").upper()
            fileira, numero = [assento[0], int(assento[1:])]
            cinema.reservar_ingresso(cliente, (fileira, numero))
        elif opcao == '3':
            print("--------------------------------")
            print("ENCERRANDO PROGRAMA......")
            print("--------------------------------")
            cinema.salvar_reservas()
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
            print("--------------------------------")
