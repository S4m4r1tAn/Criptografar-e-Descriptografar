import PySimpleGUI as sg
import main
from datetime import date

sg.theme('SandyBeach')

layout = [[sg.Text('Qual eh o seu nome?'), sg.Input(key='nome')],
          [sg.Text('Em que ano voce nasceu?'), sg.Input(key='ano')],
          [sg.Button('Calcular idade'), sg.Button('Sair')],
          [sg.Text(size=(40, 2), key='output')]]

window = sg.Window('Calculadora de Idade').Layout(layout)

while True:
    event, values = window.Read()
    
    if event == 'Sair' or event == sg.WIN_CLOSED:
        break
    
    if event == 'Calcular idade':
        nome = values['nome']
        nascimento = int(values['ano'])
        data_de_hoje = date.today().year
        idade = data_de_hoje - nascimento
        output = f'Meu nome eh {nome} e eu tenho {idade} anos.'
        window['output'].update(output)

window.Close()