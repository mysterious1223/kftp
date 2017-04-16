import os
import socket
import sys
from thread import *


# command line for address and port
# client sends file size and file name, We can dynamically all space

address="127.0.0.1"
port=5679
s_default = 1024*10

def process(_data):
	count=0
	file_name = _data[0]
	file_name=file_name.strip()
	curr_dir=os.path.dirname(os.path.realpath(__file__))
	os.system("touch "+curr_dir+"/transfers/"+ file_name)
	file = open(curr_dir+"/transfers/"+file_name,"w")
	#print _data[0]
	print "+ Creating file..."
	for f in _data:
		if count>0:
			file.write(f)
			print str((float(count)/float(len(_data)))*100)+"%"
		count+=1
	print "100.0%"
	print "+ done!"
	file.close()

def clientConnect(conn):
	conn.send("Connected to server... Welcome!\n")
	_data=[]
	while 1:
		
			# client sends in packets of s_default at a time
		try:
		
			data=conn.recv(s_default)
		except:
			print "done..."
			process(_data)
			break
			#conn.sendall("Done!")
			#s_default=1000
		#print data
		_data.append(data)
		#reply = "Message Recieved!\n"
		if data.strip() == "q":
			print "+ Kill connection requested!"
			conn.close()
		
			print "+ Listening..."
			break
			#print "\n"
		
		#try:
		#conn.sendall(reply)
		
	#print "+ Listening for new connection!"
	#conn.close()

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "+ Starting..."

	try:
		s.bind((address, port))
	except:
		print "+ FAILED"
		sys.exit()

	print "+ INITIALIZING"
	s.listen(10)
	
	print "+ Waiting for connection"
	while 1:
		
		try:
			conn, addr = s.accept()
			print "Connected!"
			start_new_thread(clientConnect, (conn,))
		except:
			s.close
			sys.exit()
			
		
	s.close

if __name__ == "__main__":
	main()
	
