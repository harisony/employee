from scapy.all import *

a=IP(ttl=10)
print(a)
print(a.src)

'''

""" 
a.dst="192.168.1.1"
print(a)
print(a.src)
"""

""""del(a.ttl)
print(a.show())

b=IP()
print (b.show())
"""

c = IP()/TCP()
print(c.show())

d=Ether()/IP()/TCP()
print(d.show())

e = IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"
print(e.show())


f = Ether()/IP()/IP()/UDP()
print(f.show())

g = IP(proto=55)/TCP()
print(g.show())

h = raw(IP())
#print(h.show())
print(h)
###########
'''