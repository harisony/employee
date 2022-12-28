#pip install get mac
#pip install uuid
##uuid -class
"""
from getmac import get_mac_address as gma
print(gma())
"""
import uuid
print(hex(uuid.getnode()))
#output -hexadecimal
"""
from getmac import get_mac_address as gma
print(gma())
"""
import uuid
print(hex(uuid.getnode()))
print("the mac address in formated way is:",end="")
print(':'.join(['(:02x)'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))#(:-1 - is negative indexing)
#8-bits
#6-parts