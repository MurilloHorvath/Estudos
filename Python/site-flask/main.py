from flask import Flask, render_template, redirect, request, flash, send_from_directory
import json
import ast
import os
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

logado = False

@app.route('/')
def home():
    global logado
    logado = False
    return render_template('login.html')


@app.route('/adm')
def adm():
    if logado == True:
        conect_BD = mysql.connector.connect(host='localhost', database='usuarios', user='root', password='')
        
        if conect_BD.is_connected():
            print('conectado')
            cursur = conect_BD.cursor()
            cursur.execute('select * from usuario;')
            usuarios = cursur.fetchall()
        
        return render_template("administrador.html",usuarios=usuarios)
    
    if logado == False:
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    global logado

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    conect_BD = mysql.connector.connect(host='localhost', database='usuarios', user='root', password='')
    cont = 0
    if conect_BD.is_connected():
        print('conectado')
        cursur = conect_BD.cursor()
        cursur.execute('select * from usuario;')

        usuariosBD = cursur.fetchall()

        for usuario in usuariosBD:
            cont+=1
            usuarioNome = str(usuario[1])
            usuarioSenha = str(usuario[2])

            if nome == 'adm' and senha == '000':
                logado = True
                return redirect('/adm')

            if usuarioNome == nome and usuarioSenha == senha:
                logado = True
                return redirect("/usuario")
            
            if cont>=len(usuariosBD):
                flash('Usuario Inválido')
                return redirect("/")
    else:
        return redirect('/')


@app.route('/usuario')
def usuario():
    if logado == True:
        arquivo = []
        for documento in os.listdir('arquivos'):
            arquivo.append(documento)
        return render_template("usuario.html", arquivos=arquivo)
    
    else:

        return redirect("/")


@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    global logado
    user = []
    nome = request.form.get('nome')
    senha = request.form.get('senha')
   
    conect_BD = mysql.connector.connect(host='localhost', database='usuarios', user='root', password='')

    if conect_BD.is_connected():
        cursur = conect_BD.cursor()
        cursur.execute(f"insert into usuario values(default,'{nome}','{senha}');")

    if conect_BD.is_connected():
        cursur.close()
        conect_BD.close()

    logado = True
    flash(f'Usuário {nome} Cadastrado')
    return redirect("/adm")


@app.route('/excluirUsuario', methods=['POST'])
def excluirUsuário():
    global logado
    logado = True

    usuarioID = request.form.get('Usuario_Para_Excluir')
    nome = request.form.get('nome')

    conect_BD = mysql.connector.connect(host='localhost', database='usuarios', user='root', password='')

    if conect_BD.is_connected():
        cursur = conect_BD.cursor()
        cursur.execute(f"delete from usuario where id='{usuarioID}';")

    if conect_BD.is_connected():
        cursur.close()
        conect_BD.close()

    flash(f'Usuário {nome} Excluido')
    return redirect('/adm')


@app.route("/upload", methods=['POST'])
def upload():
    global logado
    logado = True

    arquivo = request.files.get('documento')
    nome_arquivo = arquivo.filename.replace(' ' , "_")
    arquivo.save(os.path.join('arquivos', nome_arquivo))

    flash('Arquivo Enviado')
    return redirect('/adm')


@app.route('/download', methods=['POST'])
def download():
    nomeArquivo = request.form.get('arquivosParaDownload')

    return send_from_directory('arquivos', nomeArquivo, as_attachment=True)




if __name__ in "__main__":
    app.run(debug=True)