import datetime 
import psycopg2 as pg

conexao = pg.connect(
    dbname = "centro esportivo",
    password = "1234",
    user = "postgres",
    host = "localhost",
    port = "5432"
)


cursor = conexao.cursor(pg.connect)


def criar_cliente(nome: str, telefone: str | None, email: str | None) -> Cliente | None:
        try:
            cursor.execute(
                "INSERT INTO cliente (nome, telefone, email) "
                "VALUES (%s, %s, %s) RETURNING id_cliente",
                (nome, telefone, email)
            )
            id_cliente = cursor.fetchone()[0]  # o id que o SERIAL acabou de gerar
            conexao.commit()
            return Cliente(nome, telefone, email, id_cliente)
        except pg.DatabaseError as e:
            print(e)
            conexao.rollback()
        return None
