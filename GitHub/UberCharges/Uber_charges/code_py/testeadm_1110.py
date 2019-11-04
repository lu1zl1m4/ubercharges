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

    def __init__(self,nome,senha,obj_bd,cpf = '00000000000'):

        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.obj_bd = obj_bd

    def verify_login(self,nome, senha):

        dados_db = self.obj_bd.get_value_adm()
        logado = 0
        for element_adm in dados_db:
            if nome == element_adm[1] and senha == element_adm[2]:
                id_adm = element_adm[0]
                #print(id_adm)
                logado = 1
                break
                
            elif nome != element_adm[1] and senha == element_adm[2]:
                logado = 2
                break 
            
            elif nome == element_adm[1] and senha != element_adm[2]:
                logado = 3
                break
            
            elif nome != element_adm[1] and senha != element_adm[2]:
                logado = 4
                break

        return logado

    def retorna_id_adm_logado():    
        dados_db = self.obj_bd.get_value_adm()
        for element_adm in dados_db:
            if self.nome == element_adm[1] and self.senha == element_adm[2]:
                id_adm = element_adm[0]
        return id_adm

    def verify_cadastro(self, nome, senha, cpf):

        dados_db = self.obj_bd.get_value_adm()
        cadastro = 0
        for element in dados_db:
            if nome in element and senha in element and cpf in element:
                cadastro = True
                break
            else:
                cadastro = False
        return cadastro

class Motorista(Adm):
	
    def __init__(self,nome_mot, n_documento,obj_bd):
        #super().__init__(nome)
        self.nome_mot = nome_mot
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