from fastapi.testclient import TestClient
from app.main import app  # importa seu app FastAPI

client = TestClient(app)

def test_criar_usuario_com_sucesso():
    response = client.post("/api/v1/auth/register", json={
        "nome": "Maria Teste",
        "email": "pedro@email.com",
        "telefone": "11988887777",
        "login": "mariateste",
        "senha": "teste123",
        "dt_nascimento": "1995-03-15",
        "cpf": "42984119070"
    })
    assert response.status_code == 201
    assert "id" in response.json()
    
def test_criar_usuario_com_cpf_valido():
    response = client.post("/api/v1/auth/register", json={
        "nome": "João CPF",
        "email": "joaocpf@email.com",
        "telefone": "11999998888",
        "login": "joaocpf",
        "senha": "senha123",
        "dt_nascimento": "1990-05-10",
        "cpf": "12345678901"
    })
    assert response.status_code == 201
    assert "id" in response.json()

def test_criar_usuario_com_cpf_curto():
    response = client.post("/api/v1/auth/register", json={
        "nome": "João CPF Curto",
        "email": "joaocpfcurto@email.com",
        "telefone": "11988887777",
        "login": "joaocurto",
        "senha": "senha123",
        "dt_nascimento": "1991-01-01",
        "cpf": "12345"
    })
    assert response.status_code == 422

def test_criar_usuario_com_cpf_invalido_caracteres():
    response = client.post("/api/v1/auth/register", json={
        "nome": "João CPF Ruim",
        "email": "joaoruim@email.com",
        "telefone": "11912312312",
        "login": "joaoruim",
        "senha": "senha123",
        "dt_nascimento": "1992-03-02",
        "cpf": "abc12345678"  # inválido por conter letras
    })
    assert response.status_code == 422

def test_criar_usuario_com_cpf_duplicado():
    cpf = "99999999999"

    # Primeiro usuário com CPF válido
    res1 = client.post("/api/v1/auth/register", json={
        "nome": "Usuário 1",
        "email": "cpf1@email.com",
        "telefone": "11111111111",
        "login": "usuario1",
        "senha": "senha123",
        "dt_nascimento": "1985-06-20",
        "cpf": cpf
    })
    assert res1.status_code == 201

    # Segundo usuário com mesmo CPF
    res2 = client.post("/api/v1/auth/register", json={
        "nome": "Usuário 2",
        "email": "cpf2@email.com",
        "telefone": "22222222222",
        "login": "usuario2",
        "senha": "senha123",
        "dt_nascimento": "1980-01-01",
        "cpf": cpf
    })
    assert res2.status_code == 400
    assert res2.json()["detail"] == "CPF já cadastrado"

def test_criar_usuario_dados_invalidos():
    response = client.post("/api/v1/auth/register", json={
        "nome": "Ana",
        "email": "email_invalido",
        "telefone": "sem_telefone",
        "login": "",
        "senha": "123",
        "dt_nascimento": "não é data"
    })
    assert response.status_code == 422  
