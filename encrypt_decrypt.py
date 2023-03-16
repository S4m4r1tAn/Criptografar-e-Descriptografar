import PySimpleGUI as sg
from cryptography.fernet import Fernet


def encrypt(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode())

def decrypt(text, key):
    f = Fernet(key)
    return f.decrypt(text).decode()

def main():
    sg.theme('Python')

    layout = [[sg.Text('Escolha uma opção:')],
              [sg.Button('Encrypt'), sg.Button('Decrypt')]]

    window = sg.Window('Criptografar/Descriptografar', layout)

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Encrypt':
            layout2 = [[sg.Text('Insira o texto a ser criptografado:')],
                       [sg.Input(key='-TEXT-')],
                       [sg.Button('Criptografar')]]

            window2 = sg.Window('Encrypt', layout2)

            while True:
                event2, values2 = window2.read()
                if event2 == sg.WIN_CLOSED:
                    break
                if event2 == 'Criptografar':
                    text = values2['-TEXT-']
                    with open('chave.key', 'rb') as filekey:
                        key = filekey.read()
                    criptografado = encrypt(text, key)

                    layout3 = [[sg.Text('Resultado:')],
                               [sg.Multiline(key='-RESULT-', default_text=criptografado.decode(), size=(80, 5))],
                               [sg.Button('Visualizar'), sg.Button('Salvar'), sg.Button('Download'), sg.Button('Fechar')]]

                    window3 = sg.Window('Resultado', layout3)

                    while True:
                        event3, _ = window3.read()
                        if event3 == sg.WIN_CLOSED or event3 == 'Fechar':
                            break
                        if event3 == 'Salvar':
                            filename = sg.popup_get_file('Salvar como', save_as=True)
                            if filename:
                                with open(filename, 'w') as f:
                                    f.write(descriptografado)
                        if event3 == 'Download':
                            filename = sg.popup_get_file('Salvar como', save_as=True)
                            if filename:
                                with open(filename, 'w') as f:
                                    f.write(descriptografado.encode())
                        if event3 == 'Visualizar':
                            sg.popup_scrolled(criptografado.decode(), title='Resultado Criptografado')

                    window3.close()

            window2.close()

        if event == 'Decrypt':
            layout2 = [[sg.Text('Insira o texto a ser descriptografado:')],
                       [sg.Input(key='-TEXT-')],
                       [sg.Button('Descriptografar')]]

            window2 = sg.Window('Decrypt', layout2)

            while True:
                event2, values2 = window2.read()
                if event2 == sg.WIN_CLOSED:
                    break
                if event2 == 'Descriptografar':
                    text = values2['-TEXT-']
                    with open('chave.key', 'rb') as filekey:
                        key = filekey.read()
                    descriptografado = decrypt(text.encode(), key)

                    layout3 = [[sg.Text('Resultado:')],
                               [sg.Multiline(key='-RESULT-', default_text=descriptografado.decode(), size=(80, 5))],
                               [sg.Button('Visualizar'), sg.Button('Salvar'), sg.Button('Download'), sg.Button('Fechar')]]

                    window3 = sg.Window('Resultado', layout3)

                    while True:
                        event3, _ = window3.read()
                        if event3 == sg.WIN_CLOSED or event3 == 'Fechar':
                            break
                        if event3 == 'Salvar':
                            filename = sg.popup_get_file('Salvar como', save_as=True)
                            if filename:
                                with open(filename, 'w') as f:
                                    f.write(descriptografado)
                        if event3 == 'Download':
                            filename = sg.popup_get_file('Salvar como', save_as=True)
                            if filename:
                                with open(filename, 'w') as f:
                                    f.write(descriptografado.encode())
                        if event3 == 'Visualizar':
                            sg.popup_scrolled(descriptografado.decode(), title='Resultado Descriptorgafado')

                    window3.close()

            window2.close()

        window.close()

if __name__ == '__main__':
    main()
