import PySimpleGUI as sg
import collections
from collections import OrderedDict
import ibm_db
from db.py import databaseOn, databaseOff
import numpy as np

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

janela1 = login()

while True:    
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
        user = 
        result = db.child("Logins").order_by_child("usuario").equal_to(usuariologin).limit_to_first(1).get()

        if bool(result.val()) == True:

            pasword = db.child("Logins").order_by_child("senha").equal_to(passwordlogin).limit_to_first(1).get()
            if bool(pasword.val()) == True:
                loginsucesso = True
            else:
                sg.popup("Password incorreto")

        else:
            sg.popup("Login incorreto")


        if loginsucesso == True:
            janela2 = telainicial()
            janela1.close()
            loginsucesso == False

 
    
