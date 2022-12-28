from netmiko import ConnectHandler
CSR = {
      "device_type":"cisco_ios",
      "ip":"sandbox-iosxe-latest-1.cisco.com",
       "username":"developer",
       "password":"C1sco12345"
}
net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('show run | i host')
print(output)
