# Matheus Correa Fiori
# GRR - 20211618
# Trabalho Estrutura de Dados II - Tabela Hash

class VotingSystem:
    def __init__(self):
        self.voters = set()
        self.votes = {}

    def vote(self, voter_id, candidate):
        if voter_id in self.voters:
            return "Erro: Eleitor já votou."
        self.voters.add(voter_id)
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            self.votes[candidate] = 1
        return f"Voto registrado para {candidate}!"

    def show_results(self):
        if not self.votes:
            return "Nenhum voto registrado."
        results = ["Resultado da eleição:"]
        for candidate, count in self.votes.items():
            results.append(f"{candidate}: {count} voto(s)")
        return "\n".join(results)


if __name__ == "__main__":
    voting_system = VotingSystem()
    
    while True:
        print("\nMENU:")
        print("1. Votar")
        print("2. Mostrar resultados")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            voter_id = input("Digite o ID do eleitor: ")
            candidate = input("Digite o nome do candidato: ")
            print(voting_system.vote(voter_id, candidate))
        elif choice == "2":
            print(voting_system.show_results())
        elif choice == "3":
            print("Encerrando o sistema de votação.")
            break
        else:
            print("Opção inválida. Tente novamente.")