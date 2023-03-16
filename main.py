from cryptography.fernet import Fernet
#from PySimpleGUI import PySimpleGUI as sg

#chave = Fernet.generate_key()

#with open('chave.key', 'wb') as filekey:
#    filekey.write(chave)

with open('Criptografar_e_Descriptografar/chave.key', 'rb') as filekey:
    chave = filekey.read()

fernet = Fernet(chave)

#with open('Criptografar_e_Descriptografar/arquivo.txt', 'rb') as arquivo:
#    conteudo_arquivo = arquivo.read()

#criptografado = fernet.encrypt(conteudo_arquivo)

#with open('Criptografar_e_Descriptografar/arquivo1.txt', 'wb') as arquivo_criptografado:
#    arquivo_criptografado.write(criptografado)# type: ignore
    
with open('Criptografar_e_Descriptografar/arquivo1.txt', 'rb') as arquivo_criptografado:
    criptografado = arquivo_criptografado.read()
    
descriptografado = fernet.decrypt(criptografado)
