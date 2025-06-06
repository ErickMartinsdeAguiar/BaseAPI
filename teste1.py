import json

def carregar_dados():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            # Verifica se o arquivo contém as chaves necessárias
            if "pessoas" not in dados or "produtos" not in dados:
                return {"pessoas": [], "produtos": []}
            return dados
    except FileNotFoundError:
        # Caso o arquivo não exista, inicializamos com dados vazios
        return {"pessoas": [], "produtos": []}
    except json.JSONDecodeError:
        # Caso o arquivo tenha dados inválidos, inicializamos com dados vazios
        return {"pessoas": [], "produtos": []}
