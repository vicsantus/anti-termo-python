import os
import unicodedata


def remover_acentos(palavra):
    return ''.join((c for c in unicodedata.normalize('NFD', palavra)
                    if unicodedata.category(c) != 'Mn'))


def buscar_palavras_por_criterios(word,
                                  included_letters,
                                  excluded_letters,
                                  path='data_5_letters2'):
    try:
        nome_arquivo = os.path.join('data', path)
        with open(nome_arquivo, 'r') as arquivo:
            palavras = arquivo.read().split()

            palavras_filtradas = [
                palavra for palavra in palavras
                if (
                    all((letra is None or (letra == '0'
                                           and remover_acentos(palavra[i])
                                           not in included_letters)
                         or remover_acentos(palavra[i]) == letra)
                        for i, letra in enumerate(word))
                    and all(remover_acentos(letra_incluida) in
                            remover_acentos(palavra)
                            for letra_incluida in included_letters)
                    and all(remover_acentos(letra_excluida) not in
                            remover_acentos(palavra)
                            for letra_excluida in excluded_letters)
                )
            ]

            return palavras_filtradas
    except FileNotFoundError:
        return f"Arquivo '{nome_arquivo}' não encontrado."


def obter_letras_do_usuario(tipo_letras, tamanho_fixo=None):
    entrada_usuario = input(
        f"Digite as letras {tipo_letras} separadas por"
        " espaço (ou pressione Enter para nenhuma): ")

    if not entrada_usuario:
        return []

    letras = [letra if letra !=
              '0' else None for letra in entrada_usuario.split()]

    if tamanho_fixo and len(letras) != tamanho_fixo:
        print(f"Por favor, digite exatamente {tamanho_fixo} letras.")
        return obter_letras_do_usuario(tipo_letras, tamanho_fixo)

    return letras


def obter_letras_alvo():
    return obter_letras_do_usuario("alvo", tamanho_fixo=5)


def obter_letras_incluidas():
    return obter_letras_do_usuario("incluídas")


def obter_letras_excluidas():
    return obter_letras_do_usuario("excluídas")


# Obter letras do usuário
letras_alvo = obter_letras_alvo()
letras_incluidas = obter_letras_incluidas()
letras_excluidas = obter_letras_excluidas()

# Especificações para busca
resultado = buscar_palavras_por_criterios(
    letras_alvo, letras_incluidas, letras_excluidas)

if isinstance(resultado, list):
    print(f"Palavras que seguem os critérios: {resultado}")
else:
    print(resultado)
