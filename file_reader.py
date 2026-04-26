def ler_arquivo(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:
        return "ERRO: arquivo não encontrado."

    except UnicodeDecodeError:
        return "ERRO: problema de encoding."

    except Exception as e:
        return f"ERRO inesperado: {str(e)}"