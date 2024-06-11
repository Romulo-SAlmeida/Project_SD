import Pyro4

def main():
    # A URI do servidor impressa pelo servidor
    uri = "PYRO:obj_13c185b0d579424781e039a6b3c339f6@localhost:53319" 

    # Cria um proxy para se conectar ao servidor remoto
    math_operations = Pyro4.Proxy(uri)

    # Chama os métodos remotos
    result_add = math_operations.add(5, 3)
    result_subtract = math_operations.subtract(10, 4)
    result_multiply = math_operations.multiply(6, 7)
    result_divide = math_operations.divide(8, 2)
    result_average = math_operations.average([1, 2, 3, 4, 5])

    # resultados das operações
    print("Resultado da adição (5 + 3):", result_add)
    print("Resultado da subtração (10 - 4):", result_subtract)
    print("Resultado da multiplicação (6 * 7):", result_multiply)
    print("Resultado da divisão (8 / 2):", result_divide)
    print("Resultado da média ([1, 2, 3, 4, 5]):", result_average)

if __name__ == "__main__":
    main()
