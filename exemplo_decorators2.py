# Implemente um decorator chamado log_execucao que imprime "Executando função..." antes da execução e "Execução concluída" depois.
# Use-o em uma função calcular_quadrado(n) que retorna n ** 2.


def log_execucao(func):
    def wrapper(*args, **kwargs):
        print(f'Executando função: {func.__name__}...')
        resultado = func(*args, **kwargs)
        print(f'Execução concluída: {func.__name__}')
        return resultado
    return wrapper

@log_execucao
def calcular_quadrado(n):
    return n ** 2 


response = calcular_quadrado(3)
print(f'Resultado: {response}')

