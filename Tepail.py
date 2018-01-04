#!/usr/bin/python3
#
#
import os
import requests
import random
import time

eDisp = []
irnd = str(random.choice(range(1,9)))
print("""[""""\033[3""" + irnd + """;1m*\033[0;0m] Iniciando programa...""")

def emailsDisponiveis():
    req = requests.get("https://temp-mail.org/pt/option/change/")
    temp = open('.TmpReq', 'w')
    temp.write(req.text)
    temp.close()
    os.system("cat .TmpReq | grep '<option' | cut -d '\"' -f2 > .eTmpList")
    os.system('rm .TmpReq')
    dispEmails = open('.eTmpList', 'r')
    i=1
    for e in dispEmails.readlines():
        eDisp.append("\033[3"+irnd+";1m"+str(i)+'\033[0;0m) '+e.rstrip())
        i+=1
    os.system("rm .eTmpList")
print("""[""""\033[3""" + irnd + """;1m*\033[0;0m] Verificando dominios disponiveis...""")
emailsDisponiveis()

def sairProgram():
    print("\n\033[3" + irnd + ";1m"+" Obrigado por utilizar o Tepail! Volte sempre :)")
    print('\n  A liberdade foi confundida com a democracia.\n \033[0;0m')
    exit(0)

def emailCriado(eCreate):
    while True:
        try:
            req = requests.get('https://temp-mail.org/pt/?email='+eCreate)
            receb = len(req.text.split('class="link"'))-1
            if receb < 0:
                receb = 0
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
                       \033[1mv1.0\033[0;0m
                           
 E-mails recebidos » \033[3""" + irnd + """;1m%s\033[0;0m """ % str(receb) + """ 
 E-mail            » \033[3""" + irnd + """;1m%s\033[0;0m""" % eCreate +"""
 Link              » \033[3""" + irnd + """;1mhttps://temp-mail.org/pt/?email=%s\033[0;0m
                """ % eCreate)
            time.sleep(30)
        except KeyboardInterrupt:
            try:
                print('\n\033[31;1m [!] Você deseja realmente sair? [S/n]\033[0;0m')
                sair = input(' Tepail » ')
                if sair.lower() != 'n':
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
                       \033[1mv1.0\033[0;0m
    
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
                print("""[""""\033[3""" + irnd + """;1m*\033[0;0m] Criando e-mail...""")
                dom = eDisp[dom-1].split(' ')[1].rstrip()
                compltEm = enderec.rstrip()+dom.rstrip()
                emailCriado(compltEm)
            else:
                print(' \033[31;1m[!] O endereço não pode ser vazio ou conter espaços.\033[0;0m')
                time.sleep(2)
                continue
        else:
            print("\033[31;1m[!] Dominio não existente.\033[0;0m")
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