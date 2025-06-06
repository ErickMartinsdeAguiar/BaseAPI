from pydantic import BaseModel

# Modelo para adicionar uma nova Pessoa (POST)
class PessoaCriacao(BaseModel):
    nome: str
    data_nascimento: str
    profissao: str
    escolaridade: str
    estado_civil: str
    genero: str

# Modelo para adicionar um novo Produto (POST)
class ProdutoCriacao(BaseModel):
    nome_produto: str
    categoria: str
