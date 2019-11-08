import sqlite3
import bancodedados
#x = float (input("Escolha um valor:"))
class Viagem:

    def __init__(self, tempo, local_partida, destino, distancia, num_viag_longa, num_viag_curta, n_viagens):
        self.tempo=tempo
        self.local_partida=local_partida
        self.destino=destino
        self.distancia=distancia
        self.num_viag_longa=num_viag_longa
        self.num_viag_curta=num_viag_curta
        self.n_viagens=n_viagens

    def cont_viag_curta(self,distancia):

        if (distancia < 500):
            self.num_viag_curta +=1
        return self.num_viag_curta
                        
    def cont_viag_longa(self,distancia):

        if (distancia >= 500):
            self.num_viag_longa +=1
        return self.num_viag_longa

    def contador_de_viagens(self):
        self.n_viagens= self.cont_viag_longa + self.cont_viag_curta
        return self.n_viagens 

class Carga:

    def __init__ (self, codigo, peso, val_atual):
        self.codigo = codigo
        self.peso = peso
        self.valor= val_atual
        
    def soma_val (self,val_atual):
    
        self.valor += val_atual 
        
        return self.valor 

class Custos(Carga, Viagem):

    def __init__(self, almoco, manutencao, pedagio, diesel, carga,viagem):
        self.almoco=almoco
        self.manutencao=manutencao
        self.pedagio=pedagio
        self.diesel=diesel
        self.carga=carga
        self.viagem=viagem

    def calcula_salario(self, valor, distancia):
        salario = ((self.carga.soma_val(x))*0.11 + 20*self.viagem.num_viag_curta + 50*self.viagem.num_viag_longa)
        #return salario
class Adm:

    def __init__(self, nome , senha, obj_bd, cpf = '00000000000'):

        self.nome = nome
        self.senha = senha
        self.obj_bd = obj_bd
        self.cpf = cpf

    def verify_login(self, cpf, senha):

        db = bancodedados.BancoDados
        dados_db = db.get_value_adm()
    
        for element in dados_db:

            if cpf == element[3] and senha == element[2]:
                logado = 1
                break

            if cpf == element[3] and senha != element[2]:
                logado = 2
                break

            if cpf != element[3] and senha != element[2]:
                logado = 4
                
            elif cpf != element[3] and senha == element[2]:
                logado = 3
                break
                
        return logado

    def retorna_id_adm_logado(self, cpf, senha):    
        db = bancodedados.BancoDados
        dados_db = db.get_value_adm()
        cadastro = 0
        
        for element in dados_db:
            if senha == element[2] and cpf == element[3]:
                id_adm = element[0]
                break
            
        return id_adm

    def verify_cadastro(self, nome, senha, cpf):

        dados_db = self.obj_bd.get_value_adm()
        cadastro = 0
        
        for element in dados_db:
            if nome == element[1] and senha == element[2] and cpf == element[3]:
                cadastro = True
                break
            else:
                cadastro = False
        return cadastro
    
    def verify_user(self, nome, cpf):

        dados_db = self.obj_bd.get_value_adm()
        existente = 0
        
        for element in dados_db:
            if nome == element[1] and cpf == element[3]:
                existente = True
                break
            else:
                existente = False
        return existente

    def retorna_id_user_para_redefinir_senha(self, nome, cpf):    
        db = bancodedados.BancoDados
        dados_db = db.get_value_adm()
        
        for element in dados_db:
            if nome == element[1] and cpf == element[3]:
                id_adm = element[0]
                break
            
        return id_adm

class Motorista(Adm):
	
    def __init__(self,nome, n_documento,obj_bd):
        #super().__init__(nome)
        self.nome = nome
        self.n_documento = n_documento
        self.obj_bd = obj_bd
    
    def verify_motorista(self,nome,documento):
        
        dados_db = self.obj_bd.get_value_motorista()
        cadastro = 0
        for element in dados_db:
            if nome in element and documento in element:
                cadastro = True
                break
            else:
                cadastro = False
        return cadastro

    def retorna_id_mot_cadastrado(self):    
        dados_db = self.obj_bd.get_value_motorista()
        for element_mot in dados_db:
            if self.nome == element_mot[1] and self.n_documento == element_mot[2]:
                self.id_mot = element_mot[0]
        return self.id_mot

cargas = Carga("EEEL",10,10)
viagem1= Viagem(24, 'RJ' , 'SP', 234, 2, 3, 5)
carol=Custos(45,63,21,67,cargas,viagem1)
db = bancodedados.BancoDados
adm = Adm("Humans","Machines", db)
#print(adm.verify_login("Humans", "Machines"))

'''
qq=Motorista("tomas", 111111111111)
print(qq.nome_mot, qq.n_documento)
print(carol.calcula_salario(10,5))
db = bancodedados.BancoDados
adm = Adm("Carol","BUDA",db)
print(adm.verify("Carol","BUDA"))'''