import socket

con = socket.socket()

con.connect(('localhost',8050))
print("Conectado al servidor")

def decriptarRSA(MensajeComoLista,d,n):
    m = ''
    for i in MensajeComoLista:
        m+=(chr((i**d)%n))
    return m
   
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)
      
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        return s%r

cont = 0

while True:
   if cont == 0:
      mens = 'a'
      con.send(mens.encode('ascii'))
      cont = 1

   elif cont == 1:
      recibido = con.recv(1024)
      text = recibido.decode('utf-8')
      text = text.split(',')
      e = int(text[0])
      u = int(text[1])
      n = int(text[2])
      d = mult_inv(e,u)
      mens = 'a'
      con.send(mens.encode('ascii'))
      cont = 2

   else:  
      recibido = con.recv(1024)
      textoCifrado = recibido.decode('utf-8')
      textoCifrado = textoCifrado.split(',')
      array = []
      for num in textoCifrado:
         array.append(int(num))
         
      decifrado = decriptarRSA(array,d,n)
      archivo = open("mensajerecibido.txt","w")
      archivo.write(decifrado)
      archivo.close()
      break
   
con.close()
print("Conexión cerrada")



