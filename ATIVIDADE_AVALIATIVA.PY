# Estrutura de dados para o Registro de Reserva
class Reserva:
    def __init__(self, numero_aviao, nome_passageiro):
        self.numero_aviao = numero_aviao
        self.nome_passageiro = nome_passageiro

# --- Persistência Temporária de Dados ---
vetor_avioes = [0] * 4      # Armazena os IDs dos 4 aviões
vetor_assentos = [0] * 4    # Armazena a quantidade de assentos de cada avião
lista_reservas = []         # Armazena objetos do tipo Reserva (máx 20)
LIMITE_GLOBAL = 20

def registrar_avioes():
    print("\n--- [1] Cadastro de Aeronaves ---")
    for i in range(4):
        vetor_avioes[i] = int(input(f"Digite o número de identificação do {i+1}º avião: "))
    print("✔ Todos os aviões foram registrados.")

def registrar_assentos():
    print("\n--- [2] Cadastro de Assentos ---")
    for i in range(4):
        # Relaciona o assento ao avião pelo índice
        qtd = int(input(f"Quantidade de assentos para o avião {vetor_avioes[i]}: "))
        vetor_assentos[i] = qtd
    print("✔ Quantitativo de assentos atualizado.")

def reservar_passagem():
    # Validação do Limite Global (Regra de Negócio)
    if len(lista_reservas) >= LIMITE_GLOBAL:
        print("❌ Erro: O sistema atingiu o limite máximo de 20 reservas globais.")
        return

    print("\n--- [3] Realizar Reserva ---")
    num_busca = int(input("Informe o número do avião: "))

    # Validação de Existência
    if num_busca not in vetor_avioes:
        print("❌ Este avião não existe!")
        return

    # Localiza o índice do avião para checar os assentos
    indice = vetor_avioes.index(num_busca)

    # Validação de Vagas
    if vetor_assentos[indice] <= 0:
        print("❌ Não há assentos disponíveis para este avião!")
    else:
        nome = input("Nome do passageiro: ")
        # Criação do Registro
        nova_reserva = Reserva(num_busca, nome)
        lista_reservas.append(nova_reserva)
        
        # Redução da vaga no vetor de assentos
        vetor_assentos[indice] -= 1
        print("✔ Reserva realizada com sucesso!")

def consultar_por_aviao():
    print("\n--- [4] Consulta por Avião ---")
    num_busca = int(input("Digite o número do avião para consultar passageiros: "))
    
    if num_busca not in vetor_avioes:
        print("❌ Este avião não existe!")
        return

    print(f"Lista de passageiros do avião {num_busca}:")
    encontrou = False
    for r in lista_reservas:
        if r.numero_aviao == num_busca:
            print(f"- {r.nome_passageiro}")
            encontrou = True
    
    if not encontrou:
        print("Não há reservas realizadas para este avião!")

def consultar_por_passageiro():
    print("\n--- [5] Consulta por Passageiro ---")
    nome_busca = input("Digite o nome do passageiro: ").strip().lower()
    
    print(f"Aviões reservados para '{nome_busca.title()}':")
    encontrou = False
    for r in lista_reservas:
        if r.nome_passageiro.lower() == nome_busca:
            print(f"- Avião nº: {r.numero_aviao}")
            encontrou = True
            
    if not encontrou:
        print("Não há reservas realizadas para este passageiro!")

# --- Menu Interativo ---
def menu():
    while True:
        print("\n" + "="*35)
        print("      SISTEMA DE VENDAS AÉREAS")
        print("="*35)
        print("1. Registrar aviões")
        print("2. Registrar assentos")
        print("3. Reservar passagem")
        print("4. Consultar por avião")
        print("5. Consultar por passageiro")
        print("6. Encerrar sistema")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            registrar_avioes()
        elif opcao == '2':
            registrar_assentos()
        elif opcao == '3':
            reservar_passagem()
        elif opcao == '4':
            consultar_por_aviao()
        elif opcao == '5':
            consultar_por_passageiro()
        elif opcao == '6':
            print("Encerrando sistema... Tenha um excelente dia!")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")

if __name__ == "__main__":
    menu()