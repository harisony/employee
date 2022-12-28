import sys
print("python version my local machine:",sys.version)
####
import ip1
hostname = socket.gethostname()
print(hostname)
ipadd = socket.gethostbyname(hostname)
print(ipadd)