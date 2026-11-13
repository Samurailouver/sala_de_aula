import Cliente

def criar_clientes(nome: str, telefone: str | None, email: str | None) -> Cliente | None:
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
    
def ler_clientes() -> list[Cliente]:
        clientes = []
        try:
            cursor.execute("SELECT id_cliente, nome, telefone, email FROM cliente ORDER BY id_cliente")
            for linha in cursor.fetchall():
                clientes.append(Cliente(linha[1], linha[2], linha[3], linha[0]))
        except pg.DatabaseError as e:
            print(e)
            conexao.rollback()
        return clientes

def buscar_cliente(id_cliente: int) -> Cliente | None:
        try:
            cursor.execute(
                "SELECT id_cliente, nome, telefone, email FROM cliente WHERE id_cliente = %s",
                (id_cliente,)  # a vírgula faz disso uma tupla
            )
            linha = cursor.fetchone()  # None se nenhuma linha bateu com o WHERE
            if linha:
                return Cliente(linha[1], linha[2], linha[3], linha[0])
        except pg.DatabaseError as e:
            print(e)
            conexao.rollback()
        return None
    
def atualizar_cliente(cliente: Cliente) -> bool:
        try:
            cursor.execute(
                "UPDATE cliente SET nome = %s, telefone = %s, email = %s WHERE id_cliente = %s",
                (cliente.nome, cliente.telefone, cliente.email, cliente.id_cliente)
            )
            alteradas = cursor.rowcount  # 0 = não existe cliente com esse id
            conexao.commit()
            return alteradas > 0
        except pg.DatabaseError as e:
            print(e)
            conexao.rollback()
        return False
    
def deletar_cliente(id_cliente: int) -> bool:
        try:
            cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
            apagadas = cursor.rowcount
            conexao.commit()
            return apagadas > 0
        except pg.DatabaseError as e:
            print(e)  # ex.: o cliente tem agendamento, e a chave estrangeira impede o DELETE
            conexao.rollback()
        return False    