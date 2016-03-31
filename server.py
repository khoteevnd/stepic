from socket import *

def myrecv(sock, msglen):                                                        
  msg = ''                                                                       
  while len(msg) < msglen:                                                       
    chunk = sock.recv(msglen-len(msg))                                           
    if chunk == '':                                                              
      print("chunk = "+chunk)                                                    
      raise RuntimeError("broken")                                               
    msg = msg + chunk                                                            
  return msg                                                                     

mysock = socket(AF_INET, SOCK_STREAM)
addr = ("0.0.0.0",2222)
mysock.bind(addr)
mysock.listen(10)
mysock.setblocking(1)
#mysock.settimeout(20.0)
 
 
while 1:
	clientsock, addr = mysock.accept()
	while 1:
		data=clientsock.recv(1024)
		print (data)
		clientsock.send(bytes("you sent " + str(data), encoding='utf8'))
		if (data=="close"):
			clientsock.close()
			break 
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                            
#s.bind(('0.0.0.0', 2222))                                                        
#s.listen(10)                                                                     
 
#data = ""                                                                        

#while True:                                                                      
#  conn, addr = s.accept()                                                        
#  print("Conect: "+ str(addr))                                                   
#  while True:                                                                    
#    data += conn.recv(conn, 1024)                                                
#    print(data)                                                                  
#    if data == 'close': break                                                    
#    conn.send(data)                                                              
#  conn.close()    
