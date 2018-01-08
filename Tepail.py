#!/usr/bin/python3
#
#
import os
import requests
import random
import time
from bs4 import BeautifulSoup

eDisp = []
irnd = str(random.choice(range(1,7)))
print("""[""""\033[3""" + irnd + """;1m*\033[0;0m] Iniciando programa...""")

def emailsDisponiveis():
    req = requests.get("https://temp-mail.org/pt/option/change/")
    soup = BeautifulSoup(req.text, 'html.parser')
    i=1
    for e in soup.find_all('option'):
        eDisp.append("\033[3"+irnd+";1m"+str(i)+'\033[0;0m) '+e.attrs['value'].rstrip())
        i+=1
print("""[""""\033[3""" + irnd + """;1m*\033[0;0m] Verificando dominios disponiveis...""")
emailsDisponiveis()

def sairProgram():
    print("\n\033[3" + irnd + ";1m"+" Obrigado por utilizar o Tepail! Volte sempre :)")
    print('\n  A liberdade foi confundida com a democracia.\n \033[0;0m')
    exit(0)

def emailCriado(eCreate):
    iant = 0
    while True:
        try:
            req = requests.get('https://temp-mail.org/pt/?email='+eCreate)
            soup = BeautifulSoup(req.text, 'html.parser')
            receb = len(soup.find_all('a', class_="link"))
            os.system('clear')
            print("""
    \033[3""" + irnd + """;1m                   ,,╓╓╓╓,           \033[0;0m
    \033[3""" + irnd + """;1m              ,▄███▀▀\"\"\"\"▀▀███▄  \033[0;0m  
    \033[3""" + irnd + """;1m            ╓██▀             `██▄    \033[0;0m
    \033[3""" + irnd + """;1m           ██▀    ▄█████▄  ██  ▀██   \033[0;0m
    \033[3""" + irnd + """;1m          ██    ███`    `███▌   ██   \033[0;0m
    \033[3""" + irnd + """;1m         ║█▌   ██▌       ▐██    ██   \033[0;0m
    \033[3""" + irnd + """;1m         ██   .██        ██▌    ██   \033[0;0m
    \033[3""" + irnd + """;1m         ██   ▐██       ███    ▄█▌   \033[0;0m
    \033[3""" + irnd + """;1m         ██▌   ███,  ,██ ██  ,██▀    \033[0;0m
    \033[3""" + irnd + """;1m          ██▄   `▀▀▀▀▀   `▀▀▀▀`      \033[0;0m
    \033[3""" + irnd + """;1m           ▀██w            ,▄▄       \033[0;0m
    \033[3""" + irnd + """;1m             `▀████████████▀▀        \033[0;0m
    
    \033[1mLucas Simoni <alivemindset@protonmail.com>\033[0;0m
                       \033[1mv2.0\033[0;0m
                           
 E-mails recebidos » \033[3""" + irnd + """;1m%s\033[0;0m """ % str(receb) + """ 
 E-mail            » \033[3""" + irnd + """;1m%s\033[0;0m""" % eCreate+'\n')
            if iant < receb:
                titles = soup.find_all('a', class_="title-subject")
                print("\n [\033[31;1m!\033[0;0m] Você tem um novo e-mail - "+titles[iant].attrs['title']+" \033[0;0m")
                iant+=1
            print("\n\n [\033[3"+irnd+";1m*\033[0;0m] Aperte CTRL+C para ler sua caixa de entrada.\033[0;0m")
            time.sleep(10)
        except KeyboardInterrupt:
            try:
                print('\n\033[31;1m [!] Você deseja fazer o que?\033[0;0m')
                print('\n\033[3'+irnd+';1m 1\033[0;0m- Ver caixa de entrada\033[0;0m')
                print('\033[3'+irnd+';1m 2\033[0;0m- Sair\n\033[0;0m')
                sair = str(input(' Tepail » '))
                print('\n')
                if sair.lower() == '1':
                    i=1
                    print('\n=============== \033[3' + irnd + ';1m Caixa de entrada \033[0;0m=============== \n')
                    for title in titles:
                        print(' ('+'\033[3'+irnd+';1m'+str(i)+'\033[0;0m) '+title.attrs['title'])
                        i+=1
                    try:
                        chose = int(input('\n E-mail » '))
                    except ValueError:
                        print("\n\033[31;1m [!] E-mail não existe!\033[0;0m")
                        time.sleep(5)
                        continue
                    if chose > receb:
                        print("\n\033[31;1m [!] E-mail não existe!\033[0;0m")
                        time.sleep(5)
                        continue
                    else:
                        i = chose
                        chose = titles[chose-1].attrs['href']
                        titulo = titles[i-1].attrs['title']
                        req = requests.get(chose)
                        soup = BeautifulSoup(req.text, 'html.parser')
                        div = soup.find_all('div')[23]
                        os.system('clear')
                        print('\n\n===================== \033[3'+irnd+';1m'+titulo+' \033[0;0m===================== \n')
                        for texto in div:
                            txtp = texto.string
                            if txtp == None:
                                print(' ')
                                continue
                            print('  '+txtp)
                        print('\n===================== \033[3' + irnd + ';1m' + titulo + ' \033[0;0m===================== \n')
                        input('\n\nAperte ENTER para continuar...')
                elif sair.lower() == '2':
                    sairProgram()
                else:
                    pass
            except KeyboardInterrupt:
                sairProgram()
            except EOFError:
                sairProgram()
        except EOFError:
            sairProgram()

while True:
    try:
        os.system('clear')
        print("""
    \033[3""" + irnd + """;1m                   ,,╓╓╓╓,           \033[0;0m
    \033[3""" + irnd + """;1m              ,▄███▀▀\"\"\"\"▀▀███▄  \033[0;0m  
    \033[3""" + irnd + """;1m            ╓██▀             `██▄    \033[0;0m
    \033[3""" + irnd + """;1m           ██▀    ▄█████▄  ██  ▀██   \033[0;0m
    \033[3""" + irnd + """;1m          ██    ███`    `███▌   ██   \033[0;0m
    \033[3""" + irnd + """;1m         ║█▌   ██▌       ▐██    ██   \033[0;0m
    \033[3""" + irnd + """;1m         ██   .██        ██▌    ██   \033[0;0m
    \033[3""" + irnd + """;1m         ██   ▐██       ███    ▄█▌   \033[0;0m
    \033[3""" + irnd + """;1m         ██▌   ███,  ,██ ██  ,██▀    \033[0;0m
    \033[3""" + irnd + """;1m          ██▄   `▀▀▀▀▀   `▀▀▀▀`      \033[0;0m
    \033[3""" + irnd + """;1m           ▀██w            ,▄▄       \033[0;0m
    \033[3""" + irnd + """;1m             `▀████████████▀▀        \033[0;0m
    
    \033[1mLucas Simoni <alivemindset@protonmail.com>\033[0;0m
                       \033[1mv2.0\033[0;0m
    
            """)
        tam = len(eDisp)
        i=0
        n=0
        try:
            for intei in range(n, tam):
                print("     %s\t\t%s" %(eDisp[i],eDisp[i+1]))
                i+=2
        except IndexError:
            err=True
        try:
            dom = int(input("\n Selecione um dominio » "))
        except ValueError:
            print("\033[31;1m[!] Dominio não existente.\033[0;0m")
            time.sleep(2)
            continue
        if dom < tam+1 and dom > 0:
            print(" Selecionado » ", eDisp[dom-1].split(')')[1].rstrip())
            print(" \033[31;1m[!] Digite um endereço de no máximo 32 caracteres.\033[0;0m")
            enderec = input(" Digite um endereço » ")
            if len(enderec) > 32:
                print(' \033[31;1m[!] O endereço não pode passar 32 caracteres.\033[0;0m')
                time.sleep(2)
                continue
            elif len(enderec) < 1:
                print('\033[31;1m[!] O endereço não pode ser menor que 1 caractere.\033[0;0m')
                time.sleep(2)
                continue
            if enderec.find(' ') < 0:
                print(""" [""""\033[3""" + irnd + """;1m*\033[0;0m] Criando e-mail...""")
                dom = eDisp[dom-1].split(' ')[1].rstrip()
                compltEm = enderec.rstrip()+dom.rstrip()
                emailCriado(compltEm)
            else:
                print(' \033[31;1m[!] O endereço não pode ser vazio ou conter espaços.\033[0;0m')
                time.sleep(2)
                continue
        else:
            print(" \033[31;1m[!] Dominio não existente.\033[0;0m")
            time.sleep(2)
            continue
    except KeyboardInterrupt:
        try:
            print('\n\033[31;1m [!] Você deseja realmente sair? [S/n]\033[0;0m')
            sair = input(' Tepail » ')
            if sair.lower() != 'n':
                sairProgram()
            else:
                continue
        except KeyboardInterrupt:
            sairProgram()
        except EOFError:
            sairProgram()
    except EOFError:
        sairProgram()