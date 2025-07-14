from app.db.database import get_db_connection # conexão com o BD
from psycopg2 import sql # Trabalha com o BD postgres
from fastapi import Header, HTTPException

def criar_objetivo(descricao: str, vlr_objetivo: float, dt_inicial: str, dt_limite: str, id_usuario: int):
    conn = get_db_connection() 
    if conn is None:
        return {"erro": "Não foi possivel conectar ao banco de dados."}
    # Query para inserir um novo objetivo
    #values os dados que serao inseridos #%s marcar uma consulta sagura
    try:
        with conn.cursor() as cursor:
            
            insert_query = sql.SQL("""
                INSERT INTO objetivo (descricao, vlr_objetivo, dt_inicial, dt_limite, id_usuario)
                VALUES (%s, %s, %s, %s, %s) 
                RETURNING id_objetivo
            """)
            cursor.execute(insert_query, (descricao, vlr_objetivo, dt_inicial, dt_limite,id_usuario)) # id_usuario deve ser passado como argumento
            # id_usuario deve ser passado como argumento, pode ser obtido do token de autenticação
            objetivo_id = cursor.fetchone()[0] # ID do objetivo inserido
            conn.commit()
            return {"id": objetivo_id, "mensagem": "Objetivo criado com sucesso"}

    except Exception as e:
        conn.rollback() #se der erro, desfaz a transação
        return {"erro": str(e)}
    finally:
        conn.close() # fecha a conexão com o banco de dados

def listar_objetivos():
    conn = get_db_connection() # tenta abrir uma conexão com o banco
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}
    # Query para selecionar todos os objetivos
    try:
        with conn.cursor() as cursor:
            select_query = sql.SQL("""
                SELECT id_objetivo, descricao, vlr_objetivo, dt_inicial, dt_limite, id_usuario
                FROM objetivo                
            """)
            cursor.execute(select_query)
            objetivos = cursor.fetchall()
            return [{"id": obj[0], "descricao": obj[1], "vlr_objetivo": obj[2], "dt_inicial": obj[3], "dt_limite": obj[4], "id_usuario": obj[5]} for obj in objetivos]

    except Exception as e:

        return {"erro": str(e)}
    finally:
        conn.close()

def atualizar_objetivo(id_objetivo: int, descricao: str, vlr_objetivo: float, dt_inicial: str, dt_limite: str, id_usuario: int):
    conn = get_db_connection()  # tenta abrir uma conexão com o banco
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}

    print(f"\nAtualizando objetivo: \nid_objetivo: {id_objetivo}, id_usuario: {id_usuario}, descrição: {descricao}, valor: {vlr_objetivo}, dt_inicial: {dt_inicial}, dt_limite: {dt_limite}")

    try:
        with conn.cursor() as cursor:
            update_query = sql.SQL("""
                UPDATE objetivo
                SET descricao = %s, vlr_objetivo = %s, dt_inicial = %s, dt_limite = %s
                WHERE id_objetivo = %s AND id_usuario = %s
            """)

            cursor.execute(update_query, (
                descricao,
                vlr_objetivo,
                dt_inicial,
                dt_limite,
                id_objetivo,
                id_usuario
            ))
            conn.commit()
            return {"mensagem": "Objetivo atualizado com sucesso"}

    except Exception as e:
        print("Erro ao atualizar objetivo:", e)  # Mostra o erro no terminal
        conn.rollback()  # se der erro, desfaz a transação
        return {"erro": str(e)}
    finally:
        conn.close()  # fecha a conexão com o banco de dados
    

def excluir_objetivo(id_objetivo: int):
    conn = get_db_connection() # tenta abrir uma conexão com o banco
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}
    # Query para excluir um objetivo
    try:
        with conn.cursor() as cursor:
            delete_query = sql.SQL("""
                DELETE FROM objetivo
                WHERE id_objetivo = %s
            """)
            cursor.execute(delete_query, (id_objetivo,))
            conn.commit()
            return {"mensagem": "Objetivo excluído com sucesso"}

    except Exception as e:
        conn.rollback()
        print("Erro ao excluir objetivo:", e)  # <- Mostra o erro no terminal
    return {"erro": str(e)}


def obter_usuario_logado(x_user_id: str = Header(None)):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="Usuário não autenticado")
    return {"id": int(x_user_id)}