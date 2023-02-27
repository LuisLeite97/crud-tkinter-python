import sqlite3 as lite

con = lite.connect('bdados.db')

with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE Inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE, valor_compra DECIMAL, serie TEXT, imagem TEXT)")
    cur.execute("CREATE TABLE Paciente ()")
    cur.execute("CREATE TABLE Enfermeira ()")