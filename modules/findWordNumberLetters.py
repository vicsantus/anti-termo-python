import os


def buscar_palavras_de_5_letras(number_letters):
    try:
        nome_arquivo = os.path.join('data', 'data')
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()

            palavras_de_5_letras = [
                palavra for palavra
                in palavras if len(palavra) == number_letters]

            return palavras_de_5_letras
    except FileNotFoundError:
        return f"Arquivo '{nome_arquivo}' não encontrado."


# Substitua 'nome_do_arquivo.txt' pelo nome do seu arquivo
# nome_do_arquivo = 'exemplo.txt'
# resultado = buscar_palavras_de_5_letras(5)

# if isinstance(resultado, list):
#     print(f"Palavras de 5 letras: {resultado}")
# else:
#     print(resultado)

def salvar_palavras_em_arquivo(caminho_arquivo_saida, palavras):
    try:
        with open(caminho_arquivo_saida, 'w') as arquivo_saida:
            for palavra in palavras:
                arquivo_saida.write(f"{palavra}\n")
        print(f"Palavras salvas em '{caminho_arquivo_saida}'.")
    except Exception as e:
        print(f"Erro ao salvar palavras: {e}")


# Substitua 'data_saida.txt' pelo nome desejado para o arquivo de saída
caminho_arquivo_saida = 'data/data_5_letters'

# Use a função buscar_palavras_de_5_letras para obter o array
# de palavras (assumindo que já foi definida)
palavras_de_5_letras = buscar_palavras_de_5_letras(5)

# Salva as palavras em um novo arquivo
salvar_palavras_em_arquivo(caminho_arquivo_saida, palavras_de_5_letras)
