from fastapi.testclient import TestClient
from app.main import app  # importa seu app FastAPI

client = TestClient(app)

def test_criar_usuario():
    response = client.post("/api/v1/auth/register", json={
        
        "email": "ricardo@email.com",
        "telefone": "11999999999",
        "login": "joaosilva",
        "senha": "senha123",
        "dt_nascimento": "1990-05-10"
    })
    assert response.status_code == 201  
    assert "id" in response.json()

def test_criar_usuario_com_sucesso():
    response = client.post("/api/v1/auth/register", json={
        "nome": "Maria Teste",
        "email": "maria@email.com",
        "telefone": "11988887777",
        "login": "mariateste",
        "senha": "teste123",
        "dt_nascimento": "1995-03-15"
    })
    assert response.status_code == 201
    assert "id" in response.json()

def test_criar_usuario_com_email_duplicado():
    # Primeiro cadastro
    client.post("/api/v1/auth/register", json={
        "nome": "Pedro",
        "email": "pedro@email.com",
        "telefone": "11912345678",
        "login": "pedro1",
        "senha": "senha123",
        "dt_nascimento": "1992-01-01"
    })
    # Segundo com mesmo email
    response = client.post("/api/v1/auth/register", json={
        "nome": "Pedro Clone",
        "email": "pedro@email.com",  
        "telefone": "11900000000",
        "login": "pedro2",
        "senha": "senha456",
        "dt_nascimento": "1994-02-02"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "E-mail já cadastrado"


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
