# tests/test_usuario.py

from fastapi.testclient import TestClient
from app.main import app  # Ajuste se seu main.py estiver em outro lugar

client = TestClient(app)

def test_registrar_usuario_sucesso():
    payload = {
        "nome": "João Silva",
        "email": "joao@email.com",
        "senha": "senha123"
    }

    response = client.post("/register", json=payload)

    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["email"] == "joao@email.com"


def test_registrar_usuario_email_duplicado():
    payload = {
        "nome": "João Silva",
        "email": "joao@email.com",
        "senha": "senha123"
    }

    # Primeiro cadastro (sucesso)
    client.post("/register", json=payload)

    # Segundo cadastro com mesmo e-mail (espera erro)
    response = client.post("/register", json=payload)

    assert response.status_code == 400
    assert "detail" in response.json()
