import os,time,sys
from colorama import init
init()
from colorama import Fore, Back, Style


print (Fore.RED+'''

██████╗ ██╗███╗  ██╗ ██████╗ ███████╗██████╗
██╔══██╗██║████╗ ██║██╔════╝ ██╔════╝██╔══██╗
██████╔╝██║██╔██╗██║██║  ██╗ █████╗  ██████╔╝
██╔═══╝ ██║██║╚████║██║  ╚██╗██╔══╝  ██╔══██╗
██║     ██║██║ ╚███║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

''')

ipurl = input('Enter the IP or The URL You Want To Attack: ')
os.system('ping '+ ipurl)
time.sleep(3)
print ("\n ")
print ("Press Enter To Exit")
input ("")
    