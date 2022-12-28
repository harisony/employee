import os, ipaddress
os.system('cls') #os.-system will clear the console at the start of the execution
while True:
    ip = input("Enter Ip Address:")
    try:
        print(ipaddress.ip_address(ip))
        print("Ip valid")
    except:
        print('-' *50)
        print('Ip is not valid')
    finally:
        if ip=='mango':
            print('Script Finished')
            break