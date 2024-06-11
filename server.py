import Pyro4

# Define a classe do servidor
@Pyro4.expose
class MathOperations(object):
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a / b
    
    def average(self, numbers):
        if not numbers:
            return "Erro: Lista vazia"
        return sum(numbers) / len(numbers)

# Inicializa o servidor Pyro4
def main():
    # Cria um daemon Pyro
    daemon = Pyro4.Daemon()

    # Registra o objeto do servidor no daemon
    uri = daemon.register(MathOperations)

    # Imprime a URI do servidor para que o cliente possa se conectar
    print("Servidor está rodando. URI:", uri)

    # Mantém o servidor rodando
    daemon.requestLoop()

if __name__ == "__main__":
    main()
