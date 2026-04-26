import re

from file_reader import ler_arquivo
from utils import extrair_emails, validar_ids, contar_frequencia
from cleaner import TextCleaner


def main():

    # LEITURA DO ARQUIVO
    texto_original = ler_arquivo("exemplo.txt")

    if texto_original.startswith("ERRO"):
        print(texto_original)
        return

    print("\n=== TEXTO ORIGINAL ===")
    print(texto_original)

    # EXTRAÇÃO DE EMAILS (ANTES DE QUALQUER LIMPEZA)
    emails = extrair_emails(texto_original)

    print("\n=== E-MAILS EXTRAÍDOS ===")
    print(emails)

    
    # 3. EXTRAÇÃO DE IDS (ANTES DE QUALQUER LIMPEZA)
    ids_extraidos = re.findall(r'[A-Z]{3}-\d{4}', texto_original)

    validos, invalidos = validar_ids(ids_extraidos)

    print("\n=== IDS VÁLIDOS ===")
    print(validos)

    print("\n=== IDS INVÁLIDOS ===")
    print(invalidos)

    # 4. LIMPEZA (APENAS PARA FREQUÊNCIA DE PALAVRAS)
    texto_limpo = (
        TextCleaner(texto_original)
        .remove_extra_spaces()
        .to_lowercase()
        .get_text()
    )

    print("\n=== TEXTO LIMPO ===")
    print(texto_limpo)

    # 5. FREQUÊNCIA DE PALAVRAS
    frequencia = contar_frequencia(texto_limpo)

    print("\n=== FREQUÊNCIA DE PALAVRAS ===")

    for palavra, qtd in frequencia.items():
        print(f"{palavra}: {qtd}")


if __name__ == "__main__":
    main()