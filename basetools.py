import os
import sys
import shutil
from pathlib import Path

print("O que você deseja fazer?")
print("1 - Limpar SIP DADOS")
print("2 - Mover Backups e FDBS de DISCO")
opcao = input()

if opcao == '1':
    print("Informe o Caminho do seu SIP DADOS")
    print("Exemplo: C:\\Fiorilli\\SIP_7\\SIP_DADOS")

    dir_name = input()

    for root, dirs, files in os.walk(dir_name):
        for f in files: 
            if f.endswith('.FDB'):
                    if f != 'SIP.FDB':
                        print("Excluindo "+root+"\\"+ f)                 
                        os.remove(f)

if opcao == '2':
    print("Informe o Caminho do seu SIP DADOS")
    print("Exemplo: C:\\Fiorilli\\SIP_7\\SIP_DADOS")

    dir_name = input()+'\\'

    print("Informe o Caminho que você quer salvar os Backups")
    
    dest_name = input()+'\\'

    for root,dirs, files in os.walk(dir_name):
        for f in files: 
            if f.endswith('.7z'): 
                dirname = root.split(os.path.sep)[-1]
                if not os.path.exists(dest_name+dirname):
                    os.mkdir(dest_name+dirname)
                    shutil.move(dir_name+dirname+'\\'+f, dest_name+dirname+'\\'+f)
                    print("Criando e movendo dados: "+dest_name+dirname)
                if os.path.exists(dest_name+dirname):
                    if not os.path.exists(dest_name+dirname+'\\'+f):
                        shutil.move(dir_name+dirname+'\\'+f, dest_name+dirname+'\\'+f)
                        print(dir_name+dirname+'\\'+f, dest_name+dirname+'\\'+f)

# primeira versão: 11/03/2021                        
#   ultima versão: 12/03/2021