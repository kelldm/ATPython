historico = []

def menu(): 
    """
    Exibe o menu de opções para o usuário e solicita a escolha de uma opção.
    str: A opção escolhida pelo usuário.
    """

    print("-----------------------------------")
    print("\nMenu:")
    print("1. Adicionar receita")
    print("2. Adicionar despesa")
    print("3. Exibir extrato")
    print("4. Exibir relatório de gastos")
    print("5. Exibir relatório de receitas")
    print("6. Sair do sistema")
    print("-----------------------------------")
        
    opcao = input("Escolha uma opção: ")
    print("-----------------------------------")

    return opcao

def adicionar_receita_no_historico(tipo, valor, fonte):
    """
    Registra uma receita no histórico.
    tipo (str): Tipo da operação (receita).
    valor (float): Valor da receita.
    fonte (str): Fonte da receita.
    """
    global historico
    historico.append({
        "operacao": tipo,
        "valor": valor,
        "fonte": fonte})

def adicionar_despesa_no_historico(tipo, valor, descricao, categoria):
    """
    Registra uma despesa no histórico.
    tipo (str): Tipo da operação (despesa).
    valor (float): Valor da despesa.
    descricao (str): Descrição da despesa.
    categoria (str): Categoria da despesa.
    """

    global historico
    historico.append({
        "operacao": tipo,
        "valor": valor,
        "descricao": descricao,
        "categoria": categoria
    })
    
def adicionar_receita(saldo, valor, fonte, receitas):
    """
    Deve adicionar ao saldo o valor e deve salvar na lista de receitas a operacao
    saldo (float): Saldo atual.
    valor (float): Valor da receita.
    fonte (str): Fonte da receita.
    receitas (list): Lista de receitas.
    """
    saldo += valor
    receitas.append({
        "valor":valor,
        "fonte":fonte
    })
    adicionar_receita_no_historico("receita", valor, fonte)


def adicionar_despesa(saldo, valor, descricao, categoria, despesas):
    """
    Registra uma despesa no histórico. Deve remover do saldo o valor passado e adicionar na lista de despesas a operacao
    tipo (str): Tipo da operação (despesa).
    valor (float): Valor da despesa.
    descricao (str): Descrição da despesa.
    categoria (str): Categoria da despesa.
    """
    saldo -= valor
    despesas.append({
        "valor": valor,
        "descricao": descricao,
        "categoria":categoria,
    })
    
    adicionar_despesa_no_historico("despesa", valor, descricao, categoria)

def mostrar_extrato(): 
    """
    Exibe o extrato das operações financeiras registradas no histórico.
    """
    global historico
    print("======= EXTRATO =======")
    for item in historico:
        if item["operacao"] == 'despesa':
            print("-----------------------")
            print(f"Operação: {item['operacao']}")
            print(f"Valor: -{item['valor']:.2f}")
            print(f"Descrição: {item['descricao']}")
            print(f"Categoria: {item['categoria']}")
            print("-----------------------")            
        else:
            print("-----------------------")
            print(f"Operação: {item['operacao']}")
            print(f"Valor: +{item['valor']:.2f}")
            print(f"Fonte: {item['fonte']}")
            print("-----------------------")
    print("======= FIM DO EXTRATO =======")

def exibir_relatorio_gastos(despesas):
    """
    Exibe um relatório de gastos ordenado por maior valor gasto na categoria.
    despesas (list): Lista de despesas.
    """

    despesas_ordenadas = sorted(despesas, key = lambda item: item['valor'], reverse = True)
    print("======= RELATORIO DE GASTOS =======")
    print("-----------------------------------")
    for despesa in despesas_ordenadas:
        print(f"Despesa: -{despesa['valor']} ({despesa['categoria']})")
        print(f"Categoria: {despesa['categoria']}")
        print(f"Descricao: {despesa['descricao']}")
    print("------------------------------------------")        
    print("======= FIM DO RELATORIO DE GASTOS =======")
    
def exibir_relatoro_receitas(receitas):
    """
    Exibe um relatório de receitas.
    receitas (list): Lista de receitas.
    """

    print("======= RELATORIO DE RECEITAS =======")
    print("-------------------------------------")

    for receita in receitas:
        print(f"Receita: +{receita['valor']}")
        print(f"Fonte: {receita['fonte']}")
    print("------------------------------------------")    
    print("======= FIM DO RELATORIO DE GASTOS =======")

def main():
    """
    Função principal que executa o sistema de controle financeiro.
    """
    print("*******************************************")
    print("***** SISTEMA DE CONTROLE FINANCEIRO ******")
    print("*******************************************")

    #definir seu saldo atual;
    saldo = float(input("Digite seu saldo: "))
    receitas = []
    despesas = []
    
    while True:
        escolha = menu()
        
        match escolha:
            
            case '1':
                 #Adicionar valores (receitas) ao seu orçamento, descrevendo a fonte financeira com um texto
                valor = float(input("Digite o valor da receita: "))
                print("-----------------------------------")

                fonte = input("Digite a fonte da receita: ")
                print("-----------------------------------")

                adicionar_receita(saldo, valor, fonte,receitas)
                
            case '2':
                 #Anotar gastos (despesas) que deverão ser associados a categorias pré-definidas
                entrada = input("Digite o valor da despesa (pode adicionar uma descrição separada por ';'): ")
                valores = entrada.split('; ')
                valor = float(valores[0])
                descricao = valores[1] if len(valores) > 1 else ''  
                categoria = input("Categoria(lazer, esportes, saude...): ").lower() 
                adicionar_despesa(saldo, valor, descricao, categoria, despesas)
                
            case '3':
                #Solicitar um relatório dos gastos, tipo extrato, que liste todas entradas e saídas indicando o saldo da conta a cada operação e o saldo final;
                mostrar_extrato()
                
            case '4': 
                 #Solicitar um relatório ordenado por valor dos gastos por categoria
                exibir_relatorio_gastos(despesas)
                
            case '5':
                #Solicitar um relatório com todas as receitas.
                exibir_relatoro_receitas(receitas)
                
            case '6':
                print("Fechando programa...")
                print("ADEUS.....")
                print("-----------------------------------")
                break
                       
main()