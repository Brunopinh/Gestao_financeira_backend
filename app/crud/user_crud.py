from app.db.database import get_db_connection
from psycopg2 import sql

def get_user_by_email(email: str):
    conn = get_db_connection()
    if conn is None:
        return None

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id_usuario, nome, email FROM usuario
                WHERE email = %s
            """, (email,))
            usuario = cursor.fetchone()
            if usuario:
                return {
                    "id": usuario[0],
                    "nome": usuario[1],
                    "email": usuario[2]
                }
            return None
    except Exception as e:
        # Aqui você pode logar o erro se quiser
        return None
    finally:
        conn.close()


def criar_usuario(nome: str, email: str, telefone: str, login: str, senha: str, dt_nascimento: str):
    conn = get_db_connection()
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}

    try:
        with conn.cursor() as cursor:
            insert_query = sql.SQL("""
                INSERT INTO usuario (nome, email, telefone, login, senha, dt_nascimento)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id_usuario
            """)
            cursor.execute(insert_query, (nome, email, telefone, login, senha, dt_nascimento))
            usuario_id = cursor.fetchone()[0]
            conn.commit()
            return {"id": usuario_id, "mensagem": "Usuário criado com sucesso"}
    except Exception as e:
        conn.rollback()
        return {"erro": str(e)}
    finally:
        conn.close()

def autenticacao_usuario(login: str, senha: str):
    print("Iniciando autenticação do usuário")
    print(f"Login: {login}, Senha: {senha}")
    conn = get_db_connection()
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}

    try:
        with conn.cursor() as cursor:
            select_query = sql.SQL("""
                SELECT id_usuario, nome FROM usuario
                WHERE login = %s AND senha = %s
            """)
            cursor.execute(select_query, (login, senha))
            usuario = cursor.fetchone()
            if usuario:
                return {"id": usuario[0], "nome": usuario[1], "mensagem": "Usuário autenticado com sucesso"}
            else:
                return {"erro": "Email ou senha incorretos"}
    except Exception as e:
        return {"erro": str(e)}
    finally:
        conn.close()