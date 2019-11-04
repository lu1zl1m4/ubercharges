import sqlite3

class BancoDados:


    def criar_tabela_adm():
        con = sqlite3.connect('adm.db') 
        cursor = con.cursor() 

        cursor.execute(
        ''' 
        CREATE TABLE IF NOT EXISTS dados_adm( 
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        senha TEXT NOT NULL, 
        cpf VARCHAR(11) NOT NULL 
        ); 
        '''
        )
        con.close()


    def insert_val_adm(nome, senha, cpf):
        con = sqlite3.connect('adm.db') 
        cursor = con.cursor()
        cursor.execute(
        """ 
        INSERT INTO dados_adm (name, senha, cpf) 
        VALUES (?,?,?) 
        """,(nome,senha,cpf))

        con.commit() 
        cursor.close()
        con.close()
        

    def get_value_adm():
        con = sqlite3.connect('adm.db') 
        cursor = con.cursor()

        cursor.execute("""
        SELECT * FROM dados_adm;
        """)

        elements = cursor.fetchall()
        return elements

    def update_value(id_dados_adm, novo_nome, nova_senha, novo_cpf):
        con = sqlite3.connect('adm.db') 
        cursor = con.cursor() 
    	    
        cursor.execute("""
        UPDATE dados_adm
        SET name = ?, senha = ?, cpf=?
        WHERE id = ?
        """, (novo_nome, nova_senha, novo_cpf, id_dados_adm))
        con.commit()
        con.close()  

    def criar_tabela_motorista():
        con = sqlite3.connect('motorista.db') 
        cursor = con.cursor() 

        cursor.execute(
        ''' 
        CREATE TABLE IF NOT EXISTS dados_motorista( 
        IdMotorista INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        n_documento TEXT NOT NULL,
        id INTEGER NOT NULL,
        FOREIGN KEY(id) REFERENCES dados_adm(id)
        ); '''
        )
        con.close()

    def insert_val_motorista(nome, n_documento, id):
        con = sqlite3.connect('motorista.db') 
        cursor = con.cursor()
        cursor.execute(
        """ 
        INSERT INTO dados_motorista (name, n_documento, id) 
        VALUES (?,?,?) 
        """,(nome,n_documento, id))

        con.commit() 
        cursor.close()
        con.close()

    def get_value_motorista():
        con = sqlite3.connect('motorista.db') 
        cursor = con.cursor()

        cursor.execute("""
        SELECT * FROM dados_motorista;
        """)

        elements = cursor.fetchall()
        return elements


DB = BancoDados
DB.criar_tabela_adm()
DB.criar_tabela_motorista()
print(DB.get_value_adm())