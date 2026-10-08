import nltk 
import json
import re
from pathlib import Path

import nltk
from nltk.corpus import stopwords

# Baixa a lista de stopwords em português, caso necessário
nltk.download("stopwords", quiet=True)

# Carrega as stopwords
stopwords_pt = set(stopwords.words("portuguese"))


def preprocessar_texto(texto):
    # 1. Converter para letras minúsculas
    texto = texto.lower()

    # 2. Remover pontuação
    texto = re.sub(r"[^\w\s]", " ", texto)

    # 3. Separar o texto em palavras
    palavras = texto.split()

    # 4. Remover stopwords
    palavras = [
        palavra for palavra in palavras
        if palavra not in stopwords_pt
    ]

    return palavras


# Localizar o arquivo data.json na mesma pasta do main.py
caminho_arquivo = Path(__file__).parent / "data.json"

with caminho_arquivo.open("r", encoding="utf-8") as arquivo:
    avaliacoes = json.load(arquivo)


# Aplicar o pré-processamento em cada avaliação
for avaliacao in avaliacoes:
    avaliacao["tokens"] = preprocessar_texto(avaliacao["texto"])


# Salvar os dados processados em um novo arquivo
caminho_saida = Path(__file__).parent / "data_processado.json"

with caminho_saida.open("w", encoding="utf-8") as arquivo:
    json.dump(
        avaliacoes,
        arquivo,
        ensure_ascii=False,
        indent=4
    )

print("Pré-processamento concluído!")
print(f"Total de avaliações processadas: {len(avaliacoes)}")
print(f"Arquivo salvo em: {caminho_saida}")