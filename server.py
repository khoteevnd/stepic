import socket, sys

def myrecv(sock, msglen):
  msg = ''
  while len(msg) < msglen:
    chunk = sock.recv(msglen-len(msg))
    if chunk == '':
      raise RuntimeError("broken")
    msg = msg + chunk
  return msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
  conn, addr = s.accept()
  while True:
    data = myrecv(conn, 64)
    if not data: break
    conn.send(data)
  conn.close()
