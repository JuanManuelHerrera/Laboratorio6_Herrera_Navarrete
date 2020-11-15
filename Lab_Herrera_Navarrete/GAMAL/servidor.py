import socket

def encriptarGamal (MensajeComoString,p,k,Y1):
    m = ''
    aux = []
    for i in MensajeComoString:
        asciivalue =ord(i)
        aux.append(asciivalue)
    for x in range(0,len(aux)):
        aux[x] = (((k**b)*aux[x])%p)
    aux2= str(aux)
    aux2 = aux2.replace("[",'')
    aux2 = aux2.replace("]",'')
    return aux2

      
#Public Key
p = 601
g = 71

#Private Key
b = 69
Y1 = (g**b)%p


#Server initiation

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('',8050))
servidor.listen(1)
cliente, addr = servidor.accept()


#Mensaje encriptado

archivo = open("mensajeentrada.txt","r")
texto = archivo.read()
archivo.close()

cont = 0
while True:
   if cont == 0:
      recibido = cliente.recv(1024)
      k = int(recibido.decode('utf-8'))
      cifrado = encriptarGamal (texto,p,k,Y1)
      archivo = open("mensajeentrada.txt","w")
      archivo.write(cifrado)
      archivo.close()
      
      mens = str(Y1)
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
