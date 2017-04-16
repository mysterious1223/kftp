import os
import socket
import sys
import time
address=""
port=""
message=""
file_size=0
myfile_path=""
#filecontents=[]
# kftp "address" "port" file.txt | text for now
def getSize(file):
	file.seek(0,2)
	size = file.tell()
	return size
def convert_file_to_bytes(path):
	filecontents=[]
	print path
	print "converting"
	#open file and print to array
	with open(path) as f:
		filecontents=f.readlines()

	#for f in filecontents:
	#	print f.strip()

	print "+ Done conversion"
	return filecontents

def connect(file_name,file_size,file_contents):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (sys.argv[1], int(sys.argv[2]))
	sock.connect(server_address)
	file_size = len(file_contents)
	count = 0
	while 1:
	
		sock.sendall(file_name+"\n")
		time.sleep(.05)
		for f in file_contents:
			sock.sendall(f)
			time.sleep(.0025)
			count += 1
			print str(100*(float(count)/float (file_size)))+"%"
			
		break		
	sock.close()

def main():
	


	if len(sys.argv) == 4:
		curr_dir=os.path.dirname(os.path.realpath(__file__))
		myfile = curr_dir+"/"+sys.argv[3]
		file = open(myfile,"rb")
		file_name=sys.argv[3]
		file_size = getSize(file)
		file.close()
		#print "size ["+str(file_size)+"]"
		file_contents=convert_file_to_bytes(myfile)
		connect(file_name,file_size,file_contents)
	else:
		print "+ Error invalid arguments"



if __name__ == "__main__":
	main()
