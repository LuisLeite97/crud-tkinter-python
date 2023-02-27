import sqlite3 as lite

con = lite.connect('bdados.db')

# inserção
def inserir_form(i):
    with con: 
        cur=con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_compra, serie, imagem) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query,i)


# update
def atualizar_form(i):
    with con: 
        cur=con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query,i)

# Deleta
def deleta_form(i):
    with con: 
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query, i)


# visualização
def ver_forms():
    ver_dados= []
    with con: 
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows: 
            ver_dados.append(row) 

    return ver_dados

def ver_item(id):
    ver_dados_individual= []
    with con: 
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows: 
            ver_dados_individual.append(row) 

    return ver_item    
