from flask import Flask, request, render_template

#from Gerenciamento de Cargas import testeadm_1110

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('LoginADM.html')

@app.route("/login", methods=["POST"])
def login():
    
    Login = str(request.form["nome"])
    Senha = str(request.form["senha"])

    if request.method == 'POST':
        if request.form['button'] == 'Login':
            return render_template('PaginaPrincipal.html')
        elif request.form['button'] == 'Cadastrar':
            return render_template('CadastrarADM.html')
            
@app.route("/ADM", methods=["POST"])
def ADM():
    
    nome = str(request.form["nome"])
    senha = str(request.form["senha"])
    CPF = str(request.form["CPF"])

    if request.method == 'POST':
        if request.form['button'] == 'Cadastrar':
            return render_template('ADMcadastrado.html')
        elif request.form['button'] == 'Voltar':
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

    Nome = str(request.form["nome"])
    documento = str(request.form["Ndocumento"])

    if request.method == 'POST':
        
        if request.form['button'] == 'Cadastrar':
            return render_template('MotoristaCadastrado.html')

@app.route("/PaginaPrincipal", methods=["POST"])
def PaginaPrincipal():

    if request.method == 'POST':
        
        if request.form['button'] == 'Voltar':
            return render_template('PaginaPrincipal.html')

@app.route("/Nviagem", methods=["POST"])
def Nviagem():

    cliente = str(request.form["cliente"])
    NomeMotorista = str(request.form["Nmotorista"])
    intinerário = str(request.form["intn"])

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