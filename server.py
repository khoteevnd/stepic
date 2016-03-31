import socket, sys                                                               

def myrecv(sock, msglen):                                                        
  msg = ''                                                                       
  while len(msg) < msglen:                                                       
    chunk = sock.recv(msglen-len(msg))                                           
    if chunk == '':                                                              
      print("chunk = "+chunk)                                                    
      raise RuntimeError("broken")                                               
    msg = msg + chunk                                                            
  return msg                                                                     
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                            
s.bind(('0.0.0.0', 2222))                                                        
s.listen(10)                                                                     
 
data = ""                                                                        

while True:                                                                      
  conn, addr = s.accept()                                                        
  print("Conect: "+ str(addr))                                                   
  while True:                                                                    
    data += conn.recv(conn, 1024)                                                
    print(data)                                                                  
    if data == 'close': break                                                    
    conn.send(data)                                                              
  conn.close()    
