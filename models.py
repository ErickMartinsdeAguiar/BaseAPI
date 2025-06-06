from pydantic import BaseModel

# Classe de Pessoa
class Pessoa(BaseModel):
    id: str
    nome: str
    data_nascimento: str
    profissao: str
    escolaridade: str
    estado_civil: str
    genero: str

# Classe de Produto
class Produto(BaseModel):
    id: str
    nome_produto: str
    categoria: str