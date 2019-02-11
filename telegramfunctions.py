from json import load
from urllib import request
from subprocess import Popen,PIPE
def get_myIP():
    print(load(request.urlopen('http://jsonip.com'))['ip'])

def compare_myIP(old_ip):
    proc=Popen(['/bin/bash'],stdin=PIPE, stdout=PIPE )
    print(proc.communicate('ls '))
if __name__ == "__main__":
    get_myIP()