from scapy.all import *

'''a=IP(tt1=10)
print(a)
print(a.src)'''
'''
a.data="192.168.1.1"
var1=a.src
print(var1.show())
print(a)
print(a.src)
'''
'''del(a.tt1)
print(a.show())

b=IP()
print(b.show())'''

#for the packet manipulation#
c=IP()/TCP()
print(c.show())
d=Ether()/IP()/TCP()
print(d.show())
''''

'''