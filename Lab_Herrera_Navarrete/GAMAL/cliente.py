import socket

con = socket.socket()

con.connect(('localhost',8050))
print("Conectado al servidor")

def decriptarGamal(MensajeEncriptado,p,Y1,a):
    Mensaje = MensajeEncriptado.split(",")
    for j in range(0,len(Mensaje)):
        Mensaje[j]=int(Mensaje[j])
    m = ''
    for i in Mensaje:
        m += chr(((Y1**(p-1-a)*i)%p))
    return m

#Public Key
p = 601
g = 71

#Private Key
a = 60
k = (g**a)%p


cont = 0

while True:
   if cont == 0:
      mens = str(k)
      con.send(mens.encode('ascii'))
      cont = 1

   elif cont == 1:
      recibido = con.recv(1024)
      Y1 = int(recibido.decode('utf-8'))
      mens = 'a'
      con.send(mens.encode('ascii'))
      cont = 2

   else:  
      recibido = con.recv(1024)
      textoCifrado = recibido.decode('utf-8')
      
      decifrado = decriptarGamal(textoCifrado,p,Y1,a)
      archivo = open("mensajerecibido.txt","w")
      archivo.write(decifrado)
      archivo.close()
      break
   
con.close()
print("Conexión cerrada")



