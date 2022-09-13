import PySimpleGUI as sg
import collections
from collections import OrderedDict
import numpy as np
import ibm_db
import ibm_db_dbi
from db import *

loginsucesso = False
conn_string = "DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;PROTOCOL=TCPIP;UID=xrl14403;PWD=lEbtvSLFGIUJwrhC;SECURITY=SSL"



def login():

    sg.set_options(keep_on_top=False)
    sg.theme('LightBrown11')
    telalogin = [

    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Button('Cadastrar Usuario')]

    ]
    return sg.Window('Login', layout=telalogin, finalize=True)

def cadastrousuario():
    cadastrousuario = [
        [sg.Text('Usuario')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Checkbox('Administrador')],
        [sg.Button('Cadastrar')]
    ]
    return sg.Window('Cadastro de Usuario', layout=cadastrousuario, finalize=True)

def telaestoque():
    sg.set_options(auto_size_buttons=True)
    sg.theme('Reddit')

    telaestoque = [
        [sg.Text('Nome')],
        [sg.Input(key='nomeproduto')],
        [sg.Combo(['Bombona', 'Litros', 'Pacote'],size=(10,1))],
        [sg.Button('Cadastrar produto'), ]
    ]

    colunas = ['Produto', 'Medida','asdad']
    


    

    layout = [
        [sg.Table(values = x, headings=colunas, justification='right',
     key='-TABLE-', auto_size_columns=True, row_height=30,max_col_width=30)]
    ]#,key=dbprodu)

    return sg.Window('Estoque', layout=layout, finalize=True,keep_on_top=True, resizable=True)

def telacadastro():
    sg.set_options(auto_size_buttons=True)
    sg.theme('Black')

    telacadastro = [
        [sg.Text('Nome')],
        [sg.Input()],#key='nomeproduto'
        [sg.Combo(['Bombona', 'Litros', 'Pacote'],size=(10,1))],
        [sg.Button('Cadastrar produto')],
        [sg.Button('Deletar Produto')]
    ]
    return sg.Window('Estoque', layout=telacadastro, finalize=True)
def telainicial():
    sg.theme('DarkPurple')
    sg.set_options(auto_size_buttons=True)

    telainicial = [

        [sg.Button('Cadastro'),sg.Button('Estoque')],


    ]

    return sg.Window('Tela Inicial', layout=telainicial, finalize=True)

janela1, janela2, janela3 = login(), None, None

while True:
    conn = ibm_db_dbi.connect(conn_string,"","")
    xx = np.random.randint(1,100)
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED: #FECHAR JANELA
        if window == janela1:
           break

        if window == janela2:
            janela1 = login()
            janela2.close()

        if window == janela3:
            janela2 = telainicial()
            janela3.close()

    elif window == janela1 and event == 'Login': #BOTAO LOGIN TELA INICIAL
        usuariologin = values['usuario']
        passwordlogin = values['senha']
        #usuariologin = '1'
        #passwordlogin = '1'
        #conn = ibm_db_dbi.connect(conn_string,"","")
        
        print(conn)
        if conn:
            
            #passwordlogin = list(passwordlogin)
            cur = conn.cursor()
            usuariologin = list(usuariologin)
            #selectQuery = 'select * from Logins WHERE USERNAME = %s',(usuariologin) 
            #stmt = ibm_db.exec_immediate(conn, selectQuery)
            print(usuariologin)
            
            #(Select * from data WHERE data.field = ?),con,Params=[variable])
            queryLogin = "SELECT * from Logins WHERE USERNAME = ? and PASSWORD = ?"
            #queryPASS = "SELECT * from Logins WHERE USERNAME = ?"            
            cur.execute(queryLogin, (usuariologin, passwordlogin))
            row=cur.fetchall()
            print(len(row))
            if (len(row)) != 0:
                cur.close()                
                #cur = conn.cursor()
                loginsucesso = True
                #senha = cur.execute('SELECT PASSWORD from Logins WHERE USERNAME = ? PASSWORD = ?',(usuariologin, passwordlogin))
                #row=cur.fetchall()
                #if length(row)<1:
                #    cur.close()                    
                #    loginsucesso = True
                #else:
                #    cur.close()
                #    sg.popup("Password incorreto")
            else:
                cur.close()
                
                sg.popup("Login ou Senha incorreto")
        else:
            cur.close()
            sg.popup("Banco de dados indisponivel no momento!")


        if loginsucesso == True:
            janela2 = telainicial()
            janela1.close()
            loginsucesso == False

    elif window == janela1 and event == 'Cadastrar Usuario': #MUDAR PARA TELA CADASTRAR USUARIO BOTAO TELA INICIAL
        janela2 = cadastrousuario()
        janela1.close()

    elif window == janela2 and event == 'Cadastrar': #CADASTRAR USUARIO TELA INICIAL
        conn = ibm_db_dbi.connect(conn_string,"","")
        #cur = conn.cursor()
        usuariocadast = list(values['usuario'])
        passwordcadast = list(values['senha'])
        print(usuariocadast)
        print(passwordcadast)
        insertQuery = 'insert into Logins values where USERNAME = (?) AND PASSWORD = (?)'
        #cur.execute(insertQuery, (usuariocadast, passwordcadast))  
        #cur.close() 
        execute_query(conn, insertQuery(usuariocadast,passwordcadast))
        sg.popup('Usuario cadastrado com sucesso')

    elif window == janela2 and event == 'Estoque': #MUDAR PARA TELA DE ESTOQUE
        janela3 = telaestoque()
        janela2.close()

    elif window == janela2 and event == 'Cadastro': #MUDAR PARA TELA DE CADASTRO DE PRODUTO
        janela3 = telacadastro()
        janela2.close()

    elif window == janela3 and event == 'Cadastrar produto': #CADASTRAR PRODUTO
        data={"nome":values[0],"medida":values[0]}
        
        sg.popup('Produto Cadastrado com Sucesso')

    elif window == janela3 and event == 'Deletar Produto': #DELETAR PRODUTO
        sg.popup("Produto Deletado Com Sucesso")