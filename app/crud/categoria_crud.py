from app.db.database import get_db_connection
from psycopg2 import sql
from fastapi import Header, HTTPException

def criar_categoria(tp_movimentacao: str, descricao: str):
    if tp_movimentacao not in ["E", "S"]:
        return {"erro": "Tipo de movimentação inválido. Use 'E' ou 'S'."}

    conn = get_db_connection()
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}

    try:
        with conn.cursor() as cursor:
            insert_query = sql.SQL("""
                INSERT INTO categoria (tp_movimentacao, descricao)
                VALUES (%s, %s)
                RETURNING id_categoria
            """)
            cursor.execute(insert_query, (tp_movimentacao, descricao))
            id_categoria = cursor.fetchone()[0]
            conn.commit()
            return {"id_categoria": id_categoria, "mensagem": "Categoria criada com sucesso"}
    except Exception as e:
        conn.rollback()
        return {"erro": str(e)}
    finally:
        conn.close()

def listar_categorias():
    conn = get_db_connection()
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}

    try:
        with conn.cursor() as cursor:
            select_query = sql.SQL("""
                SELECT id_categoria, tp_movimentacao, descricao
                FROM categoria
            """)
            cursor.execute(select_query)
            categorias = cursor.fetchall()
            resultado = []
            for cat in categorias:
                resultado.append({
                    "id_categoria": cat[0],
                    "tp_movimentacao": cat[1],
                    "descricao": cat[2]
                })
            return resultado
    except Exception as e:
        return {"erro": str(e)}
    finally:
        conn.close()

def atualizar_categoria(id_categoria: int, tp_movimentacao: str, descricao: str):
    if tp_movimentacao not in ["E", "S"]:
        return {"erro": "Tipo de movimentação inválido. Use 'E' ou 'S'."}

    conn = get_db_connection()
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}

    try:
        with conn.cursor() as cursor:
            update_query = sql.SQL("""
                UPDATE categoria
                SET tp_movimentacao = %s, descricao = %s
                WHERE id_categoria = %s
            """)
            cursor.execute(update_query, (tp_movimentacao, descricao, id_categoria))
            conn.commit()
            return {"mensagem": "Categoria atualizada com sucesso"}
    except Exception as e:
        conn.rollback()
        return {"erro": str(e)}
    finally:
        conn.close()

def excluir_categoria(id_categoria: int):
    conn = get_db_connection()
    if conn is None:
        return {"erro": "Não foi possível conectar ao banco de dados."}

    try:
        with conn.cursor() as cursor:
            # Verifica se a categoria existe
            cursor.execute("SELECT 1 FROM categoria WHERE id_categoria = %s", (id_categoria,))
            if cursor.fetchone() is None:
                return {"erro": "Categoria não encontrada"}

            
            delete_query = sql.SQL("""
                DELETE FROM categoria WHERE id_categoria = %s
            """)
            cursor.execute(delete_query, (id_categoria,))
            conn.commit()
            return {"mensagem": "Categoria excluída com sucesso"}
    except Exception as e:
        conn.rollback()
        return {"erro": str(e)}
    finally:
        conn.close()

