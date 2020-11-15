import socket

def encriptarRSA (MensajeComoString,e,n):
    m = ''
    aux = []
    for i in MensajeComoString:
        asciivalue =ord(i)
        aux.append(asciivalue)
    for x in range(0,len(aux)):
        aux[x] = (aux[x]**e)%n
    return aux

def eCalculate(e,u):
    while(u!=0):
        e,u=u,e%u
    return e
      
#Public Key
p = 107
q = 19

n = p*q
u = (p-1)*(q-1)

for i in range(1,1000):
    if(eCalculate(i,u)==1):
        e=i

keys = (p,q,n,u,e)

#Server initiation

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('',8050))
servidor.listen(1)
cliente, addr = servidor.accept()


#Mensaje encriptado

archivo = open("mensajeentrada.txt","r")
texto = archivo.read()
archivo.close()


cifrado = encriptarRSA(texto,e,n)
cifrado = str(cifrado)
cifrado = cifrado.replace('[','').replace(']','')
archivo = open("mensajeentrada.txt","w")
archivo.write(cifrado)
archivo.close()

cont = 0
while True:
   if cont == 0:
      recibido = cliente.recv(1024)
      mens = str(keys[4])+','+str(keys[3])+','+str(keys[2])
      cliente.send(mens.encode('ascii'))
      cont = 1
   elif cont == 1:
      recibido = cliente.recv(1024)
      mens = cifrado
      cliente.send(mens.encode('ascii'))
      cont = 2
   else:
      recibido = cliente.recv(1024)
      break
      
   
    

cliente.close()
servidor.close()

print("Conexiones cerradas")
