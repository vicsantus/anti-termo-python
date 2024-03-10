import os


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def remover_palavras_repetidas_e_salvar(caminho_entrada, caminho_saida):
    try:
        with open(caminho_entrada, 'r') as arquivo_entrada:
            conteudo = arquivo_entrada.read()
            palavras = conteudo.split()

            # Usando o Quicksort para ordenar e remover duplicatas
            palavras_unicas = quicksort(list(set(palavras)))

            with open(caminho_saida, 'w') as arquivo_saida:
                for palavra in palavras_unicas:
                    arquivo_saida.write(f"{palavra}\n")

        print(f"Palavras únicas salvas em '{caminho_saida}'.")
    except FileNotFoundError:
        print(f"Arquivo '{caminho_entrada}' não encontrado.")


# Substitua 'data_5_letters.txt' pelo nome do seu arquivo de entrada
caminho_arquivo_entrada = os.path.join('data', 'data_5_letters')

# Substitua 'data_unicas.txt' pelo nome do seu arquivo de saída
caminho_arquivo_saida = os.path.join('data', 'data_5_letters2')

# Remover palavras repetidas e salvar em um novo arquivo
remover_palavras_repetidas_e_salvar(
    caminho_arquivo_entrada, caminho_arquivo_saida)
