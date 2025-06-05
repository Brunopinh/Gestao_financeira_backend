from app.db.database import get_db_connection
from psycopg2 import sql

def criar_usuario(nome: str, email: str, telefone: str, login: str, senha: str, dt_nascimento: str):
    conn = get_db_connection()
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}

    try:
        with conn.cursor() as cursor:
            insert_query = sql.SQL("""
                INSERT INTO usuarios (nome, email, telefone, login, senha, dt_nascimento)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
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
