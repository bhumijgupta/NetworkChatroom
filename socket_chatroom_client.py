import socket;

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	print("Process initialised");
	
except socket.error as err:
	print("Could not setup socket");

#port  over which the computers are connected	
port = 12345;

#ip address of another computer
ip = input("Enter the ip address of the server: ");

with s:
#connecting to the server
	s.connect((ip,port));
	#recieving the data from server
	rec = s.recv(1024);
	print(rec.decode());
	
	while True:
		#Enter message to be sent to server
		data_sent = (input("<< ")).encode();
		s.sendall(data_sent);
		#if empty string is sent
		#connection closes
		if not data_sent:
			break;
		#recieving data from server
		data = s.recv(1024);
		print(">> ",data.decode());

print("Connection closed");

#close the connection
s.close();
