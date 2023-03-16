from cryptography.fernet import Fernet
#from PySimpleGUI import PySimpleGUI as sg


#chave = Fernet.generate_key()

#with open('chave.key', 'wb') as filekey:
#    filekey.write(chave)

with open('chave.key', 'rb') as filekey:
    chave = filekey.read()

fernet = Fernet(chave)

with open('arquivo.txt', 'rb') as arquivo:
    conteudo_arquivo = arquivo.read()

criptografado = fernet.encrypt(conteudo_arquivo)
