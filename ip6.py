from netmiko import ConnectHandler
CSR = {
      "device_type":"cisco_ios",
      "ip":"sandbox-iosxe-latest-1.cisco.com",
       "username":"developer",
       "password":"C1sco12345"
}
net_connect = ConnectHandler(**CSR)
#Discover the host name from the prompt
hostname = net_connect.send_command('show run | 1 host')
hostname.split(" ")
#hostname,devices,*rest = hostname.split(" ")
hostname, device, *rest = hostname.split(" ")
print("Backing up" + device)
filename = "device04.txt"
showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")
log_file.write("\n")
log_file.write("show vlan")
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
net_connect.disconnect()

