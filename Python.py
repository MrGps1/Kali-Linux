#KaliLinux
#All Copyright Save By ---> MrGps
from colorama import Fore
from os import system
from time import sleep
from sys import exit,stdout

def c(s):
	for c in s + "\n":
		stdout.write(c)
		stdout.flush()
		sleep(10./250)
		
c(Fore.GREEN+'''All Cpyrights Save By MrGps

Tool : Download Kali Linux
Fix : Kali Linux
Programmer : MrGps
Telegram : MrGps0

''')

c(Fore.GREEN+'pkg update -y')
system('pkg update -y')

c(Fore.GREEN+'pkg upgrade -y')
system('pkg upgrade -y')

c(Fore.GREEN+'pkg install fish -y')
system('pkg install fish -y')

c(Fore.GREEN+'termux-setup-storage -y')
system('termux-setup-storage -y')

c(Fore.GREEN+'pkg install wget -y')
system('pkg install wget -y')

c(Fore.GREEN+'wget -O install-nethunter-termux https://offs.ec/2MceZWr')
system('wget -O install-nethunter-termux https://offs.ec/2MceZWr')

c(Fore.GREEN+'chmod 777 install-nethunter-termux')
system('chmod 777 install-nethunter-termux')

c(Fore.GREEN+'./install-nethunter-termux')
system('./install-nethunter-termux')

c(Fore.GREEN+'./install-nethunter-termux')
system('./install-nethunter-termux')
