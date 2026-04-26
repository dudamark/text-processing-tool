import re
from collections import Counter


# =========================
# 1. EXTRAÇÃO DE EMAILS
# =========================
def extrair_emails(texto):
    padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|br)'
    return [m.group() for m in re.finditer(padrao, texto)]


# =========================
# 2. VALIDAÇÃO DE IDS
# =========================
def validar_ids(lista_ids):
    padrao = r'^[A-Z]{3}-\d{4}$'

    validos = []
    invalidos = []

    for item in lista_ids:
        if re.fullmatch(padrao, item):
            validos.append(item)
        else:
            invalidos.append(item)

    return validos, invalidos


# =========================
# 3. FREQUÊNCIA DE PALAVRAS
# =========================
def contar_frequencia(texto):
    texto = texto.lower()

    # substitui pontuação por espaço (não junta palavras)
    texto = re.sub(r'[^\w\s]', ' ', texto)

    palavras = texto.split()

    return dict(Counter(palavras))