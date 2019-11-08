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
        Id_Motorista INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        n_documento TEXT NOT NULL
        ); '''
        )
        con.close()
    
    def criar_tabela_motorista_vs_adm():
        con = sqlite3.connect('mot_vs_adm.db') 
        cursor = con.cursor() 

        cursor.execute(
        ''' 
        CREATE TABLE IF NOT EXISTS mot_vs_adm ( 
        id_mot_vs_adm INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        id INTEGER NOT NULL,
        Id_Motorista INTEGER NOT NULL,
        FOREIGN KEY(id) REFERENCES dados_adm(id)
        FOREIGN KEY(Id_Motorista) REFERENCES dados_motorista(Id_Motorista)
        ); '''
        )
        con.close()
        #name TEXT NOT NULL, 
        #n_documento TEXT NOT NULL,
    
    def insert_ids_mot_vs_adm(IdAdm, IdMot):
        con = sqlite3.connect('mot_vs_adm.db') 
        cursor = con.cursor()
        cursor.execute(
        """ 
        INSERT INTO mot_vs_adm (id , Id_Motorista) 
        VALUES (?,?) 
        """,(IdAdm, IdMot))

        con.commit() 
        cursor.close()
        con.close()

    def insert_val_motorista(nome, n_documento):
        con = sqlite3.connect('motorista.db') 
        cursor = con.cursor()
        cursor.execute(
        """ 
        INSERT INTO dados_motorista (name, n_documento) 
        VALUES (?,?) 
        """,(nome,n_documento))

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