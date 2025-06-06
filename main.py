from fastapi import FastAPI, HTTPException
from models import Pessoa, Produto
from schemas import PessoaCriacao, ProdutoCriacao
import json

# Inicializa a aplicação FastAPI
app = FastAPI()

# Vamos simular um banco de dados com um arquivo JSON
def carregar_dados():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'pessoas': [], 'produtos': []}

def salvar_dados(dados):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)

# Rotas para Pessoas (Usuários)
@app.get("/usuarios")
def listar_usuarios():
    dados = carregar_dados()
    return dados['pessoas']

@app.get("/usuarios/{id}")
def obter_usuario(id: str):
    dados = carregar_dados()
    pessoa = next((p for p in dados['pessoas'] if p['id'] == id), None)
    if pessoa is None:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoa

@app.post("/-usuarios")
def criar_usuario(usuario: PessoaCriacao):
    dados = carregar_dados()
    novo_id = str(len(dados['pessoas']) + 1)  # Simulando a criação de um novo ID
    nova_pessoa = Pessoa(id=novo_id, **usuario.dict())
    dados['pessoas'].append(nova_pessoa.dict())
    salvar_dados(dados)
    return {"mensagem": f"Usuário {nova_pessoa.nome} criado com sucesso!"}

@app.delete("/usuarios/{id}")
def deletar_usuario(id: str):
    dados = carregar_dados()
    pessoa = next((p for p in dados['pessoas'] if p['id'] == id), None)
    if pessoa is None:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    dados['pessoas'] = [p for p in dados['pessoas'] if p['id'] != id]
    salvar_dados(dados)
    return {"mensagem": "Usuário deletado com sucesso!"}

@app.patch("/usuarios/{id}")
def atualizar_usuario(id: str, usuario: PessoaCriacao):
    dados = carregar_dados()
    pessoa = next((p for p in dados['pessoas'] if p['id'] == id), None)
    if pessoa is None:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    pessoa.update(usuario.dict())
    salvar_dados(dados)
    return {"mensagem": "Usuário atualizado com sucesso!"}

# Rotas para Produtos
@app.get("/produtos")
def listar_produtos():
    dados = carregar_dados()
    return dados['produtos']

@app.get("/produtos/{id}")
def obter_produto(id: str):
    dados = carregar_dados()
    produto = next((p for p in dados['produtos'] if p['id'] == id), None)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.post("/produtos")
def criar_produto(produto: ProdutoCriacao):
    dados = carregar_dados()
    novo_id = str(len(dados['produtos']) + 1)
    novo_produto = Produto(id=novo_id, **produto.dict())
    dados['produtos'].append(novo_produto.dict())
    salvar_dados(dados)
    return {"mensagem": f"Produto {novo_produto.nome_produto} criado com sucesso!"}

@app.delete("/produtos/{id}")
def deletar_produto(id: str):
    dados = carregar_dados()
    produto = next((p for p in dados['produtos'] if p['id'] == id), None)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    dados['produtos'] = [p for p in dados['produtos'] if p['id'] != id]
    salvar_dados(dados)
    return {"mensagem": "Produto deletado com sucesso!"}

@app.patch("/produtos/{id}")
def atualizar_produto(id: str, produto: ProdutoCriacao):
    dados = carregar_dados()
    p = next((p for p in dados['produtos'] if p['id'] == id), None)
    if p is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    p.update(produto.dict())
    salvar_dados(dados)
    return {"mensagem": "Produto atualizado com sucesso!"}
