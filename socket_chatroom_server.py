import socket

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	print("Process initiated");

except socket.error as err:
	print("Socket creation failed");
	
port = 12345;

#we will bind the server to listen for requests
#since we have used empty string instead of ipaddress
#server will listen to requests coming from any
#computer on the network
s.bind(('', port));
print("Socket binded to: ", port);

#socket will allow 5 unaccepted connections
#are kept waiting
#then it will refuse new connections
s.listen(5);
print("Socket is listening");

while True:
	#accept the connection
	#it returns socket object and
	#adddress of the client
	conn, add = s.accept();
	with conn:
		print("Got connection from ",add);
		conn.send(b"Connection successful");
		while True:
			data = conn.recv(1024);
			#if no data i.e. empty string is recieved
			#the connection will be closed
			if not data:
				break;
			print(">> ",data.decode());
			#Enter message you want to send to client
			data_sent = (input("<< ")).encode()
			conn.sendall(data_sent);
		print("Connection closed");
s.close();
