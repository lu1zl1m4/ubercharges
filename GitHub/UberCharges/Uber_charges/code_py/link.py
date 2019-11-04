from flask import Flask, request, render_template
import testeadm_1110, bancodedados
import pdf_file 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('LoginADM.html')

@app.route("/login", methods=["POST"])
def login():
    
    login = str(request.form["nome"])
    senha = str(request.form["senha"])
    
    bd = bancodedados.BancoDados
    adm = testeadm_1110.Adm(login,senha,bd)

    if request.method == 'POST':
        if request.form['button'] == 'Login':
            if login == "" and senha == "":
                return render_template('LoginADM.html')

            if adm.verify_login(login,senha) == 1:
                return render_template('PaginaPrincipal.html')

            elif adm.verify_login(login,senha) == 3:
                return render_template('SenhaIncorreta.html') 

            elif adm.verify_login(login,senha) == 2:
                return render_template('NomeAdmIncorreto.html')                
 
            elif adm.verify_login(login,senha) == 4: 
                return render_template('ADMNaoCadastrado.html')
                
        if request.form['button'] == 'Cadastrar':
            return render_template('CadastrarADM.html')
            
@app.route("/ADMnaocadastrado", methods=["POST"])
def voltar():
    if request.form['button'] == 'Voltar':
        return render_template('LoginADM.html')

@app.route("/ADM", methods=["POST"])
def cadastro_adm():

    verifica_bom_senso = True
    nome = str(request.form["nome"].title())
    senha = str(request.form["senha"])
    cpf = str(request.form["CPF"])
    
    bd = bancodedados.BancoDados
    adm = testeadm_1110.Adm(login, senha, bd, cpf) 

    if (not "".join(nome.split()).isalpha()):
        verifica_bom_senso = False
    
    if (not cpf.isdigit() or len(cpf)!=11):
        verifica_bom_senso = False

    if request.form["button"] == 'Cadastrar':
        if adm.verify_cadastro(nome, senha, cpf):
            return render_template('AdmJaCadastrado.html')
    
        elif not adm.verify_cadastro(nome, senha, cpf):
            if verifica_bom_senso == True:    
                bd.insert_val_adm(nome, senha, cpf)
                #bd.update_value(8,nome, senha, cpf)
                return render_template('ADMcadastrado.html')
        
            elif verifica_bom_senso == False:
                return "Nome ou cpf inválidos" 

    if request.form["button"] == 'Voltar':
        return render_template('LoginADM.html')


@app.route("/principal", methods=["POST"])
def principal():
    
    if request.method == 'POST':
        
        if request.form['button'] == 'Novo Motorista':
            return render_template('NovoMotorista.html')
        
        elif request.form['button'] == 'Nova Viagem':
            return render_template('NovaViagem.html')
        
        elif request.form['button'] == 'Inserir Gastos Extras':
            return render_template('GastosExtras.html')
        
        elif request.form['button'] == 'Pagar Motorista':
            return render_template('PagarMotorista.html')
        
        elif request.form['button'] == 'Balanço':
            return render_template('Balanco.html')
        
        elif request.form['button'] == 'Logout':
            return render_template('LoginADM.html')

          
@app.route("/Mcadastrado", methods=["POST"])
def Mcadastrado():
#O PROBLEMA É Q NÃO CONSIGO PEGAR OS VALORES(NOME E SENHA) DA PÁGINA DE LOGIN, SEM Q O  
#USUÁRIO ESCREVA NOVAMENTE, P/ REUTILIZAR NO CADASTRO DO MOTORISTA, ISSO PQ QUERO O ID_ADM.
# LOGO, ESSA PARTE ESTÁ EM ANÁLISE.     
    login = str(request.form["nome"])
    senha = str(request.form["senha"])
    
    nome = str(request.form["nome"].title())
    documento = str(request.form["Ndocumento"])
    bd = bancodedados.BancoDados
    mot = testeadm_1110.Motorista(nome,documento,bd)
    adm = testeadm_1110.Adm(login,senha,bd)

    if request.method == 'POST':
        
        if request.form['button'] == 'Cadastrar':
            if not mot.verify_motorista(nome,documento):
                id_adm = adm.retorna_id_adm_logado()
                bd.insert_val_motorista(nome, documento, id_adm)
                return render_template('MotoristaCadastrado.html')
        
            elif mot.verify_motorista(nome,documento):
                return("Motorista já cadastrado.")
    
    if request.form["button"] == 'Voltar':
        return render_template('PaginaPrincipal.html')
#acaba aqui a análise

@app.route("/PaginaPrincipal", methods=["POST"])
def PaginaPrincipal():

    if request.form['button'] == 'Voltar':
        return render_template('LoginADM.html')

@app.route("/PaginaPrincipal01", methods=["POST"])
def PaginaPrincipal01():

    if request.form['button'] == 'Voltar':
        return render_template('CadastrarADM.html')

            

@app.route("/Nviagem", methods=["POST"])
def Mviagem():

    cliente = str(request.form["cliente"])
    NomeMotorista = str(request.form["Nmotorista"])

    if request.method == 'POST':
        
        if request.form['button'] == 'Continuar':
            return render_template('DadosViagem.html')
        
        elif request.form['button'] == 'Voltar':
            return render_template('PaginaPrincipal.html')


@app.route("/Extras", methods=["POST"])
def GastosExtras():

    ValorCarga = str(request.form["valor"])
    
    text = str(request.form["tex"])
    tipo = str(request.form["tipo_carga"])
    
    if request.method == 'POST': 
        
        if request.form['button'] == 'Salvar':
            return render_template('DespesasAtualizadas.html')
        
        elif request.form['button'] == 'Voltar':
            return render_template('PaginaPrincipal.html')


app.run()