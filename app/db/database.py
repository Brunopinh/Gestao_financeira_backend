import os
from dotenv import load_dotenv
import psycopg2

# Carrega as variáveis de ambiente do arquivo .env
# É uma boa prática chamar load_dotenv() no início do seu script
load_dotenv()

# Recupera as variáveis de ambiente
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

def get_db_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Conexão com o banco de dados estabelecida com sucesso!")
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        # Você pode querer levantar uma exceção aqui ou lidar com o erro de outra forma
        return None

# Exemplo de uso:
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        # Você pode usar a conexão aqui
        # Ex: cursor = connection.cursor()
        #     cursor.execute("SELECT 1;")
        #     print(cursor.fetchone())
        connection.close()
        print("Conexão com o banco de dados fechada.")