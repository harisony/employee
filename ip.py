import os
with open("park1.txt") as file:
    park = file.read()
    park = park.splitlines()
    print("park1 \n")
    #ping for each ip in the file
for ip in park:
    response = os.popen(f"ping {ip} ").read()
    #saving some ping output details to output file
    #Type casting
    if("Request timed out."or"unreachable") in response:
        print(response)
        f = open("park2.txt","a")
        f.write(str(ip) +' link is down'+'\n')
        f.close()
    else:
        print(response)
        f = open("park2.txt","a")
        f.write(str(ip) +' is up'+'\n')
        f.close()
    #print output file to screen
with open("park2.txt") as file:
    output = file.read()
    f.close()
    print(output)
with open("park2.txt","w") as file:
    pass
#input-park1
#output-park2
