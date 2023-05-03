import socket
domainAdi = input('Domain giriniz: ')
print(domainAdi,"=",socket.gethostbyname(domainAdi))