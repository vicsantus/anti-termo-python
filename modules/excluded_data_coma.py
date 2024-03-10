import os

# Caminho do arquivo original e do novo arquivo
caminho_arquivo_original = os.path.join('data', 'data_coma')
caminho_arquivo_novo = os.path.join('data', 'data_coma_sem_extras')

# Abre o arquivo original para leitura e o novo para escrita
with open(caminho_arquivo_original,
          'r') as arquivo_original, open(caminho_arquivo_novo,
                                         'w') as arquivo_novo:
    # Lê cada linha do arquivo original, remove tudo após a
    # primeira vírgula e escreve no novo arquivo
    for linha in arquivo_original:
        # Remove tudo após a primeira vírgula
        nova_linha = linha.split(',', 1)[0]
        arquivo_novo.write(nova_linha + '\n')

print("Operação concluída. O novo arquivo foi salvo"
      " em 'data_coma_sem_extras'.")
