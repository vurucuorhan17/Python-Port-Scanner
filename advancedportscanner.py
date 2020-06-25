
#Author: Orhan Furkan VURUCU

from threading import *
from socket import *
import optparse
from termcolor import colored

def connectScan(targetHost,targetPort):
	try:
		sock = socket(AF_INET,SOCK_STREAM) # TCP bağlantısı oluşturma
		sock.connect((targetHost,targetPort)) # Parametre olarak verilen hostun portuna bağlantı sağlama.
		print(colored("[+] %d/tcp open" %targetPort,'green'))
	except:
		print(colored("[-] %d/tcp closed" %targetPort,'red'))
	finally:
		sock.close()

def portScan(targetHost,targetPorts):
	try:
		targetIP = gethostbyname(targetHost)
	except:
		print("Bilinmeyen Host: %s" %targetHost)
	try:
		targetName = gethostbyaddr(targetIP)
		print("[+] " + targetName[0] + "için arama sonuçları")
	except:
		print("[+] " + targetIP + "için arama sonuçları")
	setdefaulttimeout(1)
	for targetPort in targetPorts:
		t = Thread(target=connectScan,args=(targetHost,int(targetPort)))
		t.start()

def main():
	parser = optparse.OptionParser("Programin kullanimi: " + "-H <Hedef IP>"
				      + " -p <Hedef Port>")
	parser.add_option('-H',dest='targetHost',type='string',help='Belirlenen Hedef IP Adresini veya Domaini girin')
	parser.add_option('-p',dest='targetPort',type='string',help='Belirlenen Hedef Port veya Portlari virgul ile ayirarak girin')
	(options,args) = parser.parse_args()
	targetHost = options.targetHost
	targetPorts = str(options.targetPort).split(',')
	if (targetHost == None) | (targetPorts[0] == None):
		print(parser.usage)
		exit(0) 
	portScan(targetHost,targetPorts)

if __name__ == '__main__':
	main()
