#pip install ifaddr
import ifaddr
adapters = ifaddr.get_adapters()
for adapter in adapters:
    print("IPs of network adapter"+ adapter.nice_name)
    for ip in adapter.ips:
        print("%s %s" %(ip.ip, ip.network_prefix))
#if you wish to include network interfaces thaat do not have a configured ip address,
#pass the include configured parameters adapters with no configured ip address will have an zero-length ip-property.
import ifaddr
adapters = ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("Ipps of network adapter" + adapter.nice_name)
    if adapter.ips:
        for ip in adapter.ips:
            print("%s %s" % (ip.ip, ip.network_prefix))
    else:
        print("no ips's configured")

